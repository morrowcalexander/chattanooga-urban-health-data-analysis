import pandas as pd

acs = pd.read_csv('datasets/acs_demographics_chattanooga_2023.csv')

# Print all column names
print(acs.columns.tolist())