-- Creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS
hbtn_0d_usa.cities(id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
state_id int NOT NULL,
name varchar(256),
FOREIGN KEY(state_id) REFERENCES states(id));
