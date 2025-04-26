# preprocess_datasets.py

import os
import pandas as pd

# Create processed folder if it doesn't exist
os.makedirs('processed', exist_ok=True)

# ------------------------------
# Load original datasets
# ------------------------------
acs = pd.read_csv('datasets/acs_demographics_chattanooga_2023.csv')
cdc = pd.read_csv('datasets/cdc_places_chattanooga_2023_filtered.csv')
epa = pd.read_csv('datasets/epa_pm25_chattanooga_filtered.csv')

# ------------------------------
# Preprocessing ACS Demographics 2023
# ------------------------------
# Select only key demographic indicators
# --- Preprocessing ACS Demographics 2023 ---
acs_selected = acs[[
    'NAME',
    'DP03_0062E',   # Median Household Income
    'DP03_0001PE',  # Civilian Labor Force Participation (%)
    'DP03_0005PE'   # Unemployment Rate (%)
]]

acs_selected.rename(columns={
    'NAME': 'Geography',
    'DP03_0062E': 'Median Household Income ($)',
    'DP03_0001PE': 'Civilian Labor Force (%)',
    'DP03_0005PE': 'Unemployment Rate (%)'
}, inplace=True)

# ------------------------------
# Preprocessing CDC PLACES 2024
# ------------------------------
# Drop rows with missing Estimate Value
cdc_cleaned = cdc.dropna(subset=['Estimate Value'])

# Clean whitespace in Health Indicator names
cdc_cleaned['Health Indicator'] = cdc_cleaned['Health Indicator'].str.strip()

# Select only key health indicators (OPTIONAL)
important_indicators = [
    'Current asthma among adults aged >=18 years',
    'Diagnosed diabetes among adults aged >=18 years',
    'Obesity among adults aged >=18 years',
    'High blood pressure among adults aged >=18 years',
    'Mental health not good for >=14 days among adults aged >=18 years'
]

cdc_filtered = cdc_cleaned[cdc_cleaned['Health Indicator'].isin(important_indicators)]

# ------------------------------
# Preprocessing EPA PM2.5 2023
# ------------------------------
# Convert Date Local to datetime
epa['Date Local'] = pd.to_datetime(epa['Date Local'])

# Create Month column
epa['Month'] = epa['Date Local'].dt.to_period('M')

# Aggregate by Month (mean PM2.5 and AQI)
epa_monthly = epa.groupby('Month').agg({
    'Arithmetic Mean': 'mean',
    'AQI': 'mean'
}).reset_index()

epa_monthly.rename(columns={
    'Arithmetic Mean': 'Avg PM2.5',
    'AQI': 'Avg AQI'
}, inplace=True)

# ------------------------------
# Save Preprocessed Data
# ------------------------------
acs_selected.to_csv('processed/acs_preprocessed.csv', index=False)
cdc_filtered.to_csv('processed/cdc_preprocessed.csv', index=False)
epa_monthly.to_csv('processed/epa_pm25_monthly.csv', index=False)

print("✅ Preprocessing complete. Preprocessed files saved in 'processed/' folder.")
