# Example 1: Linear Regression
from sklearn.linear_model import LinearRegression
import numpy as np

# Create sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
X_test = np.array([[6], [7]])
predictions = model.predict(X_test)

# Example 2: K-means Clustering
from sklearn.cluster import KMeans
import numpy as np

# Create sample data
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Create and train the model
model = KMeans(n_clusters=2)
model.fit(X)

# Get cluster labels
labels = model.labels_

# Example 3: Image Classification with CNN
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess data
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# Create and train the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# Example 4: Text Sentiment Analysis with NLP
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Create sample data
X = ['I love this movie', 'This movie is terrible', 'Great movie!', 'Awful movie']
y = ['positive', 'negative', 'positive', 'negative']

# Create feature vectors
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Create and train the model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Make predictions
X_test = ['I like this movie', 'This movie is amazing']
X_test_vectorized = vectorizer.transform(X_test)
predictions = model.predict(X_test_vectorized)
