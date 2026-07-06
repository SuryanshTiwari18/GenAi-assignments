# Feature Engineering, Encoding, Scaling & Pipelines Assignment

## Description
This assignment demonstrates the complete data preprocessing workflow used in Machine Learning. It covers feature engineering, feature encoding, feature scaling, preprocessing pipelines, and building an end-to-end Scikit-learn pipeline using a Retail Sales dataset.

## Dataset Used
Retail Sales Dataset (Kaggle)

## Tasks Covered
- Task 1: Feature Engineering
  - Created new features such as Total Value, Age Group, Revenue Category, and Discount Percentage.
- Task 2: Date Feature Engineering
  - Extracted Year, Month, and Day from the Date column.
- Task 3: One-Hot Encoding
  - Applied One-Hot Encoding using `pd.get_dummies()`.
- Task 4: ColumnTransformer
  - Used `ColumnTransformer` with `OneHotEncoder` for categorical features while keeping numerical features unchanged.
- Task 5: Standardization
  - Applied `StandardScaler` to numerical features.
- Task 6: Normalization
  - Applied `MinMaxScaler` and compared the results with `StandardScaler`.
- Task 7: Preprocessing Pipeline
  - Built separate preprocessing pipelines for numerical and categorical features and combined them using `ColumnTransformer`.
- Task 8: Full Scikit-learn Pipeline
  - Created an end-to-end Machine Learning pipeline consisting of preprocessing and a `LinearRegression` model.
- Task 9: Pipeline Benefits
  - Explained the importance of pipelines, the problems they solve, and the differences between manual preprocessing and pipeline-based preprocessing.

## Libraries Used
- Pandas
- NumPy
- Scikit-learn

## Project Structure
```

Assignment-14-Feature-Engineering-Encoding-Scaling-Pipelines/
│
├── assignment14.ipynb
├── retail_sales_dataset.csv
├── README.md
├── requirements.txt
└── images/ (optional)

```

## How to Run
1. Open the project folder in VS Code.
2. Activate the virtual environment.
3. Install the required libraries:
   ```bash
   pip install pandas numpy scikit-learn
   ```
4. Place the `retail_sales_dataset.csv` file in the project folder.
5. Open `assignment14.ipynb`.
6. Run all notebook cells sequentially.

## Learning Outcomes
After completing this assignment, you will be able to:
- Create meaningful features from existing data.
- Perform feature encoding using One-Hot Encoding.
- Apply feature scaling techniques such as Standardization and Normalization.
- Build reusable preprocessing pipelines using Scikit-learn.
- Create an end-to-end Machine Learning pipeline for data preprocessing and prediction.

## GitHub Link
https://github.com/SuryanshTiwari18/GenAi-assignments.git
