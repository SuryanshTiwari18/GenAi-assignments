# Assignment 19: Word2Vec Text Embeddings

## Overview

This project demonstrates the implementation of **Word2Vec**, one of the most widely used word embedding techniques in Natural Language Processing (NLP). Unlike traditional vectorization methods such as Bag of Words (BoW) and TF-IDF, Word2Vec learns dense vector representations that capture semantic relationships between words.

The assignment covers the theoretical concepts behind word embeddings, compares the **CBOW** and **Skip-Gram** architectures, trains both models on the **SMS Spam Collection Dataset**, performs word similarity and vector arithmetic operations, and visualizes learned embeddings using PCA.

---

## Objectives

- Understand the concept of word embeddings.
- Learn why traditional vectorization methods have limitations.
- Study the working of the Word2Vec algorithm.
- Compare CBOW and Skip-Gram architectures.
- Train Word2Vec models using Gensim.
- Find similar words using learned embeddings.
- Perform vector arithmetic using word vectors.
- Visualize word embeddings using PCA.
- Analyze the advantages and limitations of Word2Vec.

---

## Dataset

**Dataset Used:** SMS Spam Collection Dataset

- Total Messages: **5,572**
- Classes:
  - Ham
  - Spam

The cleaned text generated in the previous NLP preprocessing assignment (`final_clean_text`) was used for training the Word2Vec models.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Gensim
- NLTK
- Scikit-learn
- Matplotlib

---

# Assignment Tasks

## Task 1 – Understanding Word Embeddings

Studied the concept of word embeddings and answered the following conceptual questions:

- What are word embeddings?
- Why do One-Hot Encoding and Bag of Words fail to capture semantics?
- How do embeddings solve these problems?

---

## Task 2 – Word2Vec Overview

Covered the working of Word2Vec, including:

- Vocabulary creation
- Context window
- Embedding dimensions
- Learning words from context

---

## Task 3 – CBOW vs Skip-Gram

Compared the two Word2Vec architectures.

### CBOW

- Predicts the target word using surrounding context words.
- Faster to train.
- Performs well on larger datasets.

### Skip-Gram

- Predicts surrounding context words using the target word.
- Better at learning representations for rare words.
- Slightly slower than CBOW.

---

## Task 4 – Neural Network Intuition

Studied the neural network architecture behind Word2Vec.

Topics covered:

- Input layer
- Hidden (Embedding) layer
- Output layer
- How embedding weights are learned

---

## Task 5 – Preparing Text for Word2Vec

Prepared the cleaned SMS dataset by:

- Tokenizing messages into words
- Creating a list of tokenized sentences
- Computing sentence length statistics

### Dataset Statistics

- Average Sentence Length: **8.63 words**
- Shortest Sentence: **0 words**
- Longest Sentence: **80 words**

---

## Task 6 – Training the CBOW Model

Trained a CBOW Word2Vec model using:

- Vector Size = **100**
- Window Size = **5**
- Minimum Word Count = **1**
- sg = **0 (CBOW)**

### Results

- Training Time: **0.25 seconds**
- Vocabulary Size: **7,830 words**
- Embedding Dimension: **100**

Displayed:

- Vocabulary
- Sample embedding vectors

---

## Task 7 – Training the Skip-Gram Model

Trained a Skip-Gram model using:

- Vector Size = **100**
- Window Size = **5**
- Minimum Word Count = **1**
- sg = **1 (Skip-Gram)**

### Results

| Feature | CBOW | Skip-Gram |
|---------|------:|----------:|
| Training Time | 0.25 s | 0.44 s |
| Vocabulary Size | 7,830 | 7,830 |
| Embedding Dimension | 100 | 100 |

---

## Task 8 – Word Similarity & Vector Arithmetic

Performed similarity search using the trained Word2Vec models.

Examples included:

- Finding words similar to:
  - free
  - call
  - prize
  - mobile

Performed vector arithmetic such as:

- free + call − text
- win + prize − free
- claim + cash − prize
- mobile + call − text

These operations demonstrated that Word2Vec embeddings preserve semantic relationships between words.

---

## Task 9 – Word Embedding Visualization

Reduced the 100-dimensional embeddings to two dimensions using **Principal Component Analysis (PCA)**.

Visualized important words from the SMS dataset including:

- free
- call
- text
- prize
- mobile
- claim
- cash
- reply
- receive

### Observation

Words appearing in similar contexts were generally positioned closer together in the embedding space. Although the SMS dataset is relatively small, meaningful semantic relationships were still observable.

---

## Task 10 – Observations & Limitations

### Difference between CBOW and Skip-Gram

| CBOW | Skip-Gram |
|------|-----------|
| Predicts target word | Predicts context words |
| Faster training | Slower training |
| Better for frequent words | Better for rare words |

### Advantages of Word2Vec

- Captures semantic meaning.
- Learns contextual relationships.
- Dense vector representation.
- Similar words are located close together.
- Supports vector arithmetic.

### Limitations

- Requires a reasonably large corpus.
- Produces one embedding per word regardless of context.
- Cannot distinguish multiple meanings of the same word.
- Performance depends on training data quality.

### Why Modern NLP Uses Contextual Embeddings

Unlike Word2Vec, transformer-based models (such as BERT and GPT) generate context-aware embeddings, allowing the same word to have different meanings depending on the surrounding sentence.

---

# Results Summary

- Successfully trained both **CBOW** and **Skip-Gram** models.
- Learned dense vector representations for **7,830 unique words**.
- Compared the training performance of both architectures.
- Performed semantic similarity searches.
- Demonstrated vector arithmetic using learned embeddings.
- Visualized word relationships using PCA.
- Understood the strengths and limitations of Word2Vec.

---

# Conclusion

This assignment introduced the concept of word embeddings and demonstrated how Word2Vec captures semantic relationships between words. Both CBOW and Skip-Gram models were successfully trained on the SMS Spam Collection dataset. The learned embeddings enabled similarity searches, vector arithmetic, and visualization of word relationships, highlighting the advantages of embedding-based representations over traditional count-based methods such as Bag of Words and TF-IDF. This assignment also provided a foundation for understanding contextual embeddings used in modern transformer-based NLP models.

---

## Author

**Suryansh Tiwari**