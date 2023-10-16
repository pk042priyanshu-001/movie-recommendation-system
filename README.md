# Movie Recommendation Project Report

## Author: Priyanshu Katiyar

## Introduction

The Movie Recommendation Project, created by Priyanshu Katiyar, is a fun and educational project developed while learning data science and analysis. The project aims to recommend movies to users based on the input of a movie title. This report provides an overview of the project, the tools and libraries used, and a brief explanation of the project's functionality.

## Project Overview

The Movie Recommendation Project is designed to assist users in discovering movies that are similar to a movie they specify. It employs a combination of natural language processing and collaborative filtering to provide movie recommendations. The project comprises several key components, including data preprocessing, text analysis, recommendation calculation, and a user-friendly graphical user interface (GUI) using the Tkinter library.

## Tools and Libraries Used

The project leverages several tools and libraries to accomplish its objectives:

1. **Python**: The core programming language used for development.
2. **Pandas**: A powerful data manipulation and analysis library utilized to load and process movie data from CSV files.
3. **scikit-learn (Sklearn)**: Sklearn provides the necessary modules for text analysis, including the TF-IDF vectorizer and cosine similarity calculations.
4. **NumPy**: NumPy is used for efficient numerical operations and array manipulations.
5. **re (Regular Expressions)**: The re library assists in cleaning movie titles by removing non-alphanumeric characters.
6. **Tkinter**: Tkinter is used for creating a user-friendly GUI, which allows users to interact with the application.

## Functionality

The project can be broken down into the following main components:

### 1. Data Preprocessing

The project begins by loading movie data from CSV files using the Pandas library. Movie titles are preprocessed to remove non-alphanumeric characters, creating a new column called 'clean_title'. This step ensures that the movie titles are consistent and suitable for analysis.

### 2. Text Analysis

A TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer is employed to convert movie titles into numerical vectors. These vectors represent the textual content of each movie title, allowing for cosine similarity calculations. The Sklearn library plays a crucial role in this process.

### 3. Movie Search

The user is prompted to input a movie title using the Tkinter GUI. Upon receiving user input, the system searches for movies similar to the provided title. The search function calculates the cosine similarity between the user's input and all movie titles in the dataset, ranking them based on similarity.

### 4. Movie Recommendation

Once the most similar movie is identified, the system employs collaborative filtering to recommend movies based on user ratings. Similar users are identified who have rated the selected movie highly (rating > 4), and movies that these users have positively rated are considered as recommendations. Recommendations are further filtered to ensure a minimum relative frequency of 0.10 among similar users. A final list of recommended movies is generated and presented to the user in the GUI.

## Conclusion

The Movie Recommendation Project, developed by Priyanshu Katiyar, demonstrates the application of data science and analysis techniques to provide users with movie recommendations. This project showcases the use of Python, Pandas, Sklearn, NumPy, regular expressions, and Tkinter to build a functional and user-friendly movie recommendation system. It serves as an excellent example of a practical application of data analysis and GUI development, and can be a starting point for more advanced recommendation systems.
