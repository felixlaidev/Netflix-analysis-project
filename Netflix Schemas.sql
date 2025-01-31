-- Netflix data analysis project


create table netflix
(
	show_id	VARCHAR(6) PRIMARY KEY,
	type    VARCHAR(10),
	title	VARCHAR(150),
	director VARCHAR(208),
	casts	VARCHAR(1000),
	country	VARCHAR(150),
	date_added	VARCHAR(50),
	release_year	INT,
	rating	VARCHAR(10),
	duration	VARCHAR(15),
	listed_in	VARCHAR(100),
	description VARCHAR(250)
)

