# ET721_project_George_Athanasopoulos

# Student Learning Management App

## Project Overview

The Student Learning Management App is a full-stack web application developed using the Flask framework and SQLite database. The purpose of this application is to help students improve productivity, manage academic responsibilities, and organize learning materials in one centralized platform.

The application provides students with useful academic tools such as:

- A Task Management (To-Do List) system
- A Blogging platform
- An Image Upload feature for notes and study materials

This project demonstrates full-stack web development concepts including backend development, frontend design, database management, routing, authentication, file uploads, and responsive user interface design.

---

# Features

## User Authentication System

- User Signup
- User Login
- Session Management
- Logout Functionality

Users must log in to access personal features such as tasks, blogs, and uploaded notes.

---

## Task Management System

Students can:

- Create tasks
- Organize tasks by category
- Add due dates
- Mark tasks as completed
- Delete tasks

This feature helps students stay organized and manage deadlines efficiently.

---

## Blog System

Students can:

- Create blog posts
- Share learning experiences
- Add blog categories
- Like blog posts

The blogging feature encourages collaboration and reflection on learning experiences.

---

## Notes Upload System

Students can:

- Upload note images
- Organize notes by subject
- Preview uploaded images
- Download uploaded notes

This feature helps students store and access study materials easily.

---

# Technologies Used

## Backend
- Flask (Python)

## Frontend
- HTML
- CSS
- JavaScript

## Database
- SQLite

---

# Project Structure

```text
FinalProject/
│
├── app.py
├── init_db.py
├── test_app.py
├── student_app.db
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── uploads/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── tasks.html
│   ├── blogs.html
│   ├── create_blog.html
│   ├── notes.html
│   └── upload_note.html
│
└── README.md
```

---

# File Descriptions

## Main Python Files

### app.py
Main Flask application containing:
- Routes
- Database connections
- Authentication logic
- Task management logic
- Blog functionality
- File upload functionality

### init_db.py
Creates the SQLite database and initializes all required tables:
- users
- tasks
- blogs
- notes

### test_app.py
Contains unit tests for:
- Home route
- Signup functionality
- Login functionality

---

# Static Folder

## style.css
Contains all styling for:
- Layout
- Forms
- Buttons
- Dashboard cards
- Responsive design
- Modern UI improvements

## script.js
Contains JavaScript functionality such as:
- Password validation

## uploads/
Stores uploaded note images.

---

# Templates Folder

## base.html
Main layout template containing:
- Navigation bar
- Shared styling
- Flash messages
- Base page structure

## login.html
User login page.

## signup.html
User registration page.

## dashboard.html
Main dashboard containing navigation cards for:
- Tasks
- Blogs
- Notes

## tasks.html
Task management page where users can:
- Add tasks
- Complete tasks
- Delete tasks

## blogs.html
Displays all blog posts.

## create_blog.html
Page used to create new blog posts.

## notes.html
Displays uploaded notes with preview and download options.

## upload_note.html
Allows users to upload note images.

---

# Database Tables

## users
Stores:
- User ID
- Username
- Email
- Password

## tasks
Stores:
- Task title
- Category
- Due date
- Completion status

## blogs
Stores:
- Blog title
- Content
- Category
- Likes

## notes
Stores:
- Uploaded image filename
- Subject name

---

# Application Routes

| Route | Description |
|------|-------------|
| / | Redirects to login page |
| /signup | User registration |
| /login | User login |
| /dashboard | Main dashboard |
| /logout | Logout user |
| /tasks | Task management |
| /complete_task/<id> | Mark task complete |
| /delete_task/<id> | Delete task |
| /blogs | View blogs |
| /create_blog | Create new blog |
| /like_blog/<id> | Like a blog post |
| /upload_note | Upload note image |
| /notes | View uploaded notes |
| /download/<filename> | Download uploaded note |

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-link>
```

---

## 2. Open Project Folder

```bash
cd FinalProject
```

---

## 3. Install Flask

```bash
pip install flask
```

---

## 4. Initialize Database

```bash
python init_db.py
```

---

## 5. Run Application

```bash
python app.py
```

---

## 6. Open Browser

Visit:

```text
http://127.0.0.1:5000
```

---

# Testing

Run tests using:

```bash
pytest
```

---

# Future Improvements

Possible future upgrades include:

- Password hashing
- Blog comments
- Task editing
- Reminder notifications
- Dark mode
- User profile pictures
- Rich text editor
- Search functionality
- Cloud deployment

---

# Conclusion

The Student Learning Management App successfully demonstrates full-stack web development using Flask, SQLite, HTML, CSS, and JavaScript. The project provides students with useful academic tools while showcasing backend development, frontend design, authentication, database integration, and file upload functionality.
