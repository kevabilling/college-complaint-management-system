# College Complaint Management System

A Python Flask-based website for college students to submit complaints and for administrators to manage them.

## Features
- Student complaint submission form
- Complaint status tracking
- Admin dashboard with complaint management
- MySQL database integration
- Responsive HTML/CSS frontend

## Tech Stack
- Python 3
- Flask
- MySQL
- HTML/CSS/JavaScript

## Project Structure
- `app.py` – Flask application
- `templates/` – HTML pages
- `static/` – CSS and JavaScript assets
- `requirements.txt` – Python dependencies
- `init_db.sql` – MySQL schema

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a MySQL database and user.

3. Update database settings in `app.py`:
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'root'
   app.config['MYSQL_PASSWORD'] = 'your_password'
   app.config['MYSQL_DB'] = 'college_complaints'
   ```

4. Import the database schema:
   ```bash
   mysql -u root -p < init_db.sql
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open in browser:
   ```text
   http://localhost:5000
   ```

## Default Admin Login
- Username: `admin`
- Password: `admin123`

## Demo Student Login
- Username: `student1`
- Password: `student123`

## Notes
This project is intentionally simple and designed for learning and demonstration. You can extend it with file uploads, email notifications, admin roles, and a richer dashboard.
