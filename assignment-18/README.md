# Assignment 18 – Feature Extraction Techniques for NLP

## Student Information

**Name:** Suryansh Tiwari

**Assignment:** Feature Extraction Techniques for Natural Language Processing (NLP)

---

# Project Overview

In this assignment, I explored different feature extraction techniques used in Natural Language Processing (NLP). Since machine learning models cannot work directly with raw text, textual data must first be converted into numerical representations.

I implemented and compared several commonly used techniques, including:

- Manual One-Hot Encoding
- One-Hot Encoding using Scikit-learn
- Bag of Words (BoW)
- Word Frequency Analysis
- N-Grams (Unigrams, Bigrams and Trigrams)
- TF-IDF (Term Frequency – Inverse Document Frequency)
- Parameter tuning in CountVectorizer

Throughout the notebook, I also analyzed the outputs to better understand how different vectorization methods represent text.

---

# Dataset Information

**Dataset Name:** SMS Spam Collection Dataset

**Source:** Kaggle

**Dataset Link:**
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

### Dataset Summary

- Total Messages: **5,572**
- Classes:
  - Ham (Normal Messages)
  - Spam Messages
- Text used: **final_clean_text** (generated in the previous assignment after preprocessing)

---

# Objectives

The objectives of this assignment were to:

- Understand how text is converted into numerical vectors.
- Implement One-Hot Encoding manually.
- Apply Scikit-learn vectorization techniques.
- Learn how Bag of Words represents word frequencies.
- Explore word frequency statistics.
- Generate Unigrams, Bigrams and Trigrams.
- Understand TF-IDF weighting.
- Compare Bag of Words and TF-IDF.
- Explore important CountVectorizer parameters.

---

# Libraries Used

- pandas
- numpy
- matplotlib
- scikit-learn

Modules used:

- CountVectorizer
- TfidfVectorizer

---

# Tasks Performed

## Task 1 – Manual One-Hot Encoding

- Selected sample SMS messages.
- Built the vocabulary manually.
- Created binary vectors using Python loops.
- Displayed the encoded vectors as a DataFrame.

---

## Task 2 – One-Hot Encoding using Scikit-learn

- Used CountVectorizer with `binary=True`.
- Compared the generated vocabulary with the manual implementation.
- Observed that Scikit-learn ignores single-character tokens by default.

---

## Task 3 – Bag of Words (BoW)

- Generated Bag of Words vectors for the complete dataset.
- Created the document-term matrix.
- Explored the vocabulary and feature vectors.

---

## Task 4 – Word Frequency Analysis

- Calculated word frequencies across the entire dataset.
- Displayed the most frequent words.
- Displayed the least frequent words.
- Visualized the top words using a bar chart.

---

## Task 5 – N-Grams

Generated:

- Unigrams
- Bigrams
- Trigrams

Compared their vocabulary sizes and observed how the number of features increases when word combinations are considered.

---

## Task 6 – Comparison of N-Grams

Compared:

- Vocabulary sizes
- Matrix dimensions
- Context captured by each representation

Observed that higher-order N-Grams preserve more context but also produce a much larger feature space.

---

## Task 7 – TF-IDF Vectorization

Generated TF-IDF vectors for the dataset.

Observed:

- Highest-weight words
- Lowest-weight words
- TF-IDF score distribution

Learned how TF-IDF emphasizes informative words while reducing the importance of common words.

---

## Task 8 – Bag of Words vs TF-IDF

Compared both techniques based on:

- Vocabulary size
- Matrix dimensions
- Word importance
- Common word weighting

Observed that TF-IDF provides a more informative representation for many NLP tasks.

---

## Task 9 – CountVectorizer Parameter Exploration

Experimented with:

- max_features
- min_df
- max_df

Observed how these parameters affect vocabulary size and feature selection.

---

## Task 10 – Conceptual Questions

Answered conceptual questions related to:

- One-Hot Encoding
- Bag of Words
- N-Grams
- TF-IDF
- Count-based vectorization

---

# Key Observations

Some observations I made while completing this assignment:

- Manual One-Hot Encoding helped me understand how vectorization works internally.
- Bag of Words stores word frequencies instead of only indicating presence.
- The SMS dataset contains many unique words, resulting in a sparse feature space.
- N-Grams preserve word order but greatly increase the vocabulary size.
- TF-IDF assigns higher weights to informative words and lower weights to common words such as *call*, *text*, and *go*.
- Increasing `min_df` significantly reduced the vocabulary size by removing rare words.
- In this dataset, changing `max_df` had almost no effect because no word appeared in more than 80% of the messages.

---

# Learning Outcomes

After completing this assignment, I gained a better understanding of:

- How text is transformed into numerical data.
- Differences between One-Hot Encoding and Bag of Words.
- Why N-Grams increase feature dimensions.
- How TF-IDF calculates word importance.
- When TF-IDF is preferred over simple word counts.
- How CountVectorizer parameters influence vocabulary size.
- The importance of feature extraction before applying machine learning algorithms.

---

# Folder Structure

```
Assignment_18/
│
├── assignment_18.ipynb
├── README.md
└── spam.csv
```

---

# Conclusion

This assignment helped me understand the feature extraction stage of an NLP pipeline. I learned how different vectorization techniques represent text, what information they preserve, and their respective advantages and limitations.

Compared to the previous assignment, which focused on text preprocessing, this assignment showed how cleaned text can be transformed into numerical features that can be used by machine learning models for tasks such as spam detection, sentiment analysis, and document classification.