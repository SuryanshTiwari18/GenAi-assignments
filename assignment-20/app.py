import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_resource
def load_data():
    # Load saved dataframe and TF-IDF vectorizer
    df = pickle.load(open("books.pkl", "rb"))
    tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

    # Recreate TF-IDF matrix
    tfidf_matrix = tfidf.transform(df["combined_text"])

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Create title-index mapping
    indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

    return df, cosine_sim, indices


df, cosine_sim, indices = load_data()


def recommend_books(book_title, top_n=5):

    idx = indices[book_title]

    similarity_scores = list(enumerate(cosine_sim[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:top_n + 1]

    recommendations = []

    for i, score in similarity_scores:

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
    "Select a book from the dropdown menu to get personalized recommendations based on content similarity."
)

selected_book = st.selectbox(
    "Choose a Book",
    sorted(df["title"].unique())
)


if st.button("Recommend Books"):

    recommendations = recommend_books(selected_book)

    st.subheader("Recommended Books")

    for i, book in enumerate(recommendations, start=1):

        st.markdown(f"### {i}. {book['Title']}")

        st.write(f"**Author:** {book['Author']}")

        st.write(f"**Category:** {book['Category']}")

        st.write(f"**Similarity Score:** {book['Similarity Score']}")

        st.divider()