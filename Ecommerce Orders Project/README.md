# E-commerce Orders Analysis

## Introduction
This project examines Olist’s e-commerce data to reveal payment patterns and monthly trends. Using Python and pandas, we merged order, payment and customer tables, cleaned the data, and built visualizations for strategic insights.

## Background
Olist maintains three exports from its platform:
- **orders.xlsx**: purchase records  
- **order_payment.xlsx**: payment details  
- **customers.xlsx**: buyer demographics  

The objectives were to:
1. Clean and merge all three datasets  
2. Explore payment behaviors by method and customer  
3. Track total payment value over time

## Data Processing Steps

### 1. Data Import & Exploration
- Loaded each Excel file into a pandas DataFrame  
- Inspected column types, row counts, and null values  

### 2. Data Cleaning
- Dropped duplicate rows in all tables  
- Parsed date columns to `datetime64`  
- Filled or removed any remaining nulls  
- Merged tables on `order_id` and `customer_id` to form a single `joined_data`  

### 3. Feature Engineering
- Extracted `month_year`, `week_year`, and `year` from purchase timestamps  
- Flagged “Invoiced” orders and high-value credit-card payments (> \$1,000)  

## Analysis & Visualizations

- **Time Series**:  
  - Aggregated total payment value by `month_year`  
  - Line chart revealing steady month-over-month growth  

- **Payment Behavior**:  
  - Calculated average payment value by `payment_type`  
  - Compared credit-card vs. boleto averages  

- **Customer Scatter**:  
  - Plotted total payment value vs. installments per customer  
  - Identified clusters of heavy-use customers  

- **Payment Type Breakdown**:  
  - Stacked bar chart of payment value by method across months  
  - Box plots comparing value distributions by payment type  

## Key Results
- Merged ~50 K orders with ~49 K payments and ~40 K customer records, fully cleaned.  
- **73.9 %** of payments were made by credit card, averaging **\$163.32** per order.  
- Boletos averaged **\$145.03** per order.  


## Files
- **ecom_project.py** — main Python script for data cleaning, analysis, and visualization  
- **orders.xlsx** — raw order data  
- **order_payment.xlsx** — raw payment data  
- **customers.xlsx** — raw customer data  
- **[Plots](https://github.com/ErnestTAzukaeme/ErnestTA/tree/da4100338c67c8ccbd71843e6dc5434f48f2a99c/Ecommerce%20Orders%20Project/My%20Plots)** — Visualizations 
 
