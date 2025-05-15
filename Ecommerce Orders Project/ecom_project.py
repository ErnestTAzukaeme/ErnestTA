# -*- coding: utf-8 -*-
"""
Created on Wed May 14 18:37:04 2025

@author: tejir
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir("C:/Users/tejir")

print(os.getcwd())
# =============================================================================
# Loading Data
# =============================================================================
orders_data=pd.read_excel('C:/Users/tejir/Downloads/Ecommerce+Orders+Project/Ecommerce Orders Project/orders.xlsx')

customer_data=pd.read_excel("C:/Users/tejir/Downloads/Ecommerce+Orders+Project/Ecommerce Orders Project/customers.xlsx")

payment_data=pd.read_excel('C:/Users/tejir/Downloads/Ecommerce+Orders+Project/Ecommerce Orders Project/order_payment.xlsx')

# =============================================================================
# Previewing data
# =============================================================================
orders_data.info()
customer_data.info()
payment_data.info()


orders_data.isnull().sum()
payment_data.isnull().sum()
customer_data.isnull().sum()

orders_data2 = orders_data.fillna('N/A')

orders_data2.isnull().sum()

payment_data=payment_data.dropna()

payment_data.isnull().sum()

# =============================================================================
# Removing duplicate Data
# =============================================================================
orders_data.duplicated().sum()

orders_data=orders_data.drop_duplicates()

payment_data.duplicated().sum()

payment_data=payment_data.drop_duplicates()

# =============================================================================
# Filtering the Data
# =============================================================================
#selecting a subset from order_dataframe based on order stats
invoiced_orders_data = orders_data[
    orders_data['order_status'] == 'Invoiced'
]

invoiced_orders_data = invoiced_orders_data.reset_index(drop=True)
#check a subset of the payments data where payment type = creditc card and payment value >1000
credit_card_payments_data=payment_data[
    (payment_data['payment_type'] == 'credit_card') & (payment_data['payment_value'] > 1000)]
#subset based on customer state = sp
customers_data_state=customer_data[customer_data['customer_state'] == 'SP']

# =============================================================================
# Merge and Join Dataframes
# =============================================================================
merged_data=pd.merge(orders_data,payment_data, on='order_id')


joined_data = pd.merge(merged_data,customer_data,on = 'customer_id')

# =============================================================================
# Data Vizualization
# =============================================================================
joined_data['month_year']= joined_data['order_purchase_timestamp'].dt.to_period('M')
joined_data['week_year']= joined_data['order_purchase_timestamp'].dt.to_period('W')
joined_data['year']= joined_data['order_purchase_timestamp'].dt.to_period('Y')

grouped_data= joined_data.groupby('month_year')['payment_value'].sum()
grouped_data = grouped_data.reset_index()

grouped_data['month_year'] = grouped_data['month_year'].astype(str)

plt.plot(grouped_data['month_year'],grouped_data['payment_value'])

# extract period fields
joined_data['month_year'] = joined_data['order_purchase_timestamp'].dt.to_period('M')
joined_data['week_year']  = joined_data['order_purchase_timestamp'].dt.to_period('W')
joined_data['year']       = joined_data['order_purchase_timestamp'].dt.to_period('Y')

# line plot: total payment_value by month
grouped_data = joined_data.groupby('month_year')['payment_value'].sum()
grouped_data = grouped_data.reset_index()
grouped_data['month_year'] = grouped_data['month_year'].astype(str)

plt.figure(figsize=(10,5))
plt.plot(grouped_data['month_year'], grouped_data['payment_value'], color='red', marker='o')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Month and Year')
plt.ylabel('Payment Value')
plt.title('Payment Value by Month and Year')
plt.xticks(rotation=90, fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()
plt.show()

# Scatter Plot
scatter_df = joined_data.groupby('customer_unique_id').agg({
    'payment_value': 'sum',
    'payment_installments': 'sum'
}).reset_index()

plt.figure(figsize=(8,6))
plt.scatter(scatter_df['payment_value'], scatter_df['payment_installments'])
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value vs Installments by Customer')
plt.tight_layout()
plt.show()

# Seaborn scatter
sns.set_theme(style='darkgrid')
plt.figure(figsize=(8,6))
sns.scatterplot(data=scatter_df,
                x='payment_value',
                y='payment_installments')
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value vs Installments by Customer')
plt.tight_layout()
plt.show()

# Creating a bar chart
bar_chart_df = joined_data.groupby(['payment_type','month_year'])['payment_value'].sum().reset_index()

pivot_data = bar_chart_df.pivot(
    index='month_year',
    columns='payment_type',
    values='payment_value'
)
pivot_data.index = pivot_data.index.astype(str)

plt.figure(figsize=(12,6))
pivot_data.plot(kind='bar', stacked=True, ax=plt.gca())
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Month of Payment')
plt.ylabel('Payment Value')
plt.title('Payment per Payment Type by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Creating a box plot
payment_vals  = joined_data['payment_value']
payment_types = ['credit_card','boleto','voucher','debit_card']

plt.figure(figsize=(8,6))
plt.boxplot(
    [payment_vals[joined_data['payment_type'] == pt] for pt in payment_types],
    labels=['Credit Card','Boleto','Voucher','Debit Card']
)
plt.xlabel('Payment Type')
plt.ylabel('Payment Value')
plt.title('Box Plot showing Payment Value ranges by Payment Type')
plt.tight_layout()
plt.show()

# Creating a subplot (3 plots in one)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10,18))

# ax1: boxplot
ax1.boxplot(
    [payment_vals[joined_data['payment_type'] == pt] for pt in payment_types],
    labels=['Credit Card','Boleto','Voucher','Debit Card']
)
ax1.set_xlabel('Payment Type')
ax1.set_ylabel('Payment Value')
ax1.set_title('Box Plot showing Payment Value ranges by Payment Type')

# ax2: stacked bar chart
pivot_data.plot(kind='bar', stacked=True, ax=ax2)
ax2.tick_params(axis='x', rotation=45)
ax2.set_xlabel('Month of Payment')
ax2.set_ylabel('Payment Value')
ax2.set_title('Payment per Payment Type by Month')

# ax3: scatter
ax3.scatter(scatter_df['payment_value'], scatter_df['payment_installments'])
ax3.set_xlabel('Payment Value')
ax3.set_ylabel('Payment Installments')
ax3.set_title('Payment Value vs Installments by Customer')

plt.tight_layout()
plt.savefig('my_plot.png')
plt.show()