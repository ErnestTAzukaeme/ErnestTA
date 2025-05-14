# -*- coding: utf-8 -*-
"""
Tj Azukaeme

Amamzon Sales Analysis Porject 
"""

import pandas as pd

#Load the sales data form excel file itno Pandas Dataframe
sales_data=pd.read_excel("C:\\Users\\tejir\\Downloads\\Amazon+Sales+Project (1)\\Amazon Sales Project\\sales_data.xlsx")
# =============================================================================
# Exploring our data 
# =============================================================================
#summary of sales data
sales_data.info()
sales_data.describe()

#exploring the data type 
sales_data.dtypes
#displaying the first few rows of data 
print(sales_data.head())

# =============================================================================
# Cleaning the data 
# =============================================================================


print(sales_data.isnull().sum())

sales_data_dropped=sales_data.dropna()

sales_data_cleaned= sales_data.dropna(subset=['Amount'])

print(sales_data_cleaned.isnull().sum())

# =============================================================================
# Slicing and Filterign Data 
# =============================================================================
#Splitting the data based on the categroy column
category_data = sales_data[sales_data['Category'] == 'Top']
print(category_data)
#Splitting it based on the amount Being bigger than 1000
high_amount_data = sales_data[sales_data['Amount']>1000]
print(high_amount_data)
#Splitting the data based on two conditions
filtered_data=sales_data[(sales_data['Category']=='Top') & (sales_data['Qty'] == 3)]
print(filtered_data)

# =============================================================================
# Aggregating Data
# =============================================================================

#Total Sales by category
category_totals = sales_data.groupby('Category')['Amount'].sum()
category_totals = sales_data.groupby('Category',as_index=False)['Amount'].sum()
category_totals = category_totals.sort_values('Amount',ascending = False)

#calculate the average amount by Category and Fufillment
Fufillment_avg=sales_data.groupby(['Category','Fulfilment'],as_index=False)['Amount'].mean()
Fufillment_avg=Fufillment_avg.sort_values('Amount',ascending=False)     

#calculate average by category and status   
Status_avg=sales_data.groupby(['Category','Status'],as_index=False)['Amount'].mean()
Status_avg=Status_avg.sort_values('Amount',ascending=False)  

#Total Sales by Shipment and Fufilment 
Total_Sales_ShipandFul=sales_data.groupby(['Courier Status','Fulfilment'],as_index=False)['Amount'].sum()
Total_Sales_ShipandFul=Total_Sales_ShipandFul.sort_values('Amount',ascending=False)               
Total_Sales_ShipandFul.rename(columns={'Courier Status':'Shipment'}, inplace=True)            

# =============================================================================
# Exporting The Data 
# =============================================================================
Status_avg.to_excel("average_sales_by_Catgeory_and_status.xlsx", index =False)
Total_Sales_ShipandFul.to_excel("Total_sales_by_ship_and_ful.xlsx",index = False)