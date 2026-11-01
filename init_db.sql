CREATE DATABASE IF NOT EXISTS college_complaints;
USE college_complaints;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('student', 'admin') NOT NULL DEFAULT 'student',
    full_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

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
);

INSERT INTO users (username, password, role, full_name)
VALUES
('admin', 'admin123', 'admin', 'College Administrator'),
('student1', 'student123', 'student', 'Riya Sharma');

INSERT INTO complaints (student_id, title, category, description, status)
VALUES
(2, 'Library AC not working', 'Infrastructure', 'The air conditioner in the library is not cooling and students are facing discomfort during evening study.', 'Open'),
(2, 'Wi-Fi connectivity issue', 'IT Support', 'Internet connection is very slow in the second floor lab and interrupts online class access.', 'In Progress');
