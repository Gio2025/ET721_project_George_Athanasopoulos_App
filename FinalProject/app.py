import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory

app = Flask(__name__)

app.secret_key = "student_secret_key"

UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# --------------------------------
# DATABASE CONNECTION
# --------------------------------
def get_db():
    conn = sqlite3.connect("student_app.db")
    conn.row_factory = sqlite3.Row
    return conn


# --------------------------------
# FILE VALIDATION
# --------------------------------
def allowed_file(filename):

    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# --------------------------------
# HOME
# --------------------------------
@app.route('/')
def home():

    return redirect(url_for('login'))


# --------------------------------
# SIGNUP
# --------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()

        try:

            cursor.execute("""
            INSERT INTO users(username, email, password)
            VALUES (?, ?, ?)
            """, (username, email, password))

            conn.commit()

            flash("Account created successfully!")

            return redirect(url_for('login'))

        except sqlite3.IntegrityError:

            flash("Email already exists!")

        finally:

            conn.close()

    return render_template('signup.html')


# --------------------------------
# LOGIN
# --------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM users
        WHERE email=? AND password=?
        """, (email, password))

        user = cursor.fetchone()

        conn.close()

        if user:

            session['user_id'] = user['id']
            session['username'] = user['username']

            return redirect(url_for('dashboard'))

        else:

            flash("Invalid email or password")

    return render_template('login.html')


# --------------------------------
# DASHBOARD
# --------------------------------
@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        username=session['username']
    )


# --------------------------------
# LOGOUT
# --------------------------------
@app.route('/logout')
def logout():

    session.clear()

    return redirect(url_for('login'))


# --------------------------------
# TASKS
# --------------------------------
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':

        title = request.form['title']
        category = request.form['category']
        due_date = request.form['due_date']

        cursor.execute("""
        INSERT INTO tasks(user_id, title, category, due_date)
        VALUES (?, ?, ?, ?)
        """, (
            session['user_id'],
            title,
            category,
            due_date
        ))

        conn.commit()

    cursor.execute("""
    SELECT * FROM tasks
    WHERE user_id=?
    """, (session['user_id'],))

    all_tasks = cursor.fetchall()

    conn.close()

    return render_template(
        'tasks.html',
        tasks=all_tasks
    )


# --------------------------------
# COMPLETE TASK
# --------------------------------
@app.route('/complete_task/<int:id>')
def complete_task(id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET completed=1
    WHERE id=?
    """, (id,))

    conn.commit()
    conn.close()

    return redirect(url_for('tasks'))


# --------------------------------
# DELETE TASK
# --------------------------------
@app.route('/delete_task/<int:id>')
def delete_task(id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM tasks
    WHERE id=?
    """, (id,))

    conn.commit()
    conn.close()

    return redirect(url_for('tasks'))


# --------------------------------
# BLOGS
# --------------------------------
@app.route('/blogs')
def blogs():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM blogs
    ORDER BY id DESC
    """)

    all_blogs = cursor.fetchall()

    conn.close()

    return render_template(
        'blogs.html',
        blogs=all_blogs
    )


# --------------------------------
# CREATE BLOG
# --------------------------------
@app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':

        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO blogs(user_id, title, content, category)
        VALUES (?, ?, ?, ?)
        """, (
            session['user_id'],
            title,
            content,
            category
        ))

        conn.commit()
        conn.close()

        return redirect(url_for('blogs'))

    return render_template('create_blog.html')


# --------------------------------
# LIKE BLOG
# --------------------------------
@app.route('/like_blog/<int:id>')
def like_blog(id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE blogs
    SET likes = likes + 1
    WHERE id=?
    """, (id,))

    conn.commit()
    conn.close()

    return redirect(url_for('blogs'))


# --------------------------------
# UPLOAD NOTE
# --------------------------------
@app.route('/upload_note', methods=['GET', 'POST'])
def upload_note():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':

        file = request.files['image']
        subject = request.form['subject']

        if file and allowed_file(file.filename):

            filename = file.filename

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    filename
                )
            )

            conn = get_db()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO notes(user_id, image, subject)
            VALUES (?, ?, ?)
            """, (
                session['user_id'],
                filename,
                subject
            ))

            conn.commit()
            conn.close()

            flash("Image uploaded successfully!")

            return redirect(url_for('notes'))

        else:

            flash("Invalid file type")

    return render_template('upload_note.html')


# --------------------------------
# NOTES
# --------------------------------
@app.route('/notes')
def notes():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM notes
    WHERE user_id=?
    """, (session['user_id'],))

    all_notes = cursor.fetchall()

    conn.close()

    return render_template(
        'notes.html',
        notes=all_notes
    )


# --------------------------------
# DOWNLOAD NOTE
# --------------------------------
@app.route('/download/<filename>')
def download_file(filename):

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )


# --------------------------------
# RUN APP
# --------------------------------
if __name__ == '__main__':

    app.run(debug=True)