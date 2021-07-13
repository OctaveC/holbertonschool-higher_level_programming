-- Creates the tables hbtn_0d_usa and states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS
states(id int PRIMARY KEY AUTO_INCREMENT UNIQUE, name varchar(256) NOT NULL);
