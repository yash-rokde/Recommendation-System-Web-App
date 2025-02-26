

import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender System Using Machine Learning')
st.subheader('Upload the dataset')
import streamlit as st
import os
# File Processing Pkgs
import pandas as pd
from PIL import Image 


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

def save_uploaded_file(uploadedfile):
	with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
		f.write(uploadedfile.getbuffer())
	return st.success("Saved file :{} in tempDir".format(uploadedfile.name))


data_file = st.file_uploader("Upload CSV",type=['csv'])

if data_file is not None:
	file_details = {"FileName":data_file.name,"FileType":data_file.type}

	df = pd.read_csv(data_file, encoding='latin-1',sep='delimiter', header=None)
	st.dataframe(df)
	save_uploaded_file(data_file)
else:
	st.subheader("About")
        
model = pickle.load(open('data/model.pkl','rb'))
book_names = pickle.load(open('data/book_names.pkl','rb'))
final_rating = pickle.load(open('data/final_rating.pkl','rb'))
book_pivot = pickle.load(open('data/book_pivot.pkl','rb'))


def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url



def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list , poster_url       



selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books,poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])