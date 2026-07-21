import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 1. Load data
df = pd.read_csv("iris.csv")

# IMPORTANT: Select only the first 2 feature columns (e.g., Sepal Length & Sepal Width)
# This allows us to map them directly to a 2D flat X/Y grid boundary.
X = df.iloc[:, :2].values
y = df.iloc[:, -1].values

# 2. Convert text strings ('virginica') to numbers (0, 1, 2)
le = LabelEncoder()
y = le.fit_transform(y)

# 3. Split the data (UNCOMMENTED)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Scale features (UNCOMMENTED)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Train the Model (UNCOMMENTED)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 6. Create a grid mesh to plot the decision boundaries
x_min, x_max = X_test[:, 0].min() - 1, X_test[:, 0].max() + 1
y_min, y_max = X_test[:, 1].min() - 1, X_test[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# 7. Predict the class for every single point on the background grid mesh
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 8. Plot the colored background zones
plt.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")

# 9. Overlay your actual test data points on top
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap="coolwarm", edgecolors="k", s=50)
plt.title("KNN Decision Boundaries vs Actual Test Points (2 Features)")
plt.xlabel("Feature 1 (Scaled)")
plt.ylabel("Feature 2 (Scaled)")
plt.show()
