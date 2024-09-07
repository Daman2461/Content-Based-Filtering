import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st
import numpy as np
import requests


def readCSV(file):
    return pd.read_csv(file)

def findSimilar(movies3):
     
     
    similar = []
    a = pd.DataFrame((cosine_sim[indices[movies3[0]]]+cosine_sim[indices[movies3[1]]]+cosine_sim[indices[movies3[2]]])/3, columns=["score"])
    
    a= a.sort_values("score", ascending=False)[0:5]
    
    movie_indices = [indices[movies3[0]], indices[movies3[1]], indices[movies3[2]]]

    x=  pd.DataFrame(cosine_sim[indices[movies3[0]]], columns=["score"])
    x=x.sort_values("score", ascending=False)[0:5]

    for i in range(1,len(movie_indices)):
        b=  pd.DataFrame(cosine_sim[indices[movies3[i]]], columns=["score"])

        b= b.sort_values("score", ascending=False)[0:5]

        x=pd.concat([b,x])

    
    

    
    x = x.drop(movie_indices)
    similar = x.sort_values("score", ascending=False)[1:11].index
    return (movies['title'].iloc[similar])
   


def poster(moveid):
   url='https://api.themoviedb.org/3/movie/{}?api_key=f2f4840944d9cc178e9f22d1979eb440'.format(moveid)
   data = requests.get(url)
   json =data.json()

   pic_path = json['poster_path']

   full_path = "https://image.tmdb.org/t/p/w500/" + pic_path
   return full_path




movies = pd.read_csv("./top10K-TMDB-movies.csv") 


movies.dropna(inplace=True)
 
movies.isnull().sum()
movies.reset_index(drop=True, inplace=True)

movies['combined_text'] = movies['title']+" "+movies['overview']

tfidf = TfidfVectorizer(stop_words='english')  # Initialize TF-IDF Vectorizer
tfidf_matrix = tfidf.fit_transform(movies['combined_text'])  

 
tfidf_matrix.toarray()


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title'])
indices = indices[~indices.index.duplicated(keep='last')]

 

