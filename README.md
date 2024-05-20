Find-Movie-Similarity-from-Plot-Summaries-by-cosine similarity

NLP and TF_IDF without sikit_learn on movie plot summeries from IMDB to quantify movie similarity

Project Description

Natural Language Processing (NLP) is an exciting field of study for data scientists where they develop algorithms that can make sense out of conversational language used by humans. In this Project, you will use NLP to find the degree of similarity between movies based on their plots available on 250 top movie IMDb.

The dataset contains the summaries of the top 250 movies on IMDb.

This project by Meysam_hyda

Requarequairment

install:
Numpy
pandas
Beautiful Soup
Request

Project structure

1.Scrap Data from IMDB
َAt first  I sent a request to IMDb by using Request library
Note: for send reqest to IMDB by request library must set a header
then by Beautiful soup and parser clean data and create Excel file
2.clean stop words
clean stop words without Scikit_learn
3.calculate TF_IDF
writing function to calculate TF_IDF
4.cosine_similarity
writing function that calculate cosine_similarity between two movie and craete Data_frame by Pandas

Use
to use this project run this code and enter the plot summury and get three movie in 250 top movie IMDB that max similarity to given plot summary

Example
after run this code on Terminal
enter plot summary of The Walking Dead
Input:Please enter the summury of the new movie : Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive.
Output : ['Kill Bill', 'The Lord of the Rings: The Return of the King', 'Inglourious Basterds']