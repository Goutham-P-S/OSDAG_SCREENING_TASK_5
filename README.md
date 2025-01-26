# OSDAG_SCREENING_TASK_5

# BridgeCostApp

**BridgeCostApp** is a Python-based desktop application built using PyQt5 and SQLite. It allows users to calculate and compare the construction costs of a bridge using two materials: **Steel** and **Concrete**. The application takes user input for various parameters like span length, width, traffic volume, and design life, and calculates the total construction costs for both materials, including maintenance, repair, environmental, and social costs.

## Features

-   **Cost Comparison**: Compare construction, maintenance, repair, demolition, environmental, social, and user costs for Steel vs. Concrete.
-   **Dynamic Inputs**: Users can input values for span length, bridge width, traffic volume, and design life.
-   **Data Visualization**: The application generates a bar chart to visualize the cost comparison and a table for detailed cost breakdown.
-   **Exportable Data**: Users can export the generated bar chart as a PNG image.
-   **SQLite Database**: The application uses an SQLite database to store cost data for both materials (Steel and Concrete).

## Prerequisites

To run the `BridgeCostApp`, ensure you have the following installed:

-   Python 3.x
-   PyQt5
-   SQLite3
-   Matplotlib
-   Pandas

You can install the required dependencies using `pip`:

```bash
pip install PyQt5 matplotlib pandas sqlite3

```

## Setup

1.  **Download the Repository**:  
    Clone or download the project repository to your local machine.
    
2.  **Run the Application**:  
    Navigate to the project directory and run the `BridgeCostApp.py` script.
    
    ```bash
    python BridgeCostApp.py
    
    ```
    
3.  **Database Initialization**:  
    On the first run, the app will automatically create the SQLite database file `Bridge_cost.db` in the same directory if it does not already exist. The database will contain initial cost data for **Steel** and **Concrete**.
    

## Usage

### 1. **Input Parameters**:

The following fields are provided for the user to input:

-   **Span Length**: The length of the bridge span (in meters or preferred units).
-   **Width**: The width of the bridge (in meters or preferred units).
-   **Traffic Volume**: The average daily traffic (vehicles/day).
-   **Design Life**: The expected design life of the bridge in years.

### 2. **Cost Calculation**:

Once the user inputs all the necessary parameters, click the **"Calculate Costs"** button. The app will:

-   Calculate the costs for both materials (Steel and Concrete).
-   Display the results in a table and a bar chart.

### 3. **Exporting the Results**:

After generating the results:

-   You can export the bar chart by clicking the **"Export as PNG"** button.
-   The exported chart will be saved as a PNG file.

## Database Structure

The application uses an SQLite database named `Bridge_cost.db` to store cost data. It contains a table `cost_data` with the following columns:

Column Name

Data Type

Description

**Material**

TEXT

Type of material (Steel or Concrete)

**BaseRate**

REAL

Base construction rate per unit area for the material

**MaintenanceRate**

REAL

Maintenance cost rate per unit area

**RepairRate**

REAL

Repair cost rate per unit area

**DemolitionRate**

REAL

Demolition cost rate per unit area

**EnvironmentalFactor**

REAL

Environmental impact factor per unit area

**SocialFactor**

REAL

Social cost factor per unit area

**DelayFactor**

REAL

Delay cost factor per vehicle and year

The app will automatically initialize the database and populate it with initial values for **Steel** and **Concrete** when you first run it.

## Screenshots

### 1. **Main Window**

The main window contains three panels — one for input fields, one for the cost comparison chart, and one for the cost breakdown table.

<a href="https://ibb.co/DMYkvrS"><img src="https://i.ibb.co/7pQVZk6/image.png" alt="image" border="0"></a>

### 2. **Cost Comparison Bar Chart**

A bar chart showing the comparison between Steel and Concrete for each cost category (Construction, Maintenance, etc.).
<a href="https://ibb.co/wZtgYGj"><img src="https://i.ibb.co/dsZM7Cx/image.png" alt="image" border="0"></a>

### 3. **Cost Breakdown Table**
A table showing the calculated costs for both Steel and Concrete.
<a href="https://ibb.co/8B1Y8Vb"><img src="https://i.ibb.co/z5q6fwF/image.png" alt="image" border="0"></a>

[Video of Result](https://drive.google.com/file/d/1X6E99oSJN7qGEfIAoOO0UienF7TiCxcC/view?usp=drive_link)



----------
