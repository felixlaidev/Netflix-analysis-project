# Netflix-analysis-project


## Project Overview
This project analyzes Netflix's content catalog to uncover trends in movies and TV shows. Using SQL, we explore content distribution, ratings, release patterns, and thematic elements to derive actionable insights.

```
![alt text](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAKgAswMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAUCAwYBB//EADsQAAIBAgIDCwoGAwAAAAAAAAABAgMEBREGEjETISI0NVFxcnOxwTJBU2GBkqGy0fAUFTNSgpFC4fH/xAAaAQEAAgMBAAAAAAAAAAAAAAAAAgQBAwUG/8QANBEAAgICAAQCBwYHAQAAAAAAAAECAwQRBRIxQSFxMzRRYZHB0RMyNXKx8BUiI4Gh4fEU/9oADAMBAAIRAxEAPwD42AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAexi5NKKbb2JLMDqeAynTnDLXhKOf7otCEJz8iEpZftWY2Z5XvWvExBlKMoPKcZRfM1kZKjVaTVKo09jUGY2jKhJvSRrBs3Ct6Gp7jMXCakouElJ7E1vjaDhJdUYg2bhW9DU9xjcK3oanuMbRn7OfsZrBk4TUlFwkpPZFrfMtwrehqe4xtGFCT6I1g2bhW9DU9xmMYTk2owlJrakm8htDkkuxiDKUZQeU4yi+ZrIxMmGmvBgGcadSazhTnJc8YtnjjJS1XF62zLLfGxyvW9GIM5UqkVnKnOK53FoxSbaUU23sSGw4tPTR4DOVKpBZzpziudxaMAGmvBgAAwCbg3KdDpl8rIRNwblOh0y+VkLPuPyLWB63V+aP6ousaobvYTaXCp8Nezb8CBo3+rX6q72XrSaye+mVGDUfw9/eUf2ZJdHm+BRhP+lKJ7HLxtcSovXfafwev37iJpFx6PZLvZeWbUbGg3sVKLf9FHpDx6PZLvZdWybw6kltdFdxm30UDTw9tcRyWjV+b2Pp37kvoVd5eUKuLUK8J50oautLVe9k2Rlhl7lxeX9r6kQsV01p7izj5vFc2yMY3QUfFNeDXTzZ1lviFtc1Nzo1HKWWeWq0Z3N5QtdXd56utnlwW9nQUOA8oLqMk6SeVbfy8Cu6Yq1Q7Har4tfLhs8ppcyeu+uq9/v9phVuKVzjltUoy1o8FZ5Nb++XVzc0rWmp15asW8s8m9/wBhzGGcoW/XRe4zb1bm0jChDXkqieWaW9k+cldCKnGL6GnheVdLFvvitzb3rT66Xbqe/m9j6d+5L6EHAZKV7dyjse+v7ZX1rC6oU3Uq0XGC2vWT8Sdo5+vX6i7yUq4Qrk4vZWpzsrJz6YZEOVrb6NdU/azXpFx6HZLvZVlppDx6HZLvZVm+n0aOPxX12zzOh0d4nV7XwRVYq3HE68ovJqSafsRa6O8Tq9r4IqsW5SuOsu5Gqv08jqZ34RR5/JnQ05Qv7BN+TVhk/U/+lVgVpJXVSrUX6LcF1vP9+s26O184VLeT2cOPR5/v1ls9SjCc3lGO/KT8SvJutygu52KK68+NGZN+Mevn/p+JTaRXGbp20Xs4c/ApTbcVpXFepWltnLPo5kai9VDkgkeP4hlPKyZW9n08uwABsKYJuDcp0OmXyshE3BuU6HTL5WQs+4/ItYPrdX5o/qjo6tZU61GL2VG4+3LPwCoqN1Ksv84KL9j/ANlfpBOVOlbzh5Uaua6Uizo1I1qUKkfJnFNHNcdQUl3Pf13RsyZ0y6x01/dfv4nP6Q8ej2S72XdpLVsKMnsVKL+BSaQ8ej2S72XVsm8OpJbXRWX9G630UDlcP3/EcnRC/Prf0Vb4fU58nRwi+e9uKXTNfUj3VtUtaip1klJrPeeZZrVcXqDOBn2598YzyYNJe7XX/hLwHlBdRknSTyrb+XgRsB5QXUZJ0k8q2/l4GuXrC/ftL1P4HZ+b5xK/DOULfro6O/u42VFVZQck5auS9v0OcwzlC366LjSHiMO1XcyN8VK2KZt4RbOnh11kOqfyRDv8Wp3VrOjGlOLk1vtrzMy0c/Xr9Rd5Tlxo5+vX6i7zZZCMKmkU8DLtyuJVTte30/wzXpDx6HZLvZVnQYth1e7uY1KLhkoKOUnk9r+pV3OGXNtSlVqxhqR2tSFNkeRLfiR4rhZH/pst5Hy73vXYtdHeJ1e18EVWLcpV+su5Fro7xOr2vgiqxblK46y7kRr9PIs5/wCEUefyZtwKnOd+pxeUacW5evPey++YusVhOph9aNN7+WfSltRqwS33CyUpLKdXhPo8336yTaXVO7hOVPZGbi/X9o0Wzbs5l2Ovw3FjXgqib1KxN/FfJaOQBvvqH4a7qUvMnwejzGg6Ce1tHiLISrm4S6rwAAMkATcG5Tofy+VkI9Ta2PIjJc0WjbRb9lbCzW+Vp/Bl7pG1uFFZrPX2ew8wfEKNKz3O4qqDhJ6ufnT+2UQNX2C5ORs6b4xYsx5UI6bWtdfoTsZuKVzdxnQlrRVNRzya382T6GNW9K3pU3TquUIJPJLLNLpKIEnTFxUX2NNfFMiu6d0NJy6+Beyx+n/jbzfTJIrMQu/xtdVdz1MoqOWefP8AUigQphB7SI5PFMrKhyWy2vJfQkWV1K0r7rCKk8msmZ399UvnDdIRjqZ5avr/AOEQE+SPNzdyssq5UuhS/lfY2UKsqFaFWCTlB5rPYSbzEq95SVOrGmoqWtwU8+8hAOMW9sxDIthW64y1F9UCVYXs7Kc5QhGWssnmyKDMoqS0yNVs6Zqyt6aLlY/Pz20ff/0ar3F/xdrOi6GprZcLXz2PPmKsGtUVp7SL0+L5s4OEp7TWn4L6FphWJUrKjOnUhOWtPWzjlzIi3FWjc4hKrPWjRnNOWa38vYRQSVcVJyXVmmedbOmFMtOMXtHQ3uK27s6kbapnUa1UtVrL1kHAbhUbqVKTyhUXn519srAQVEVBxXcs2cXvsyYZEtbj2XT3+3qXmkNDONK5jv5cCTXw8SjPdiyWw8J1w5I8uyrnZMcq92qPLvtvf0AAJlQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//9k=)


```

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
