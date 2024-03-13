-- creates a table and a database with a specific description
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTs states (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL
);
