import os
import sqlite3
import pytest

from app import app

TEST_DB = "test_student_app.db"


# --------------------------------
# TEST DATABASE
# --------------------------------
def init_test_db():

    conn = sqlite3.connect(TEST_DB)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


# --------------------------------
# TEST CLIENT
# --------------------------------
@pytest.fixture
def client(monkeypatch):

    def test_get_db():

        conn = sqlite3.connect(TEST_DB)

        conn.row_factory = sqlite3.Row

        return conn

    monkeypatch.setattr(
        "app.get_db",
        test_get_db
    )

    app.config['TESTING'] = True

    init_test_db()

    with app.test_client() as client:

        yield client

    if os.path.exists(TEST_DB):

        os.remove(TEST_DB)


# --------------------------------
# HOME REDIRECT TEST
# --------------------------------
def test_home_redirect(client):

    response = client.get('/')

    assert response.status_code == 302


# --------------------------------
# SIGNUP TEST
# --------------------------------
def test_signup(client):

    response = client.post('/signup', data={
        "username":"testuser",
        "email":"test@test.com",
        "password":"123456"
    }, follow_redirects=True)

    assert response.status_code == 200


# --------------------------------
# LOGIN TEST
# --------------------------------
def test_login(client):

    client.post('/signup', data={
        "username":"loginuser",
        "email":"login@test.com",
        "password":"123456"
    })

    response = client.post('/login', data={
        "email":"login@test.com",
        "password":"123456"
    }, follow_redirects=True)

    assert b"Welcome" in response.data