# -*- coding: utf-8 -*-
"""
Created on Thu May 15 10:49:06 2025

@author: tejir
"""

import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
#read the Excel Files

pizza_sales_df = pd.read_excel('C:/Users/tejir/Downloads/Pizza+Sales+Project (1)/Pizza Sales Project/pizza_sales.xlsx')
pizza_size_df=pd.read_csv('C:/Users/tejir/Downloads/Pizza+Sales+Project (1)/Pizza Sales Project/pizza_size.csv')
pizza_category_df = pd.read_csv('C:/Users/tejir/Downloads/Pizza+Sales+Project (1)/Pizza Sales Project/pizza_category.csv')

# Describe and inspect the DataFrame
print(pizza_sales_df.describe())
print(pizza_sales_df.info())

# Count nulls and duplicates
null_counts = pizza_sales_df.isnull().sum()
dup_count = pizza_sales_df.duplicated().sum()
print(f"Null values per column:\n{null_counts}")
print(f"Total duplicate rows: {dup_count}")

# Select columns and rows
quantity_col = pizza_sales_df['quantity']
selected_cols = pizza_sales_df[['order_id', 'quantity', 'unit_price']]
row_3 = pizza_sales_df.loc[3]
rows_3_5 = pizza_sales_df.loc[[3, 5]]
subset_rows = pizza_sales_df.loc[3:5]
subset_rows_cols = pizza_sales_df.loc[3:5, ['quantity', 'unit_price']]

# Set and reset index
pizza_sales_df.set_index('order_details_id', inplace=True)
pizza_sales_df.reset_index(inplace=True)

# Truncate rows before and after
truncated_before = pizza_sales_df.truncate(before=3)
truncated_after = pizza_sales_df.truncate(after=5)

# Truncate a Series of quantity
quantity_series = pizza_sales_df['quantity']
trunc_q_before = quantity_series.truncate(before=3)
trunc_q_after = quantity_series.truncate(after=5)

# Basic filtering
gte_20 = pizza_sales_df[pizza_sales_df['unit_price'] > 20]

# Filter by date
pizza_sales_df['order_date'] = pd.to_datetime(pizza_sales_df['order_date']).dt.date
date_target = datetime.datetime.strptime('2015-12-15', '%Y-%m-%d').date()
after_target = pizza_sales_df[pizza_sales_df['order_date'] > date_target]

# Filtering on multiple conditions
bbq_and = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) &
                         (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]
bbq_or = pizza_sales_df[(pizza_sales_df['unit_price'] > 20) |
                        (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

# Filter a specific range
high_sales = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) &
                             (pizza_sales_df['unit_price'] <= 20)]

# Dropping null values and replacing
dropped_nulls = pizza_sales_df.dropna()
nulls_after_drop = dropped_nulls.isnull().sum()
date_fill = datetime.datetime.strptime('2000-01-01', '%Y-%m-%d').date()
filled = pizza_sales_df.fillna(date_fill)

# Deleting rows and columns
deleted_rows = pizza_sales_df.drop([5, 7, 9], axis=0)
deleted_unit = pizza_sales_df.drop('unit_price', axis=1)
deleted_multi = pizza_sales_df.drop(['unit_price', 'order_id'], axis=1)

# Sorting
total_sorted_asc = pizza_sales_df.sort_values('total_price')
total_sorted_desc = pizza_sales_df.sort_values('total_price', ascending=False)
sorted_multi = pizza_sales_df.sort_values(['pizza_category_id', 'total_price'], ascending=[True, False])

# Grouping and aggregation
count_per_size = pizza_sales_df.groupby('pizza_size_id')['total_price'].count()
sum_per_size = pizza_sales_df.groupby('pizza_size_id')['total_price'].sum()
sales_per_size = pizza_sales_df.groupby('pizza_size_id')[['total_price', 'quantity']].sum()
agg_example = pizza_sales_df.groupby('pizza_size_id').agg({'quantity': 'sum', 'total_price': 'sum'})

# Merging lookup tables and concatenating
merged1 = pizza_sales_df.merge(pizza_size_df, on='pizza_size_id')
merged2 = merged1.merge(pizza_category_df, on='pizza_category_id')
another_df = pd.read_excel('another_pizza_sales.xlsx')
vert_concat = pd.concat([pizza_sales_df, another_df], axis=0)
voucher_df = pd.read_excel('pizza_sales_voucher.xlsx')
horz_concat = pd.concat([pizza_sales_df, voucher_df], axis=1)

# Converting case for ingredients
lower_text = pizza_sales_df['pizza_ingredients'].str.lower()
upper_text = pizza_sales_df['pizza_ingredients'].str.upper()
title_text = pizza_sales_df['pizza_ingredients'].str.title()

# Replacing text values
replaced = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')
pizza_sales_df['pizza_ingredients'] = replaced

# Stripping extra whitespace in names
pizza_sales_df['pizza_name'] = pizza_sales_df['pizza_name'].str.strip()

# Boxplot of total sales by category
sns.boxplot(x='category', y='total_price', data=merged2)
plt.xlabel('Pizza Category')
plt.ylabel('Total Sales')
plt.title('Boxplot showing distribution of sales by category')
plt.show()

