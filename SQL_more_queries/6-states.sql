-- Create the database hbtn_0d_usa if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique, auto-generated, not null, and primary key
    name VARCHAR(256) NOT NULL         -- Name field, cannot be null
);
