# Assignment 16 - SVM, Trees, Ensembles, Validation & Unsupervised Learning

## Overview

This assignment focuses on implementing some of the most commonly used machine learning algorithms for classification and understanding how different validation techniques affect model performance.

For this assignment, I used the **Retail Sales Dataset** from Kaggle and applied different supervised learning algorithms to predict the **Product Category** based on customer and transaction information.

## Dataset Used

**Retail Sales Dataset**

Kaggle Link:
https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset

Target Variable:
- Product Category

Features Used:
- Age
- Gender
- Quantity
- Price per Unit
- Total Amount

## What I Implemented

### Task 1 - Support Vector Machine (SVM)

- Applied feature scaling using StandardScaler.
- Trained SVM using Linear kernel.
- Trained SVM using RBF kernel.
- Compared the performance of both kernels.
- Experimented with different values of the C parameter.

### Task 2 - Decision Tree

- Trained Decision Trees with different maximum depths.
- Compared training accuracy and testing accuracy.
- Observed signs of underfitting and overfitting.
- Visualized the decision tree.

### Task 3 - Train / Validation / Test Split

- Split the dataset into training, validation and testing sets.
- Used the validation set for selecting the best SVM parameter.
- Evaluated the final model on the unseen test data.

### Task 4 - Cross Validation

- Applied 5-Fold Cross Validation.
- Compared average cross-validation accuracy with the validation accuracy obtained from a single split.

### Task 5 - Ensemble Learning

Implemented:

- Bagging Classifier
- AdaBoost Classifier

Compared both models with a Decision Tree to understand how ensemble learning affects performance.

### Task 6 - Random Forest

- Trained a Random Forest classifier.
- Compared its performance with Decision Tree and Bagging.
- Displayed feature importance scores.

---

## Observations

Some interesting things I noticed while working on this assignment:

- Feature scaling is important for SVM because the algorithm is distance-based.
- Changing the C value affected the validation accuracy, although the improvement was small.
- Increasing the depth of a Decision Tree improved training accuracy but reduced testing accuracy, showing overfitting.
- Bagging and Random Forest achieved higher training accuracy than a single Decision Tree, but testing accuracy remained around 30–33%.
- Cross-validation gave a more reliable estimate of model performance than relying on a single train-test split.

Overall, this dataset appears difficult to classify because the different product categories have overlapping numerical features.

---

## Challenges Faced

- Choosing the best value of C for SVM.
- Understanding why higher training accuracy does not always lead to better testing accuracy.
- Comparing multiple algorithms fairly using the same preprocessing pipeline.
- Interpreting feature importance instead of only looking at accuracy scores.

---

## Libraries Used

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

## Repository

https://github.com/SuryanshTiwari18/GenAi-assignments

---

## Personal Learning

This assignment helped me understand that selecting a machine learning algorithm is only one part of building a model. Data preprocessing, feature scaling, validation techniques and proper evaluation are equally important.

I also learned that it is normal for real-world datasets to produce moderate accuracies. Instead of expecting every model to achieve very high accuracy, it is more important to understand why a model performs the way it does and compare different approaches objectively.