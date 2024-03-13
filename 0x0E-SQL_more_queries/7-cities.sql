-- creates a table and a database with a specific description
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTs cities (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        FOREIGN KEY (state_id) REFERNCES states(id)
);
