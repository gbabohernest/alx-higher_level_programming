-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
-- Description id int unique auto generated, can't be null and is primary key
-- state_id int, can't be null and must be a foreign key that reference id of the states table
-- name varchar(256) can't be null
-- if db and table already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(`state_id`) REFERENCES states(`id`)
);
