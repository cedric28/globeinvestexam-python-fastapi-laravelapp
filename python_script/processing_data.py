import pandas as pd
import sqlite3
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sales_data.db')

# load data to csv
df = pd.read_csv('sales_data.csv')

# convert date column  data to datetime
df['Date'] = pd.to_datetime(df['Date'])

# create new TotalSale column which is the product of Price and QuantitySold
df['TotalSale'] = df['Price'] * df['QuantitySold']

df.head()
# Generate a summary report showing total sales per category
category_sales = df.groupby("Category")["TotalSale"].sum().reset_index()

# Find the top 3 best-selling products in each StoreLocation
top_products = df.groupby("StoreLocation")["ProductName"].value_counts().head(3)

print(category_sales)
print(top_products)

#connect  to database
conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()

# Create tables for Sales and Products
cursor.execute("""
    CREATE TABLE Sales (
        Date DATE,
        ProductID INTEGER,
        ProductName TEXT,
        Category TEXT,
        Price REAL,
        QuantitySold INTEGER,
        StoreLocation TEXT,
        TotalSale REAL
    );
""")

cursor.execute("""
    CREATE TABLE Products (
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT
    );
""")

# Insert data into Sales table
df.to_sql("Sales", conn, if_exists="replace", index=False)

# Insert data into Products table
products_df = df[["ProductID", "ProductName"]].drop_duplicates()
products_df.to_sql("Products", conn, if_exists="replace", index=False)

#commit then close
conn.commit()
conn.close()
