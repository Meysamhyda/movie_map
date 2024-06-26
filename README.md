# Find Movie Similarity from Plot Summaries by Cosine Similarity
NLP and TF_IDF without scikit-learn on movie plot summaries from IMDb to quantify movie similarity

## Project Description
Natural Language Processing (NLP) is an exciting field of study for data scientists where they develop algorithms that can make sense out of conversational language used by humans. In this project, you will use NLP to find the degree of similarity between movies based on their plots available on the top 250 movies on IMDb.

The dataset contains the summaries of the top 250 movies on IMDb.

This project is developed by Meysam_hyda.

## Requirements
Install the following libraries:

Numpy
pandas
Beautiful Soup
Requests
## Project Structure
### Scrap Data from IMDb

First, a request is sent to IMDb using the Requests library.
Note: To send a request to IMDb using the Requests library, a header must be set.
Then, using Beautiful Soup and a parser, the data is cleaned and an Excel file is created.
### Clean Stop Words

Clean stop words without using Scikit-learn.
### Calculate TF-IDF

Write a function to calculate TF-IDF.
### Cosine Similarity

Write a function that calculates cosine similarity between two movies and create a DataFrame using pandas.
##Usage
To use this project, run the code and enter a plot summary. The program will return three movies from the top 250 IMDb movies that have the maximum similarity to the given plot summary.

Example:

After running the code in the terminal:

Input:


Please enter the summary of the new movie: Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive.
Output:


['Kill Bill', 'The Lord of the Rings: The Return of the King', 'Inglourious Basterds']
