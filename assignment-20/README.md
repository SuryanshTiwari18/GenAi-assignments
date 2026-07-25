# 📚 Book Recommendation System

A **Content-Based Book Recommendation System** built using **Python, Scikit-learn, TF-IDF Vectorization, Cosine Similarity, and Streamlit**. The system recommends books based on the textual similarity of their descriptions, authors, categories, and titles.

---

## 🌐 Live Demo

**Render Deployment:**  
https://book-recommendation-system-ro7f.onrender.com

---

## 📖 Project Overview

This project demonstrates a **Content-Based Recommendation System** using Natural Language Processing (NLP).

Instead of recommending books based on user ratings, the system analyzes the textual information of each book and recommends books with similar content.

The recommendation engine is built using:

- TF-IDF Vectorization
- Cosine Similarity
- Streamlit Web Application

---

## 📂 Dataset

**Dataset Name:** Books Dataset

Source:
https://www.kaggle.com/datasets/abdallahwagih/books-dataset

### Dataset Information

- Total Books: **6810**
- Total Features: **12**

### Features Used

- Title
- Subtitle
- Authors
- Categories
- Description

These features are combined into a single text column before applying TF-IDF Vectorization.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle
- Streamlit

---

## ⚙️ Project Workflow

### Task 1
- Dataset Selection
- Data Loading
- Dataset Exploration

### Task 2
- Data Cleaning
- Handling Missing Values
- Feature Selection
- Creating Combined Text

### Task 3
- TF-IDF Vectorization
- Vocabulary Generation
- Feature Matrix Creation

### Task 4
- Cosine Similarity
- Book Similarity Analysis
- Finding Similar Books

### Task 5
- Recommendation Function
- Top-N Similar Book Recommendations

### Task 6
- Streamlit User Interface
- Interactive Book Selection
- Recommendation Display

---

## 🚀 Features

- Content-Based Recommendation System
- Interactive Streamlit Interface
- Dropdown Book Selection
- Top 5 Similar Book Recommendations
- Displays:
  - Book Title
  - Author
  - Category
  - Similarity Score

---

## 📁 Project Structure

```
assignment-20/
│
├── app.py
├── Assignment20.ipynb
├── Books.csv
├── books.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/SuryanshTiwari18/GenAi-assignments.git
```

Move into Assignment-20

```bash
cd assignment-20
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💡 Recommendation Method

The recommendation system follows these steps:

1. Combine important textual features.
2. Convert text into TF-IDF vectors.
3. Generate the TF-IDF matrix.
4. Compute cosine similarity **on demand** for the selected book.
5. Return the Top 5 most similar books.

This on-demand approach avoids storing a large similarity matrix and improves deployment efficiency.

---

## 📸 Application Preview

- Select a book from the dropdown.
- Click **Recommend Books**.
- View the Top 5 recommended books with their:
  - Title
  - Author
  - Category
  - Similarity Score

---

## 📈 Future Improvements

- Book Cover Images
- Search Bar with Autocomplete
- Recommendation Filters
- Genre-Based Recommendations
- Author-Based Recommendations
- Hybrid Recommendation System
- Collaborative Filtering
- User Authentication
- Bookmark Favorite Books

---

## 👨‍💻 Author

**Suryansh Tiwari**

GitHub:
https://github.com/SuryanshTiwari18

LinkedIn:
https://www.linkedin.com/in/suryansh-tiwari-a09b32306/

---

## ⭐ Acknowledgements

- Kaggle Books Dataset
- Scikit-learn Documentation
- Streamlit Documentation

---

**Assignment:** 20  
**Topic:** Content-Based Book Recommendation System using TF-IDF and Cosine Similarity