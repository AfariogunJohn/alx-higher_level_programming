-- creates a table with a specific description
CREATE TABLE IF NOT EXISTS id unique_id (
        id INT DEFAULT 1 UNIQUE,
        name VARCHAR(256) NOT NULL
);
