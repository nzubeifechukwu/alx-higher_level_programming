-- Create a table unique_id with columns
-- id (default value 1, unique) and name
CREATE TABLE IF NOT EXISTS unique_id
    (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
