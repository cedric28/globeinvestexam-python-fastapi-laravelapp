import pandas as pd
import random
from datetime import datetime

# sample data
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports', 'Toys']
store_locations = ['Cavite', 'Laguna', 'Batangas', 'Bataan', 'Tarlac']
product_names = ['Product1', 'Product2', 'Product3', 'Product4', 'Product5']

# date range
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start_date, end_date).tolist()

# Generate data
data = []
for date in date_range:
    for _ in range(random.randint(10, 20)):  # Random number of sales per day
        product = random.choice(product_names)
        category = random.choice(categories)
        store = random.choice(store_locations)
        price = round(random.uniform(10, 500), 2)
        quantity_sold = random.randint(1, 20)
        data.append([date, product, category, price, quantity_sold, store])

# create a pandas data frame then save to CSV 
df = pd.DataFrame(data, columns=['Date', 'ProductName', 'Category', 'Price', 'QuantitySold', 'StoreLocation'])
df['ProductID'] = df['ProductName'].apply(lambda x: product_names.index(x) + 1)
df.to_csv('sales_report_data.csv', index=False)
