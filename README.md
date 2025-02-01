# Netflix-analysis-project


## Project Overview
This project analyzes Netflix's content catalog to uncover trends in movies and TV shows. Using SQL and Python, we explore content distribution, ratings, release patterns, and thematic elements to derive actionable insights. 

![Image](https://github.com/user-attachments/assets/7e30f620-171c-4d58-8416-8626e2ac7b96)

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
## Python project
## IMPORT LIBRARY AND FILE READING
```py
import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AffinityPropagation
warnings.filterwarnings("ignore")
import plotly as py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import datetime as dt
import missingno as msno
import os
import matplotlib.lines as lines
py.offline.init_notebook_mode(connected = True)
#print(os.listdir("../input"))

plt.rcParams['figure.dpi'] = 140
# Load the CSV file
file_path = "/Users/felixlai/Desktop/Work/Data analyst Project/netflix_project/Netflix-analysis-project/netflix_titles.csv"
df = pd.read_csv(file_path)

# Display initial dataset information
print("Initial Dataset Info:")
print(df.info())
```
## DATA CLEANING

```py
from project_name import BaseClass
from project_name import base_function

BaseClass().base_method()
base_function()
```

```py
# Calculate the null rate for each column
null_rates = (df.isna().sum() / df.shape[0]) * 100
```

```py
# Missing data
# Filter and display only columns with null rates > 0%
print("Null rate")
null_rates_filtered = null_rates[null_rates > 0]
print(null_rates_filtered)
```

```py
# Handling missing values:
# Fill missing values in 'director' and 'cast' columns with 'Unknown'
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
```

```py
# Fill missing values in 'country' with 'Not Specified'
df['country'].fillna('Not Specified', inplace=True)
# Fill missing values in 'rating' with 'Unrated'
df['rating'].fillna('Unrated', inplace=True)
# Fill missing values in 'date_added' with the most frequent date
df['date_added'].fillna(df['date_added'].mode()[0], inplace=True)
# Fill missing values in 'rating' with 'Unrated'
df['rating'].fillna('Unrated', inplace=True)
```

```py
# Drop rows where 'duration' is missing (assuming they are not useful)
df.dropna(subset=['duration'], inplace=True)

# Removing duplicate records (if any)
df.drop_duplicates(inplace=True)
```

# --------------------------------------------
# DATA TRANSFORMING
# --------------------------------------------
```py
# Convert 'date_added' to datetime format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Format 'date_added' to YYYY-MM-DD
df['date_added'] = df['date_added'].dt.strftime('%Y-%m-%d')

# Display the updated column
print(df[['date_added']].head())

# Creating a binary column: 1 for Movies, 0 for TV Shows
df['is_movie'] = np.where(df['type'] == 'Movie', 1, 0)

# Mapping 'rating' categories to numeric codes for easier analysis
rating_mapping = {
    'TV-MA': 1, 'R': 2, 'PG-13': 3, 'TV-14': 4, 'PG': 5,
    'TV-PG': 6, 'G': 7, 'TV-G': 8, 'NC-17': 9, 'TV-Y': 10,
    'TV-Y7': 11, 'TV-Y7-FV': 12, 'Unrated': 13
}
df['rating_code'] = df['rating'].map(rating_mapping)
```
# --------------------------------------------
# DATA ANALYSIS AND VISUALIZATION
# --------------------------------------------

# --------------------------------------------
# PERCENTAGE & COUNTS OF MOVIES vs TV SHOWS
# --------------------------------------------
```py
# Get the 'type' column as a NumPy array
types_array = df['type'].values

# Calculate unique values and their counts using NumPy
unique_types, type_counts = np.unique(types_array, return_counts=True)

# Calculate percentages
total = type_counts.sum()
percentages = (type_counts / total) * 100

# Print formatted distribution statistics
print("\nContent Type Distribution:")
for media_type, quantity, proportion in zip(unique_types, type_counts, percentages):
    print(f"- {media_type}: {proportion:.1f}% ({quantity} entries)")

# Calculate proportional distribution for visualization
content_counts = df.groupby('type').size()
total_entries = len(df)
content_ratios = (content_counts / total_entries).round(2)

# Prepare ratio data for plotting
content_ratios_df = pd.DataFrame(content_ratios).T

# Initialize visualization canvas
plot_figure, plot_axis = plt.subplots(1, 1, figsize=(6.5, 2.5))

# Create stacked horizontal bars
plot_axis.barh(content_ratios_df.index, content_ratios_df['Movie'], 
             color='#b20710', alpha=0.9, label='Cinema')
plot_axis.barh(content_ratios_df.index, content_ratios_df['TV Show'], 
             left=content_ratios_df['Movie'], color='#1f77b4', 
             alpha=0.9, label='Series')

# Configure axis parameters
plot_axis.set_xlim(0, 1)
plot_axis.set_xticks([])
plot_axis.set_yticks([])

# Annotate movie percentages
for idx in content_ratios_df.index:
    # Movie percentage label
    plot_axis.annotate(
        f"{int(content_ratios_df['Movie'][idx]*100)}%", 
        xy=(content_ratios_df['Movie'][idx]/2, idx),
        va='center', ha='center', color='white',
        fontsize=40, fontfamily='serif', fontweight='light'
    )
    # Movie category label
    plot_axis.annotate(
        "Movie", 
        xy=(content_ratios_df['Movie'][idx]/2, -0.25),
        va='center', ha='center', color='white',
        fontsize=15, fontfamily='serif', fontweight='light'
    )

# Annotate TV show percentages    
for idx in content_ratios_df.index:
    # TV Show percentage label
    plot_axis.annotate(
        f"{int(content_ratios_df['TV Show'][idx]*100)}%", 
        xy=(content_ratios_df['Movie'][idx] + content_ratios_df['TV Show'][idx]/2, idx),
        va='center', ha='center', color='white',
        fontsize=40, fontfamily='serif', fontweight='light'
    )
    # TV Show category label
    plot_axis.annotate(
        "TV Show", 
        xy=(content_ratios_df['Movie'][idx] + content_ratios_df['TV Show'][idx]/2, -0.25),
        va='center', ha='center', color='white',
        fontsize=15, fontfamily='serif', fontweight='light'
    )

# Add titles and descriptions
plot_figure.text(0.125, 1.03, 'Content Type Distribution', 
               fontfamily='serif', fontsize=15, fontweight='bold')
plot_figure.text(0.125, 0.92, 'Movies dominate Netflix\'s content library', 
               fontfamily='serif', fontsize=12)

# Remove chart borders
for spine in ['top', 'left', 'right', 'bottom']:
    plot_axis.spines[spine].set_visible(False)

# Hide residual legend elements
plot_axis.legend().set_visible(False)
plt.show()
```

<img width="766" alt="Image" src="https://github.com/user-attachments/assets/a498e139-b597-4896-820b-9487b5615176" />

# --------------------------------------------
# TOP 10 COUNTRIES OF COUNTS OF MOVIES vs TV SHOWS 
# --------------------------------------------
```py
df['first_country'] = df['country'].str.split(',').str[0].str.strip()
df['first_country'].replace({
    'United States': 'USA',
    'United Kingdom': 'UK',
    'South Korea': 'S. Korea'
}, inplace=True)

# FILTER OUT NULL VALUES (Not Specified)
country_counts = df[df['first_country'] != 'Not Specified']['first_country'].value_counts().head(10)

# Visualization setup
plt.figure(figsize=(12, 6))
color_palette = ['#b20710' if i < 3 else '#f5f5f1' for i in range(10)]

# Create bar plot
bars = plt.bar(country_counts.index, country_counts.values,
               color=color_palette, edgecolor='darkgray', linewidth=0.6)

# Add value labels
for bar, value in zip(bars, country_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, value + 50, str(value),
             ha='center', va='bottom', fontfamily='serif', fontsize=10)

# Style adjustments
plt.gca().spines[['top', 'right', 'left']].set_visible(False)
plt.axhline(0, color='black', linewidth=1.3, alpha=0.7)

# Grid and ticks
plt.yticks(np.arange(0, 4000, 500), fontfamily='serif')
plt.grid(axis='y', alpha=0.4)
plt.xticks(fontfamily='serif', rotation=0)

# Titles
plt.title('Top 10 Countries on Netflix\n', 
          fontsize=18, fontfamily='serif', fontweight='bold', x=0.12, ha='left')
plt.text(0.12, 0.92, 'The three most frequent countries have been highlighted', 
         fontfamily='serif', fontsize=12, transform=plt.gcf().transFigure)

plt.tight_layout()
plt.show()

```
<img width="1453" alt="Image" src="https://github.com/user-attachments/assets/bd97e589-a503-4db7-824d-a444ddbd7a64" />

# --------------------------------------------
# MONTHLY ANALYSIS & VISUALIZATION
# --------------------------------------------
```py
# Convert date_added back to datetime (if needed)
df['date_added'] = pd.to_datetime(df['date_added'])

# Extract month names and count entries
df['month_added'] = df['date_added'].dt.month_name()
monthly_counts = df['month_added'].value_counts()

# Ensure all 12 months are present (fill missing months with 0)
all_months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
monthly_counts = monthly_counts.reindex(all_months, fill_value=0)

# Identify top 2 months with the highest content added
top2_months = monthly_counts.nlargest(2).index.tolist()

# Create custom colors (highlight top 2 months)
colors = ['#ff9999' if month in top2_months else '#66b3ff' 
          for month in monthly_counts.index]

# Explode the highlighted months
explode = [0.1 if month in top2_months else 0 
           for month in monthly_counts.index]

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(monthly_counts, 
        labels=monthly_counts.index,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1})

# Draw circle to make it a donut chart (optional)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures pie is drawn as circle
plt.title('Distribution of Netflix contents Added by Month', fontsize=16, pad=20)
plt.axis('equal')

# Add legend with month names and counts
plt.legend(monthly_counts.index, 
           title="Months",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()
```
<img width="1275" alt="Image" src="https://github.com/user-attachments/assets/77903f6c-e807-482c-850e-09acfa006ea6" />

# Tableau for data visualization 

![Image](https://github.com/user-attachments/assets/dc568722-52b3-42b5-be68-cda94c0119c5)
### **Netflix Dashboard Summary**
- **Dynamic Feature**: Allows users to select a specific movie and view detailed information.  

#### **Key Metrics & Visualizations:**
1. **Movie Information Section**:
   - Displays **Type, Title, Rating, Date Added, Duration, Release Year, Genre, and Description** of the selected movie.
   
2. **Top 10 Genres**:
   - Shows a **bar chart** of the most common genres, with **"Dramas, International Movies"** as the top genre (362 occurrences).

3. **Ratings Distribution**:
   - A **bar chart** depicting the number of titles under each rating category.
   - **TV-MA** is the most frequent rating with **3,207 titles**, followed by **TV-14** (2,160).

4. **Total Movies & TV Shows by Country**:
   - A **choropleth map** illustrating the distribution of Netflix content across different countries.
   - Darker shades represent higher numbers of content.

5. **Movies & TV Shows Distribution**:
   - A **bubble chart** showing the proportion of **Movies (6,131; 69.62%)** and **TV Shows (2,676; 30.38%)** in the dataset.

This dashboard effectively visualizes Netflix's content distribution and enables dynamic exploration of individual movies.

## Conclusion

1.Netflix has a diverse catalog dominated by movies rather than TV shows.

2.The United States remains the largest contributor to Netflix’s library.

3.The common rating of TV shows and movies are TV-MA

4.Netflix prioritizes movie content over series, likely due to production cost and licensing agreements.

5.The distribution highlights Netflix's strong reliance on American and Indian content, reflecting global market demand and production capabilities.

6.The months of July (9.4%) and December (9.1%) have the highest percentage of content additions, indicating Netflix may strategically release more content during summertime and Christmas, knowing that people have more free time due to holidays, making it an ideal opportunity to attract and engage viewers.

7.
