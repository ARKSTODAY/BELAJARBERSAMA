import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Netflix data
netflix_df = pd.read_csv("netflix_data.csv")

# Filter only movies
netflix_movies = netflix_df[netflix_df["type"] == "Movie"]

# Select relevant columns
netflix_movies = netflix_movies[["title", "country", "genre", "release_year", "duration"]]

# Filter short movies (<60 min)
short_movies = netflix_movies[netflix_movies['duration'] < 60].copy()  # Copy the DataFrame to avoid the warning

# Define genre_category based on genre
short_movies.loc[:, 'genre_category'] = short_movies['genre'].apply(lambda x: x if x in ['Children', 
                                                                                         'Documentaries', 
                                                                                         'Stand-Up'] 
                                                                                         else 
                                                                                         'Others')

# Assign colors based on genre_category
colors = sns.color_palette("husl", 4)  # Use a palette with 4 colors
# Ensure the palette has enough colors for the number of unique genre_category
palette = {category: colors[i] for i, category in enumerate(short_movies['genre_category'].unique())}

# Set Seaborn style
sns.set(style="whitegrid")

# Create scatter plot with Seaborn
plt.figure(figsize=(12, 8))
sns.scatterplot(data=short_movies, x="release_year", y="duration", hue="genre_category", palette=palette, s=100)
plt.title("Movie Duration <60 min by Year of Release and Genre Category")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.legend(title='Genre Category')
plt.show()