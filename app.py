import numpy as np
from recsys_utils import *
import pandas as pd
import streamlit as st
import random


st. set_page_config(layout="wide")
st.write(""" <h1> <b style="color:red"> Movie Reccomender System</b> </h1>""",unsafe_allow_html=True)
st.write(""" <h7> <b style="color:white"> Uses Content Based Filtering</b> </h7>""",unsafe_allow_html=True)
st.write(""" <h7> <b style="color: white"> Made by Damanjit</b> </h7>""",unsafe_allow_html=True)
 
List = readCSV('./top10K-TMDB-movies.csv')
movieList = List['title']

st.session_state.options = []
st.session_state.id = []
with st.form("my_form"):
    options = []
    for i in range(3):
        option = st.selectbox(
            "Enter your Most Favorite Movies",
            movieList,
            key=f'selectbox_{i}',placeholder="",index=None
        )
        options.append(option)
    
    
    submitted = st.form_submit_button('Submit my picks')
    if submitted:
        st.session_state.options = options
        

st.write(""" <h1> <b style="color:red"> Recommendations</b> </h1>""",unsafe_allow_html=True)


if submitted:
        
    mov = findSimilar(st.session_state.options)
    columns = st.columns(5)
    m_id = List[List['title'].isin(mov)]['id']
    for i,col in zip(m_id[:5],columns):
        
        col.image(poster(i),caption = List[List['id'] == i][ 'title'].values,width=200)

    
    
    

    for i,col in zip(m_id[5:],columns):
        
        col.image(poster(i),caption = List[List['id'] == i][ 'title'].values,width=200)
