-- A script that creates the MySQL server user user_0d_1.
-- Grant all privileges on  your MYSQL server
-- user pwd user_01_1, if user already exists, script won't fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
