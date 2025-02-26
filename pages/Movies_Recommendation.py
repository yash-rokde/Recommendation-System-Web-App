import streamlit as st
import pickle
import pandas as pd
import requests
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=''.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w780/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommend_movies = []
    recommend_movies_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
      
        
        recommend_movies.append(movies.iloc[i[0]].title)

          # fetch poster from api
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_posters


movies_dict = pickle.load(open('data/movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('data/similarity.pkl','rb'))
st.title('Movie Recommender System')
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
selected_movie_name = st.selectbox(
    'Which movie you would like to choose?',
     movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
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