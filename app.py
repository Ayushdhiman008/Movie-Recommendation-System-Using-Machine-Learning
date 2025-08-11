import pandas as pd
import streamlit as st

st.title("🎥 Movie Recommendation System")


st.write("Loading datasets...")
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('file.tsv', sep='\t', names=column_names)

movie_titles = pd.read_csv('Movie_Id_Titles.csv')


data = pd.merge(df, movie_titles, on='item_id')


ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = data.groupby('title')['rating'].count()


moviemat = data.pivot_table(index='user_id', columns='title', values='rating')

st.sidebar.header("Select a Movie")
selected_movie = st.sidebar.selectbox("Choose a movie to find similar recommendations:", ratings.index)


if selected_movie:
    st.write(f"Movies similar to **{selected_movie}**:")
   
    user_ratings = moviemat[selected_movie]
    

    similar_movies = moviemat.corrwith(user_ratings)
    corr_df = pd.DataFrame(similar_movies, columns=['Correlation'])
    corr_df.dropna(inplace=True)
    corr_df = corr_df.join(ratings['num of ratings'])
    
    recommendations = corr_df[corr_df['num of ratings'] > 100].sort_values('Correlation', ascending=False).head(10)
    
    st.table(recommendations)


st.header("Ratings Distribution")
st.subheader("Number of Ratings")
st.bar_chart(ratings['num of ratings'].sort_values(ascending=False).head(20))

st.subheader("Average Rating")
st.bar_chart(ratings['rating'].sort_values(ascending=False).head(20))
