# Amazon Sales Data Analysis

## Introduction
This project analyzes a merchant’s Amazon sales data to uncover key performance metrics and insights for strategic decision-making. Using Python and pandas, raw sales records were cleaned, filtered, aggregated, and summarized into investor-ready outputs.

## Background
A retail merchant exports their transaction data from the Amazon portal in `sales_data.xlsx`. The merchant needs:
- Identification of **high-value orders** (amounts > \$1,000)
- Performance metrics by **product category** and **order status**
- Total sales breakdown by **shipment method** and **fulfillment type**

## Data Processing Steps
1. **Data Import & Exploration**  
   - Loaded `sales_data.xlsx` into a pandas DataFrame  
   - Reviewed data types, summary statistics, and initial rows  

2. **Data Cleaning**  
   - Dropped all rows with missing `Amount` values to ensure financial accuracy (resulting in 996 complete records)  

3. **Filtering & Segmentation**  
   - Extracted orders with `Amount > 1,000`  
   - Filtered “Top”–category orders with a quantity of 3  

4. **Aggregation & Analysis**  
   - Calculated total sales by **Category**  
   - Computed average sale amount by **Category** and **Status**  
   - Summarized total sales by **Shipment** (Courier Status) and **Fulfilment**  

5. **Export**  
   - Saved summary tables to Excel:  
     - `average_sales_by_Catgeory_and_status.xlsx`  
     - `Total_sales_by_ship_and_ful.xlsx`  

## Key Results
- **Cleaned & analyzed 996 records**: removed all missing `Amount` values for complete data integrity  
- **156 orders** over \$1,000, representing **24.8%** of total revenue  
- Top shipment–fulfillment method (**Delivered + Self-fulfilled**) generated **\$21,750** in sales  

## Files
- `Amazon_Project.py` — Main Python script for cleaning, filtering, aggregation, and export  
- `sales_data.xlsx` — Raw transaction data  
- `average_sales_by_Catgeory_and_status.xlsx` — Average sales by category & status  
- `Total_sales_by_ship_and_ful.xlsx` — Total sales by shipment & fulfillment  
