import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from  scipy import stats

# Read data from the CSV file
data = pd.read_csv("C:\\Users\\Konny\\Downloads\\data.csv")
df = pd.DataFrame(data)
print(f'my dataframe{df}')

# Print all columns in the dataframe
print(f'print all columns in dataframe {df.columns}')
print(pd.isnull(df).sum())  # Check for missing values

# Print statistics of the dataframe
print(f'print statistics for all colums {df.describe()}')
# CO2 statistics
print(F'CO2 mode is {stats.mode(df['CO2'])}')
print(F'CO2 median is {np.median(df['CO2'])}')
print(F'CO2 mean is {np.mean(df['CO2'])}')
print(f'CO2 standard deviation is {np.std(df['CO2'])}')

plt.hist(df['CO2'], bins=5, color='lightsteelblue', alpha=0.7, edgecolor='black')  # bins = αριθμός στηλών
plt.title('Histogram CO2 ')
plt.xlabel('Values CO2')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
count_car = df['Car'].count()
count_co2 = df['CO2'].count()
print(count_car,count_co2)

# Group data by 'Car' and sum the 'CO2' values
groupby_columns = df.groupby(['Car'])['CO2'].sum().reset_index()

# Filter data for Ford and Mercedes cars
values_fort = df[df['Car'] == 'Ford']['CO2']
values_mercedes = df[df['Car'] == 'Mercedes']['CO2']

# Calculate mean CO2 for Ford and Mercedes
mean_fort = values_fort.mean()
mean_mercedes = values_mercedes.mean() 

# Calculate the difference between means
md = mean_fort - mean_mercedes

#Standard error difference
std_fort = values_fort.std()
std_mercedes = values_mercedes.std()
s_e_md = np.sqrt(std_fort **2 /len(values_fort) + std_mercedes ** 2/len(values_mercedes))

# Calculate the confidence interval for the difference
result_upper = md + 1.96 * s_e_md
result_lower = md - 1.96 * s_e_md

# Print the confidence interval
print(f'Confidence Interval for difference: {result_lower , result_upper}')

# Plot the total CO2 for each car
plt.bar(groupby_columns['Car'], groupby_columns['CO2'], color='lightsteelblue')
plt.xticks(rotation=50, fontsize=8, color='dimgray')
plt.yticks(fontsize=10,color='dimgray')
plt.title('Total CO2 Emissions by Car Brand', fontsize=14)
plt.ylabel('CO2 numbers')
plt.xlabel('Car Brand')
plt.tight_layout()
plt.grid(True)
plt.show()

