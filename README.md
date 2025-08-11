# 🎥 Movie Recommendation System

A simple movie recommender web app built with **Streamlit** and **Pandas**.  
It uses collaborative filtering to recommend movies similar to a user-selected movie based on past ratings.

---

## 📸 Demo
When you select a movie from the sidebar, the app recommends similar movies based on correlation in ratings.  
It also shows two bar charts:
- **Number of Ratings**: Popularity of movies.
- **Average Rating**: Quality based on user feedback.

---

## ✨ Features
- **Movie Selection** from an interactive sidebar.
- **Top 10 Recommendations** based on similarity in user ratings.
- **Ratings Statistics**:
  - Number of ratings for each movie.
  - Average rating for each movie.
- **Interactive Charts** with Streamlit.

---

## 🛠️ Technologies Used
- **Python 3**
- **Streamlit** for the web interface.
- **Pandas** for data manipulation.
- **CSV & TSV files** for storing movie ratings and titles.

---

## 📂 Project Structure
├── app.py # Main Streamlit app script
├── file.tsv # MovieLens user ratings dataset
├── Movie_Id_Titles.csv # Mapping of movie IDs to movie titles

---

## Run the app
streamlit run app.py

---

👨‍💻 Author
Ayush Dhiman
📧 Email: harshitd9897@gmail.com
