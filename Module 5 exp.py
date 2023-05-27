# Example 1: NumPy Array
import numpy as np

# Create a 1-dimensional array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a 2-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Example 2: Pandas Series
import pandas as pd

# Create a Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Example 3: Pandas DataFrame
# Create a dictionary of data
data = {'Name': ['John', 'Emma', 'Sam', 'Alice'],
        'Age': [25, 28, 21, 24],
        'City': ['New York', 'Paris', 'London', 'Sydney']}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Example 4: Data Visualization with Matplotlib
import matplotlib.pyplot as plt

# Create data for x and y axes
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.show()

# Example 5: Advanced Data Analysis with Pandas
# Load data from a CSV file
data = pd.read_csv('data.csv')

# Handle missing data
data.dropna(inplace=True)

# Perform statistical analysis
mean = data['Column1'].mean()
std = data['Column2'].std()
