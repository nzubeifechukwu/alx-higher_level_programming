-- Creates a database hbtn_0d_usa and a table states in the database with
-- columns: id (int, unique, auto-generated, not null) and name (not null)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
