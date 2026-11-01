from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'college-complaint-system-secret-key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'college_complaints'

mysql = MySQL(app)


def get_db_connection():
    return mysql.connection


def init_db():
    cur = mysql.connection.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS college_complaints")
    cur.execute("USE college_complaints")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            role ENUM('student', 'admin') NOT NULL DEFAULT 'student',
            full_name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            title VARCHAR(255) NOT NULL,
            category VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            status ENUM('Open', 'In Progress', 'Resolved', 'Closed') NOT NULL DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES users(id)
        )
    """)
    cur.execute("SELECT COUNT(*) FROM users WHERE username='admin'")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO users (username, password, role, full_name) VALUES (%s, %s, %s, %s)", ('admin', 'admin123', 'admin', 'College Administrator'))
    cur.execute("SELECT COUNT(*) FROM users WHERE username='student1'")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO users (username, password, role, full_name) VALUES (%s, %s, %s, %s)", ('student1', 'student123', 'student', 'Riya Sharma'))
    mysql.connection.commit()
    cur.close()


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()

    if user:
        session['user_id'] = user['id']
        session['username'] = user['username']
        session['role'] = user['role']
        session['full_name'] = user['full_name']
        return redirect(url_for('dashboard'))

    flash('Invalid username or password.', 'error')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if session['role'] == 'admin':
        cur.execute("""
            SELECT c.*, u.full_name AS student_name
            FROM complaints c
            JOIN users u ON c.student_id = u.id
            ORDER BY c.created_at DESC
        """)
        complaints = cur.fetchall()
    else:
        cur.execute("SELECT * FROM complaints WHERE student_id = %s ORDER BY created_at DESC", (session['user_id'],))
        complaints = cur.fetchall()
    cur.close()

    return render_template('dashboard.html', complaints=complaints)


@app.route('/new-complaint', methods=['GET', 'POST'])
def new_complaint():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form.get('title')
        category = request.form.get('category')
        description = request.form.get('description')

        if not title or not category or not description:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('new_complaint'))

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO complaints (student_id, title, category, description, status) VALUES (%s, %s, %s, %s, %s)",
            (session['user_id'], title, category, description, 'Open')
        )
        mysql.connection.commit()
        cur.close()
        flash('Complaint submitted successfully.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('complaint_form.html')


@app.route('/update-status/<int:complaint_id>', methods=['POST'])
def update_status(complaint_id):
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('index'))

    status = request.form.get('status')
    cur = mysql.connection.cursor()
    cur.execute("UPDATE complaints SET status = %s WHERE id = %s", (status, complaint_id))
    mysql.connection.commit()
    cur.close()
    flash('Complaint status updated.', 'success')
    return redirect(url_for('dashboard'))


app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


if __name__ == '__main__':
    with app.app_context():
        try:
            init_db()
        except Exception:
            pass
    app.run(debug=True)
