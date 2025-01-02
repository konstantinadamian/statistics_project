import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read data from the CSV file
data = pd.read_csv("C:\\Users\\Konny\\Downloads\\data.csv")
df = pd.DataFrame(data)

# Print all columns in the dataframe
print(f'print all columns in dataframe {df}')
print(pd.isnull(df).sum())  # Check for missing values
print(f'print statistics {df.describe()}')  # Print statistics of the dataframe

# Group data by 'Car' and sum the 'CO2' values
groupby_columns = df.groupby(['Car'])['CO2'].sum().reset_index()

# Filter data for Ford and Mercedes cars
valus_fort = df[df['Car'] == 'Ford']['CO2']
valus_mercedes = df[df['Car'] == 'Mercedes']['CO2']

# Calculate mean CO2 for Ford and Mercedes
mean_fort = valus_fort.mean()
mean_mercedes = valus_mercedes.mean()

# Calculate the difference between means
md = mean_fort - mean_mercedes

# Calculate the standard error of the difference
s_e_md = np.sqrt(mean_fort/len(valus_fort) + mean_mercedes/len(valus_mercedes))

# Calculate the confidence interval for the difference
result_ = (md + 1.96 * s_e_md) , (md - 1.96 * s_e_md)
print(f'Confidence Interval for difference: {result_}')  # Print the confidence interval

# Plot the total CO2 for each car
plt.plot(groupby_columns['Car'], groupby_columns['CO2'], color='b')
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.ylabel('CO2 numbers')
plt.xlabel('Car name')
plt.tight_layout()
plt.grid(True)
plt.show()

