# Data Gathering, Preprocessing & Exploratory Data Analysis Assignment

## Description
This assignment demonstrates the complete data analysis workflow using multiple data sources, including CSV files, JSON files, SQLite databases, and REST APIs. It also covers data preprocessing, feature preparation, and exploratory data analysis (EDA) using Pandas, Matplotlib, and Seaborn.

## Datasets Used
- **CSV:** Titanic Dataset (Kaggle)
- **JSON:** Custom Products Dataset
- **SQLite:** Employees Database
- **API:** TMDB (The Movie Database) API

## Tasks Covered

### Part 1: Data Gathering
- Task 1: Load data from a CSV file (Titanic Dataset)
- Task 2: Load data from a JSON file
- Task 3: Create and query an SQLite database
- Task 4: Fetch movie data using the TMDB REST API

### Part 2: Data Preprocessing & Cleaning
- Task 5: Understand the dataset structure
- Task 6: Handle missing values, remove duplicates, rename columns, and verify data types
- Task 7: Feature preparation using One-Hot Encoding and feature selection

### Part 3: Exploratory Data Analysis (EDA)
- Task 8: Univariate Analysis
  - Histogram
  - KDE Plot
  - Count Plot
  - Box Plot
  - Violin Plot
  - Pie Chart
  - Bar Chart

- Task 9: Bivariate Analysis
  - Scatter Plot
  - Correlation Heatmap
  - Bar Plot
  - Box Plot
  - Violin Plot
  - Pair Plot
  - Regression Plot
  - LM Plot
  - Relational Plot
  - Categorical Plot
  - Distribution Plot
  - FacetGrid

- Task 10: Insights & Observations

## Libraries Used
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Requests
- SQLite3 (Built-in Python Library)

## How to Run
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the Titanic dataset (`train.csv`) from Kaggle and place it in the project folder.
4. Place `products.json` in the project folder.
5. Open `assignment13.ipynb`.
6. Run all notebook cells sequentially.

## Project Structure

```
Assignment-13/
│
├── assignment13.ipynb
├── README.md
├── train.csv
├── products.json
├── sample.db
└── tmdb_movies.csv
```

## Learning Outcomes
- Import data from multiple sources.
- Work with CSV, JSON, SQLite, and REST APIs.
- Perform data cleaning and preprocessing.
- Prepare features for machine learning.
- Visualize data using Matplotlib and Seaborn.
- Extract meaningful insights through exploratory data analysis.

## GitHub Repository
https://github.com/SuryanshTiwari18/GenAi-assignments.git