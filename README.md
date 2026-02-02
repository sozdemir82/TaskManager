# TaskMaster Pro

TaskMaster Pro is a modern, user-friendly To-Do application developed using Flask and SQLAlchemy. This project implements core CRUD (Create, Read, Update, Delete) operations and follows modern web development best practices.

## Features

* Task Management: Easily add, delete, and toggle tasks between completed and pending states.
* Deadline Support: Set specific due dates for every task to stay organized.
* Instant Notifications: A built-in "Flash Messages" system to provide real-time feedback on user actions.
* Modern UI: A sleek, responsive CSS design featuring a Dark Mode theme.
* OOP Architecture: Database models are structured using Object-Oriented Programming principles.
* Secure Configuration: Sensitive database files and temporary folders are protected via .gitignore.

## Technologies Used

* Backend: Python, Flask
* Database: SQLite & Flask-SQLAlchemy (ORM)
* Frontend: HTML5, CSS3 (Flexbox & Animations), FontAwesome Icons

## Installation

1. Clone the project to your local machine:
   git clone https://github.com/your_username/your_project_name.git

2. Navigate to the project directory:
   cd your_project_name

3. Install the required libraries:
   pip install flask flask-sqlalchemy

4. Run the application:
   python app.py

5. Access the app in your browser:
   Open http://127.0.0.1:5000

## File Structure

* app.py: Main application logic and routing.
* db.sqlite: Local database file (excluded from the repository).
* templates/: Folder containing HTML templates.
* static/: Folder containing CSS files and visual assets.
* .gitignore: List of files and directories to be ignored by Git.
