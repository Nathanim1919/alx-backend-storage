-- Create a table users with these requirements
-- id, integer, never null, auto increment and primary key
-- email, string(255 characters), never null and unique
-- name, string(255 characters)
-- country, enumeration of countries: US, CO and TN,
-- never null (- default will be the first element of
-- the enumeration, here US)
-- if the table already exists, your script should not fail
-- your script can be executed on any database

CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US'
);
