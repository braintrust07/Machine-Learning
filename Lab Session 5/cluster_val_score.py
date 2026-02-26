import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

def load_all_feature_files(folder_path):
    all_dfs = []
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx") or file.endswith(".xls"):
            df = pd.read_excel(os.path.join(folder_path, file))
            all_dfs.append(df)
    return pd.concat(all_dfs, ignore_index=True)

def split_xy(data):
    X = data.iloc[:, :-1]  
    y = data.iloc[:, -1]    
    return X, y

folder_path = r"C:\Users\syama\OneDrive\Desktop\ML\eeg-during-mental-arithmetic-tasks-1.0.0\features\features"

data = load_all_feature_files(folder_path)
X, y_class = split_xy(data)
y_pseudo = X.iloc[:, 0]
X_reg = X.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(
    X_reg, y_pseudo, test_size=0.2, random_state=42
)
X_cluster = X

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

kmeans = KMeans(n_clusters=2, random_state=42, n_init="auto")
labels = kmeans.fit_predict(X_train)

print("Silhouette:", silhouette_score(X_train, labels))
print("CH:", calinski_harabasz_score(X_train, labels))
print("DB:", davies_bouldin_score(X_train, labels))