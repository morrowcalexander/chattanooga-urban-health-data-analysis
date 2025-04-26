# Chattanooga Urban Health Data Analysis

This project explores health outcomes and environmental conditions in Chattanooga, Tennessee, through the analysis of three thematically connected real-world datasets:

- **Environmental Protection Agency (EPA) Air Quality Monitoring Data**
- **Centers for Disease Control and Prevention (CDC) PLACES Health Outcome Data**
- **United States Census Bureau Demographic Data (American Community Survey)**

The goal is to investigate potential patterns between environmental quality, public health outcomes, and socioeconomic factors within Chattanooga’s urban population using interactive data visualizations.

---

# Data Filtering Prior to Upload

Before uploading the datasets into the project environment, initial filtering was conducted to ensure relevance, manageable size, and focus on Chattanooga:

- **ACS Demographics 2023**:  
  Filtered to include only Chattanooga-area records, resulting in 2 records with 551 demographic and economic attributes.

- **CDC PLACES 2024**:  
  Filtered to retain 145 health indicator records related to Chattanooga.

- **EPA PM2.5 2023**:  
  Filtered to include daily PM2.5 measurements only for Chattanooga's monitoring sites (369 records total).

> **Purpose:**  
> To reduce file size, minimize processing overhead, and focus analysis exclusively on Chattanooga’s urban population.

---

# Data Preprocessing for Visualization

After uploading, further preprocessing steps were applied to prepare the data for effective visualization:

- **ACS Demographics 2023**:
  - Selected three core socioeconomic attributes: Median Household Income, Civilian Labor Force Participation (%), and Unemployment Rate (%).
  - Renamed columns for clarity.
  - Verified data types and completeness.

- **CDC PLACES 2024 (Filtered)**:
  - Dropped records with missing **Estimate Value** fields.
  - Cleaned and standardized **Health Indicator** names.
  - Filtered down to five key chronic health indicators:
    - Current Asthma
    - Diagnosed Diabetes
    - Obesity
    - High Blood Pressure
    - Poor Mental Health (14+ days)

- **EPA PM2.5 2023 (Filtered)**:
  - Converted **Date Local** to datetime format.
  - Created a **Month** field.
  - Aggregated daily PM2.5 and AQI measurements into monthly averages.

> **Purpose:**  
> To ensure clean, well-structured datasets optimized for creating interactive visualizations that reveal trends, patterns, and outliers in Chattanooga’s urban health profile.

---

# Dataset 1: ACS Demographics 2023 (Preprocessed)

The first dataset, *ACS Demographics 2023*, was sourced from the American Community Survey (ACS) and focuses specifically on the Chattanooga metropolitan area.  
The original dataset contained 2 records and over 550 attributes covering a wide range of demographic, economic, housing, and social indicators.  
For the purposes of this project, a subset of three key economic variables was selected:

- **Median Household Income**
- **Civilian Labor Force Participation Rate (%)**
- **Unemployment Rate (%)**

These attributes were chosen to provide socioeconomic context regarding employment and income levels in the area.  
The selected columns were renamed for clarity, and no significant missing values were encountered.  
This dataset offers a critical demographic and economic foundation for the project.

---

# Dataset 2: CDC PLACES 2024 (Filtered and Preprocessed)

The second dataset, *CDC PLACES 2024 (Filtered)*, originates from the Centers for Disease Control and Prevention’s PLACES project, which models and estimates health outcomes, preventive service use, and health behaviors at the local level.  
The initial dataset included 145 records across three attributes: **Health Indicator**, **Estimate Value**, and **Percent Value**.  
Preprocessing steps included:

- Removing records with missing estimate values.
- Cleaning and standardizing health indicator names.
- Filtering to retain only five critical health outcomes relevant to urban public health:
  - Current Asthma
  - Diagnosed Diabetes
  - Obesity
  - High Blood Pressure
  - Poor Mental Health (14+ days)

These indicators provide a focused lens into major chronic health issues affecting Chattanooga residents.

---

# Dataset 3: EPA PM2.5 2023 (Aggregated and Preprocessed)

The third dataset, *EPA PM2.5 2023 (Filtered)*, was sourced from the U.S. Environmental Protection Agency’s air quality monitoring network.  
It originally included 369 daily observations of Chattanooga’s fine particulate matter (PM2.5) levels for 2023, capturing six attributes: **Date Local**, **Site Number**, **Arithmetic Mean**, **AQI (Air Quality Index)**, **Latitude**, and **Longitude**.  
Preprocessing involved:

- Parsing dates into a datetime format.
- Creating a "Month" attribute to enable temporal aggregation.
- Calculating monthly averages for PM2.5 levels and AQI values.

The resulting dataset provides a concise summary of Chattanooga’s monthly air quality patterns, suitable for temporal trend visualization and comparison against public health data.

---

# Project Structure

