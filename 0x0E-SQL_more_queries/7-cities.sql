-- Create a database hbtn_0d_usa and a table cities in the database with
-- columns id (int, autogen, not null, prim key), name (varchar, not null) and
-- state_id (int, not null, foreign key referencing id of states table)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
