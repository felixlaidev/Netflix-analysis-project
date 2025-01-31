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
```
##  Business question
```sql
/*
Question 1:
1. Classify Netflix content into two groups: those with descriptions containing either 'kill' or 'violence' (labeled 'Bad') and those without these keywords (labeled 'Good'). Provide the total number of titles in each category.
*/

WITH categorized_content AS (
    SELECT 
        CASE 
            WHEN LOWER(description) LIKE '%kill%' OR LOWER(description) LIKE '%violence%' 
            THEN 'Bad' 
            ELSE 'Good' 
        END AS content_category
    FROM netflix
    WHERE description IS NOT NULL
)

SELECT 
    content_category,
    COUNT(*) AS number_of_titles
FROM categorized_content
GROUP BY content_category
ORDER BY number_of_titles DESC;

```

```sql
-- 2. List the numbers of movies and TV shows are available respectively on Netflix
-- Goal: Analyze the distribution of different content types available on Netflix.


SELECT 
type, 
COUNT(*) AS typecount
FROM netflix
GROUP BY type;

```

```sql
-- 3.List all TV shows that have more than 5 seasons.
-- Goal: Locate TV shows that have more than 5 seasons.


SELECT title, duration
FROM netflix
WHERE type = 'TV Show' 
AND CAST(SPLIT_PART(duration, ' ', 1) AS INTEGER) > 5;

```

```sql
-- 4. Identify the most common rating assigned to movies and TV shows.
-- Goal: Determine the most common rating for each content type.


WITH RankedRatings AS (
    SELECT type, rating, COUNT(*) AS count,
           RANK() OVER (PARTITION BY type ORDER BY COUNT(*) DESC) AS rank
    FROM netflix
    GROUP BY type, rating
)
SELECT type, rating, count
FROM RankedRatings
WHERE rank = 1;
```
```sql
-- 5. Find all the titles (movies or TV shows) that do not have a director listed.
-- Goal: Retrieve content that is missing a director.


SELECT *
FROM netflix
WHERE director IS NULL OR director = '';
```
```sql
-- 6. Which is the Longest TV Show available on Netflix?
-- Goal: Identify the movie with the longest runtime.


select * from 
 (select distinct title as movie,
  split_part(duration,' ',1):: numeric as duration 
  from netflix
  where type ='Movie') as subquery
where duration = (select max(split_part(duration,' ',1):: numeric ) from netflix)
```

```sql
-- 7. Identify all movies and TV shows directed by ‘Kim Seong-hun’.
-- Goal: Retrieve all content directed by 'Kim Seong-hun'.


SELECT
*
FROM netflix
where director='Kim Seong-hun';
```
```sql
-- 8. Retrieve a list of all movies categorized as Action & Adventure.
-- Goal:  Get all movies belong to Action & Adventure.


SELECT
*
FROM netflix
where type='Movie' and listed_in LIKE'%Action & Adventure%';
```
```sql


-- 9. How many items of content exist in each genre on Netflix?   
-- Goal: Calculate the total number of content items in each genre.


SELECT 
	UNNEST(STRING_TO_ARRAY(listed_in, ',')) AS genre,
	COUNT(*) AS count
FROM netflix
GROUP BY genre;
```
```sql

-- 10. List all the movies released in 2002
-- Goal:Fetch all movies that were released in a particular year.


SELECT * 
FROM netflix
WHERE type='Movie' and release_year = 2002
```
```sql
-- 11. Find the top five countries that have contributed the most content to Netflix.
-- Goal: Determine the top 5 countries with the largest number of content items in Netflix.


SELECT 
    TRIM(UNNEST(STRING_TO_ARRAY(country, ','))) AS new_country,
    COUNT(DISTINCT show_id) AS total_contents
FROM netflix
GROUP BY new_country
ORDER BY total_contents DESC
LIMIT 5;
```
```sql

-- 12. Over the past five years, how many contents have been added to Netflix?
-- Goal: Fetch contents that has been added to Netflix within the past 5 years.


SELECT 
    title, 
    date_added, 
    type
FROM netflix
WHERE TO_DATE(date_added, 'Month DD, YYYY') >= CURRENT_DATE - INTERVAL '5 years'
ORDER BY date_added DESC;
```

```sql
-- 13. How many movies has the actor ‘Leonardo DiCaprio’ appeared in over the past 20 years?
-- Goal: calculate the number of movies featuring 'Leonardo DiCaprio' released in the past 20 years.


SELECT 
*
FROM netflix
WHERE casts LIKE '%Leonardo DiCaprio%'
AND type = 'Movie'AND release_year >= EXTRACT(YEAR FROM CURRENT_DATE) - 20;

```
```sql
-- 14.Find the top 10 actors who have appeared in the most movies produced in United States.
-- Goal: determine the top 10 actors with the highest number of appearances in movies produced in the United States.


SELECT 
    UNNEST(STRING_TO_ARRAY(casts, ',')) AS actor,
    COUNT(*) AS movie_count
FROM netflix
WHERE country='United States'
GROUP BY actor
ORDER BY movie_count DESC
LIMIT 10;
```
```sql
-- 15. Determine the average number of content releases in United States per year. Return the top five years with the highest average content releases.
-- Goal: calculate and rank the years based on the average number of content releases from the United States.


SELECT 
    release_year,
    COUNT(*) AS total_release,
    ROUND(
        COUNT(show_id)::numeric /
        (SELECT COUNT(show_id) FROM netflix WHERE country = 'United States')::numeric * 100, 2
    ) AS avg_release
FROM netflix
WHERE country ='United States'
GROUP BY release_year
ORDER BY avg_release DESC
LIMIT 5;
```
## Conclusion

1.Netflix has a diverse catalog dominated by movies rather than TV shows.

2.The United States remains the largest contributor to Netflix’s library.

3.The common rating of TV shows and movies are TV-MA
