import sqlite3

conn = sqlite3.connect("student_app.db")
cursor = conn.cursor()

# -----------------------------
# USERS TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# -----------------------------
# TASKS TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT NOT NULL,
    category TEXT,
    due_date TEXT,
    completed INTEGER DEFAULT 0,

    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# -----------------------------
# BLOGS TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS blogs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    category TEXT,
    likes INTEGER DEFAULT 0,

    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# -----------------------------
# NOTES TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    image TEXT,
    subject TEXT,

    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()

print("Database created successfully!")