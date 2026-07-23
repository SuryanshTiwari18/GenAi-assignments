# NLP Assignment - Text Preprocessing using NLTK

## Description

This assignment focuses on performing various Natural Language Processing (NLP) preprocessing techniques using Python and the NLTK library. The objective was to understand how raw text can be cleaned and transformed into a structured format that is suitable for machine learning and text analysis.

For this assignment, I used the **SMS Spam Collection Dataset** from Kaggle and implemented each preprocessing step individually before combining them into a complete NLP preprocessing pipeline.

## Dataset

**Dataset Name:** SMS Spam Collection Dataset

**Kaggle Link:**  
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Tasks Covered

- Dataset loading and exploration
- Basic text cleaning
  - Lowercasing
  - Removing punctuation
  - Removing numbers
  - Removing extra spaces
- Advanced text cleaning
  - Removing URLs
  - Removing email addresses
  - Removing HTML tags
- Stopword removal
- Handling repeated characters
- Handling slang words using a custom dictionary
- Word tokenization
- Sentence tokenization
- Stemming using Porter Stemmer
- Lemmatization using WordNet Lemmatizer
- Building a complete NLP preprocessing pipeline
- Comparing original and processed text

## Libraries Used

- pandas
- numpy
- matplotlib
- nltk
- re (Regular Expressions)

## Key Observations

- The dataset contains **5,572 SMS messages**, with the majority belonging to the **ham** class.
- Most SMS messages are very short and contain only one sentence.
- Removing stopwords and punctuation significantly reduced unnecessary text while preserving important information.
- Stemming reduced words to their root forms but sometimes produced words that were difficult to read.
- Lemmatization generated more meaningful English words compared to stemming.
- During preprocessing, a few messages became empty because they mainly contained stopwords or very little useful information.
- Combining all preprocessing techniques into a single pipeline made the text cleaner and more consistent for future NLP tasks.

## What I Learned

While working on this assignment, I realized that every preprocessing technique has a different purpose and can affect the dataset in different ways.

I found it interesting to compare stemming and lemmatization because both reduce words, but lemmatization generally produces more readable results. I also learned that it is important to explore the dataset before preprocessing instead of applying techniques blindly. Looking at intermediate outputs helped me understand how each step transformed the text.

Overall, this assignment gave me a much better understanding of the preprocessing stage in an NLP workflow.

## How to Run

1. Open the notebook: `NLP_Assignment.ipynb`
2. Install the required libraries if they are not already installed.
3. Run all notebook cells sequentially.

## GitHub Repository

https://github.com/SuryanshTiwari18/GenAi-assignments.git