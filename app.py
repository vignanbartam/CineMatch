import streamlit as st
import pandas as pd
import pickle
import requests
import time

import os
import gdown

# Google Drive file ID from your link
file_id = "1Kh9YGkiNTDHOC6wuLm1OCasHSPd5P6fc"
url = f"https://drive.google.com/uc?id={file_id}"
output = "similarity.pkl"

# Download the file only if it's not already present
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# Load the similarity matrix
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)


def fetch_poster(movie_id):
    api_key = st.secrets["api"]["tmdb_key"]
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US')

    data= response.json()
    #st.text(data)
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie_name):
    movie_index = movies[movies['title']==movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key=lambda x:x[1])[1:6]

    recommended_movies =[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetching posters from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies =pd.DataFrame(movies_dict)


st.title('Movie Recommendation System')

select_movie_name = st.selectbox(
    'Enter your movie name', movies['title'].values
)

button_ph = st.empty()
if button_ph.button('Recommend'):
    button_ph.button("Here are the results", disabled=True)
    names,posters=recommend(select_movie_name)
    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
   

    
 