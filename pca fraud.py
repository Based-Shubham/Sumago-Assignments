import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X, y = make_classification(n_samples=5000, n_features=28, n_informative=8, n_redundant=6,
                            weights=[0.98, 0.02], flip_y=0.001, class_sep=1.2, random_state=42)
feature_names = [f"V{i+1}" for i in range(28)]
df = pd.DataFrame(X, columns=feature_names)
df["Amount"] = np.round(np.abs(np.random.exponential(scale=60, size=len(df))), 2)
df["Class"] = y

features = [c for c in df.columns if c != "Class"]
X = df[features].values
y = df["Class"].values

X_scaled = StandardScaler().fit_transform(X)

pca_full = PCA().fit(X_scaled)
cumulative = np.cumsum(pca_full.explained_variance_ratio_)
n_components_95 = np.argmax(cumulative >= 0.95) + 1

plt.plot(range(1, len(cumulative) + 1), cumulative, marker="o")
plt.axhline(0.95, color="red", linestyle="--")
plt.xlabel("Number of components")
plt.ylabel("Cumulative explained variance")
plt.show()

pca = PCA(n_components=n_components_95)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[y == 0, 0], X_pca[y == 0, 1], s=8, alpha=0.4, label="Normal")
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], s=15, alpha=0.8, color="red", label="Fraud")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()

print(X_scaled.shape[1], X_pca.shape[1])
