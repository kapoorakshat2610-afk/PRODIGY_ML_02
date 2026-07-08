import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/Mall_Customers.csv")

print("Dataset Preview:")
print(df.head())

print("\nDataset Shape:", df.shape)

# ==========================================
# Feature Selection
# ==========================================

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# ==========================================
# Elbow Method
# ==========================================

wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow Method

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)

plt.savefig("images/elbow_method.png")
plt.show()

# ==========================================
# K-Means Clustering
# ==========================================

kmeans = KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=42,
    n_init=10
)

y_kmeans = kmeans.fit_predict(X)

# ==========================================
# Silhouette Score
# ==========================================

sil_score = silhouette_score(X, y_kmeans)

print("\n" + "=" * 50)
print(f"Silhouette Score: {sil_score:.3f}")
print("=" * 50)

# ==========================================
# Cluster Visualization
# ==========================================

plt.figure(figsize=(10, 7))

plt.scatter(
    X.iloc[y_kmeans == 0, 0],
    X.iloc[y_kmeans == 0, 1],
    s=80,
    label='Cluster 1'
)

plt.scatter(
    X.iloc[y_kmeans == 1, 0],
    X.iloc[y_kmeans == 1, 1],
    s=80,
    label='Cluster 2'
)

plt.scatter(
    X.iloc[y_kmeans == 2, 0],
    X.iloc[y_kmeans == 2, 1],
    s=80,
    label='Cluster 3'
)

plt.scatter(
    X.iloc[y_kmeans == 3, 0],
    X.iloc[y_kmeans == 3, 1],
    s=80,
    label='Cluster 4'
)

plt.scatter(
    X.iloc[y_kmeans == 4, 0],
    X.iloc[y_kmeans == 4, 1],
    s=80,
    label='Cluster 5'
)

# Centroids

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=300,
    marker='X',
    label='Centroids'
)

plt.title('Customer Segmentation using K-Means Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)

plt.savefig("images/clusters.png")
plt.show()

# ==========================================
# Cluster Summary
# ==========================================

df['Cluster'] = y_kmeans

print("\nCustomers per Cluster:")
print(df['Cluster'].value_counts().sort_index())

print("\nProject Completed Successfully!")