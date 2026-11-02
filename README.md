# College Complaint Management System

A Python Flask-based website for college students to submit complaints and for administrators to manage them.

## Features
- Student complaint submission form
- Complaint status tracking page for students
- Thank-you confirmation after complaint submission
- Admin dashboard with complaint management
- MySQL database integration
- Responsive HTML/CSS frontend

## Tech Stack
- Python 3
- Flask
- MySQL
- HTML/CSS

## Project Structure
- `app.py` – Flask application
- `templates/` – HTML pages
- `static/` – CSS assets
- `requirements.txt` – Python dependencies
- `init_db.sql` – MySQL schema

## Local Setup

### 1. Clone or open the project
```bash
git clone https://github.com/kevabilling/college-complaint-management-system.git
cd college-complaint-management-system
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and start MySQL locally
Make sure MySQL is installed and running on your computer.

Then create a database and set the login credentials in your environment or update them in `app.py`.

Example:
```bash
export MYSQL_HOST=localhost
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DB=college_complaints
```

On Windows PowerShell:
```powershell
$env:MYSQL_HOST = "localhost"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "your_password"
$env:MYSQL_DB = "college_complaints"
```

### 5. Initialize the database
You can either let the app create the tables automatically on first run, or import the schema manually:

```bash
mysql -u root -p < init_db.sql
```

### 6. Run the application
```bash
python app.py
```

The app runs at:
```text
http://localhost:5000
```

## Default Login Credentials
### Admin
- Username: `admin`
- Password: `admin123`

### Student
- Username: `student1`
- Password: `student123`

## Notes
- The app is intentionally simple and designed for learning and demo purposes.
- If MySQL uses a different password, update the environment variables before running the app.
- To stop the app, press `Ctrl + C` in the terminal.
