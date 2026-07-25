import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------------------
# Load Data
# -----------------------------------------
@st.cache_resource
def load_data():
    df = pickle.load(open("books.pkl", "rb"))
    tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

    # Create TF-IDF matrix only once
    tfidf_matrix = tfidf.transform(df["combined_text"])

    # Mapping from title to dataframe index
    indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

    return df, tfidf_matrix, indices


df, tfidf_matrix, indices = load_data()


# -----------------------------------------
# Recommendation Function
# -----------------------------------------
def recommend_books(book_title, top_n=5):

    idx = indices[book_title]

    # Compute similarity only for the selected book
    similarity_scores = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    similar_books = list(enumerate(similarity_scores))

    similar_books = sorted(
        similar_books,
        key=lambda x: x[1],
        reverse=True
    )

    # Ignore the selected book itself
    similar_books = similar_books[1:top_n + 1]

    recommendations = []

    for i, score in similar_books:

        recommendations.append({
            "Title": df.iloc[i]["title"],
            "Author": df.iloc[i]["authors"],
            "Category": df.iloc[i]["categories"],
            "Similarity Score": round(float(score), 3)
        })

    return recommendations


# -----------------------------------------
# Streamlit UI
# -----------------------------------------
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Book Recommendation System")

st.write(
    "Select a book from the dropdown menu to receive content-based recommendations."
)

selected_book = st.selectbox(
    "Choose a Book",
    sorted(df["title"].unique())
)

if st.button("Recommend Books"):

    with st.spinner("Finding similar books..."):

        recommendations = recommend_books(selected_book)

    st.subheader("Recommended Books")

    for i, book in enumerate(recommendations, start=1):

        st.markdown(f"### {i}. {book['Title']}")

        st.write(f"**Author:** {book['Author']}")

        st.write(f"**Category:** {book['Category']}")

        st.write(f"**Similarity Score:** {book['Similarity Score']}")

        st.divider()