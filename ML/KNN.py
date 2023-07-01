import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

np.random.seed(0)

# randomly generate 10 cities
areas = np.random.uniform(50, 200, 10)  # 面积
bedrooms = np.random.randint(1, 6, 10)  # 卧室数量
cities = np.random.choice(['城市A', '城市B', '城市C'], 10)  # 地理位置

#  encoding cities
encoder = LabelEncoder()
cities_encoded = encoder.fit_transform(cities)

# assume the price of a house is 100000 + 10000 * area + 50000 * bedroom + 100000 * city
prices = 100000 + areas * 10000 + bedrooms * 50000 + cities_encoded * 100000

# create a dataframe with all these features
features = np.array(list(zip(areas, bedrooms, cities_encoded)))

# normalize the features
scaler = MinMaxScaler()
features = scaler.fit_transform(features)

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size=0.2, random_state=42)

# K=3
knn = KNeighborsRegressor(n_neighbors=3)

# FIT
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)


X_test_orig = scaler.inverse_transform(X_test)
print("Original features:", X_test_orig)
print("Predictions:", predictions)
print("Actual:", y_test)
