# Tasks
### 0. we are all uniques!

Write a SQL script that creates a table `users` following these requirements:
	- With these attributes:
		- id, integer, never null, auto increment and primary key
		- email, string(255 characters), never null and unique
		- name, string(255 characters)
	- if the table already exists, your script should not fail
	- your script can be executed on any database
