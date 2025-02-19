-- Netflix Data Analysis by PostgreSQL
-- Questions and solutions of 15 business problems

-- SELECT * FROM Netflix;
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




-- 2. List the numbers of movies and TV shows are available respectively on Netflix
-- Goal: Analyze the distribution of different content types available on Netflix.


SELECT 
type, 
COUNT(*) AS typecount
FROM netflix
GROUP BY type;


-- 3.List all TV shows that have more than 5 seasons.
-- Goal: Locate TV shows that have more than 5 seasons.


SELECT title, duration
FROM netflix
WHERE type = 'TV Show' 
AND CAST(SPLIT_PART(duration, ' ', 1) AS INTEGER) > 5;



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


-- 5. Find all the titles (movies or TV shows) that do not have a director listed.
-- Goal: Retrieve content that is missing a director.


SELECT *
FROM netflix
WHERE director IS NULL OR director = '';


-- 6. Which is the Longest TV Show available on Netflix?
-- Goal: Identify the movie with the longest runtime.


select * from 
 (select distinct title as movie,
  split_part(duration,' ',1):: numeric as duration 
  from netflix
  where type ='Movie') as subquery
where duration = (select max(split_part(duration,' ',1):: numeric ) from netflix)


-- 7. Identify all movies and TV shows directed by ‘Kim Seong-hun’.
-- Goal: Retrieve all content directed by 'Kim Seong-hun'.


SELECT
*
FROM netflix
where director='Kim Seong-hun';


-- 8. Retrieve a list of all movies categorized as Action & Adventure.
-- Goal:  Get all movies belong to Action & Adventure.


SELECT
*
FROM netflix
where type='Movie' and listed_in LIKE'%Action & Adventure%';


-- 9. How many items of content exist in each genre on Netflix?   
-- Goal: Calculate the total number of content items in each genre.


SELECT 
	UNNEST(STRING_TO_ARRAY(listed_in, ',')) AS genre,
	COUNT(*) AS count
FROM netflix
GROUP BY genre;


-- 10. List all the movies released in 2002
-- Goal:Fetch all movies that were released in a particular year.


SELECT * 
FROM netflix
WHERE type='Movie' and release_year = 2002


-- 11. Find the top five countries that have contributed the most content to Netflix.
-- Goal: Determine the top 5 countries with the largest number of content items in Netflix.


SELECT 
    TRIM(UNNEST(STRING_TO_ARRAY(country, ','))) AS new_country,
    COUNT(DISTINCT show_id) AS total_contents
FROM netflix
GROUP BY new_country
ORDER BY total_contents DESC
LIMIT 5;


-- 12. Over the past five years, how many contents have been added to Netflix?
-- Goal: Fetch contents that has been added to Netflix within the past 5 years.


SELECT 
    title, 
    date_added, 
    type
FROM netflix
WHERE TO_DATE(date_added, 'Month DD, YYYY') >= CURRENT_DATE - INTERVAL '5 years'
ORDER BY date_added DESC;


-- 13. How many movies has the actor ‘Leonardo DiCaprio’ appeared in over the past 20 years?
-- Goal: calculate the number of movies featuring 'Leonardo DiCaprio' released in the past 20 years.


SELECT 
*
FROM netflix
WHERE casts LIKE '%Leonardo DiCaprio%'
AND type = 'Movie'AND release_year >= EXTRACT(YEAR FROM CURRENT_DATE) - 20;


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

