# Customer Segmentation using K-Means Clustering

## 📌 Overview

This project was completed as part of **Task 02** of the **Prodigy InfoTech Machine Learning Internship**.

The objective is to group retail store customers into meaningful segments using the **K-Means Clustering Algorithm** based on their annual income and spending behavior. Customer segmentation helps businesses understand customer patterns and make data-driven marketing decisions.

---

## 🎯 Objective

To apply K-Means Clustering and segment customers of a retail store based on:

* Annual Income (k$)
* Spending Score (1-100)

---

## 📂 Dataset

Dataset: Mall Customer Segmentation Dataset

Source:
https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

Features available in the dataset:

* CustomerID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1-100)

Features used for clustering:

* Annual Income (k$)
* Spending Score (1-100)

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

---

## 📋 Project Workflow

### 1. Data Collection

Loaded the customer dataset and explored its structure.

### 2. Data Preprocessing

Selected relevant numerical features for clustering.

### 3. Feature Selection

Used:

* Annual Income (k$)
* Spending Score (1-100)

### 4. Elbow Method

Determined the optimal number of clusters by analyzing WCSS values.

### 5. K-Means Clustering

Applied K-Means to segment customers into distinct groups.

### 6. Cluster Evaluation

Evaluated clustering quality using the Silhouette Score.

### 7. Data Visualization

Visualized customer clusters and cluster centroids.

---

## 📈 Elbow Method

The Elbow Method was used to determine the optimal number of clusters.

![Elbow Method](images/elbow_method.png)

---

## 📉 Customer Segmentation

Customer groups identified using K-Means Clustering.

![Customer Segments](images/clusters.png)

---

## 📏 Cluster Evaluation

The Silhouette Score was used to evaluate cluster quality.

**Silhouette Score: 0.554**

Interpretation:

* Close to +1 → Well-separated clusters
* Around 0 → Overlapping clusters
* Close to -1 → Poor clustering

The obtained score indicates that the customer groups are reasonably well-defined and meaningful.

---

## 📊 Results Summary

| Metric               | Value                         |
| -------------------- | ----------------------------- |
| Algorithm            | K-Means Clustering            |
| Dataset Size         | 200 Customers                 |
| Features Used        | Annual Income, Spending Score |
| Optimal Clusters (K) | 5                             |
| Evaluation Metric    | Silhouette Score              |
| Silhouette Score     | 0.554         |

---

## 🔍 Business Insights

### Cluster 1

Customers with balanced income and spending patterns.

### Cluster 2

High-income customers with high spending behavior (premium customers).

### Cluster 3

Low-income customers with lower spending behavior.

### Cluster 4

High-income customers with relatively lower spending.

### Cluster 5

Low-income customers with unexpectedly high spending.

Potential applications:

* Personalized marketing
* Customer retention strategies
* Product recommendation systems
* Loyalty program targeting

---

## 📁 Project Structure

PRODIGY_ML_02

├── data/
│ └── Mall_Customers.csv

├── images/
│ ├── elbow_method.png
│ └── clusters.png

├── notebooks/
│ └── customer_segmentation.ipynb

├── customer_segmentation.py

├── requirements.txt

└── README.md

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/kapoorakshat2610-afk/PRODIGY_ML_02.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python customer_segmentation.py
```

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Unsupervised Machine Learning
* K-Means Clustering
* Customer Segmentation
* Cluster Evaluation
* Silhouette Score Analysis
* Data Visualization
* Business Data Interpretation

---

## 🏢 Internship Information

**Organization:** Prodigy InfoTech

**Domain:** Machine Learning Internship

**Task:** Task 02 – Customer Segmentation using K-Means Clustering

---

## 👨‍💻 Author

Akshat Kapoor

GitHub:
https://github.com/kapoorakshat2610-afk
