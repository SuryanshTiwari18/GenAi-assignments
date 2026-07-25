import streamlit as st
import pandas as pd
import pickle

df=pickle.load(open("books.pkl","rb"))
cosine_sim=pickle.load(open("cosine_sim.pkl","rb"))
indices=pd.Series(df.index,index=df['title']).drop_duplicates()

def recommend_books(title, top_n=10):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    recommendations=[]
    for i,score in sim_scores:
        recommendations.append({
            "Title": df.iloc[i]["title"],
            "Author": df.iloc[i]["authors"],
            "Category": df.iloc[i]["categories"],
            "Similarity Score": round(score, 3)
        })
    return recommendations

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Book Recommendation System")

st.write(
    "Select a book to receive content-based recommendations."
)

selected_book = st.selectbox(
    "Choose a Book",
    sorted(df["title"].unique())
)

if st.button("Recommend Books"):
    recommendations = recommend_books(selected_book)
    st.subheader("Recommended Books:")
    for i, book in enumerate(recommendations, start=1):
        st.markdown(f"### {i}. {book['Title']}")
        st.write(f"**Author:** {book['Author']}")
        st.write(f"**Category:** {book['Category']}")
        st.write(f"**Similarity Score:** {book['Similarity Score']}")
        st.divider()
        