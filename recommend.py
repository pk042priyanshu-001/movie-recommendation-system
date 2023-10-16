import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import Entry, Label, Button, Text

# Load movie data from a CSV file
movies = pd.read_csv("movies.csv")

# Define a function to clean movie titles by removing non-alphanumeric characters
def clean_title(title):
    return re.sub(r"[^a-zA-Z0-9 ]", "", title)

# Apply the title cleaning function to create a new column 'clean_title'
movies["clean_title"] = movies.title.apply(clean_title)

# Initialize a TF-IDF vectorizer with a range of 1 to 2 n-grams
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(movies.clean_title)

# Define a function to find similar movies based on user input
def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indx = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indx][::-1]
    return results

# Load movie ratings data from a CSV file
ratings = pd.read_csv("ratings.csv")

# Define a function to find and recommend similar movies
def find_similar_movies(movie_id):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > 0.10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[[ "title", "genres"]]

# Create a function to handle the movie recommendation process
def recommend_movies():
    user_input = entry.get()
    results = search(user_input)
    if not results.empty:
        movie_id = results.iloc[0]["movieId"]
        recommended_movies = find_similar_movies(movie_id)
        result_text.config(state='normal')
        result_text.delete('1.0', 'end')
        result_text.insert('1.0', recommended_movies.to_string(index=False))
        result_text.config(state='disabled')
    else:
        messagebox.showinfo("Movie Recommendations", "No recommendations found for the input.")

# Create a Tkinter window
window = tk.Tk()
window.title("Movie Recommendation App")

# Create and place the input label and entry widget
input_label = Label(window, text="Enter the title of the movie:")
input_label.pack()

entry = Entry(window, width=100)
entry.pack()

# Create and place the "Recommend" button
recommend_button = Button(window, text="Recommend", command=recommend_movies)
recommend_button.pack()

# Create a Text widget to display recommendations
result_text = Text(window, width=200, height=300)
result_text.config(state='disabled')
result_text.pack()

# Start the Tkinter main loop
window.mainloop()
