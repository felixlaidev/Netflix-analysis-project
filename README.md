# Netflix-analysis-project


## Project Overview
This project analyzes Netflix's content catalog to uncover trends in movies and TV shows. Using SQL, we explore content distribution, ratings, release patterns, and thematic elements to derive actionable insights.

## Objectives
- Compare movie vs. TV show quantities
- Identify dominant content ratings
- Analyze geographical content distribution
- Investigate production trends over time
- Categorize content based on descriptions

# Dataset
This project using the dataset from kaggle https://www.kaggle.com/datasets/shivamb/netflix-shows. This dataset contains 8807 rows of the infomation of netflix movies and tv shows. Each row has details like showid,duration,directors,rating etc.


## Schema Design
```sql
CREATE TABLE netflix (
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
);
