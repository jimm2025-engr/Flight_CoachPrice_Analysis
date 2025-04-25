# Flight Coach Price Analysis
# This script loads flight price data and plots a histogram of coach prices.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
flight = pd.read_csv("flight.csv")
print(flight.head())

# Summary Statistics
print(flight["coach_price"].describe())

# Histogram of Coach Prices
plt.figure(figsize=(10, 6))
sns.histplot(flight['coach_price'], kde=True, color='blue', bins=30)
plt.title('Distribution of Coach Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
