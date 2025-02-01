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

# --------------------------------------------
# DATA CLEANING
# --------------------------------------------
# Calculate the null rate for each column
null_rates = (df.isna().sum() / df.shape[0]) * 100

# Missing data
# Filter and display only columns with null rates > 0%
print("Null rate")
null_rates_filtered = null_rates[null_rates > 0]
print(null_rates_filtered)

# Handling missing values:
# Fill missing values in 'director' and 'cast' columns with 'Unknown'
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)

# Fill missing values in 'country' with 'Not Specified'
df['country'].fillna('Not Specified', inplace=True)
# Fill missing values in 'rating' with 'Unrated'
df['rating'].fillna('Unrated', inplace=True)
# Fill missing values in 'date_added' with the most frequent date
df['date_added'].fillna(df['date_added'].mode()[0], inplace=True)
# Fill missing values in 'rating' with 'Unrated'
df['rating'].fillna('Unrated', inplace=True)

# Drop rows where 'duration' is missing (assuming they are not useful)
df.dropna(subset=['duration'], inplace=True)

# Removing duplicate records (if any)
df.drop_duplicates(inplace=True)

# --------------------------------------------
# DATA TRANSFORMING
# --------------------------------------------
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

# --------------------------------------------
# DATA ANALYSIS AND VISUALIZATION
# --------------------------------------------

# --------------------------------------------
# PERCENTAGE & COUNTS OF MOVIES vs TV SHOWS
# --------------------------------------------

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




# --------------------------------------------
# TOP 10 COUNTRIES OF COUNTS OF MOVIES vs TV SHOWS 
# --------------------------------------------
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




# --------------------------------------------
# MONTHLY ANALYSIS & VISUALIZATION
# --------------------------------------------
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
