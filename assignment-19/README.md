# Assignment 19 - Word2Vec (CBOW & Skip-Gram)

## Student Details

**Name:** Suryansh Tiwari

---

## About the Assignment

In this assignment, I learned how Word2Vec creates word embeddings using the CBOW and Skip-Gram models. I trained both models on the SMS Spam Collection dataset and compared their performance. I also visualized the learned embeddings and performed vector arithmetic to understand how word relationships are represented.

---

## Dataset

**Dataset:** SMS Spam Collection Dataset

The dataset contains SMS messages labeled as spam or ham. It is commonly used for text classification and natural language processing tasks.

---

## Tasks Completed

- Loaded and explored the dataset
- Cleaned and preprocessed the text
- Tokenized the messages
- Trained a CBOW model
- Trained a Skip-Gram model
- Compared both models
- Performed vector arithmetic
- Visualized embeddings using PCA
- Visualized embeddings using t-SNE
- Wrote observations for each task

---

## Libraries Used

- Python
- pandas
- numpy
- matplotlib
- nltk
- gensim
- scikit-learn

---

## Project Files

```
Assignment-19.ipynb
README.md
spam.csv
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/SuryanshTiwari18/GenAi-assignments.git
```

2. Move to the project folder

```bash
cd assignment-19
```

3. Install the required libraries

```bash
pip install pandas numpy matplotlib nltk gensim scikit-learn
```

4. Open Jupyter Notebook

```bash
jupyter notebook
```

5. Open the notebook file and run all the cells from top to bottom.

---

## What I Learned

- Difference between CBOW and Skip-Gram
- How Word2Vec learns word embeddings
- How similar words are represented in vector space
- How vector arithmetic works with word embeddings
- Difference between PCA and t-SNE visualizations

---

## Conclusion

Both CBOW and Skip-Gram were able to learn useful word embeddings from the SMS Spam dataset. CBOW trained faster, while Skip-Gram produced better separated clusters in the t-SNE visualization. Since the dataset is relatively small, the models cannot learn complex relationships like large pretrained Word2Vec models, but they still capture meaningful relationships between frequently occurring words.
