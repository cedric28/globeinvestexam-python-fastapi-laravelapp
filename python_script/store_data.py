import pandas as pd
import sqlite3
import logging
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sales_data.db')
#log info
logging.basicConfig(filename='data_processing.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
# use chunk for large datasets for processing data by batch
chunksize = 1000
conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()

for chunk in pd.read_csv("sales_data.csv", chunksize=chunksize):
    chunk["Date"] = pd.to_datetime(chunk["Date"])
    chunk["TotalSale"] = chunk["Price"] * chunk["QuantitySold"]
    chunk.to_sql("Sales", conn, if_exists="append", index=False)


#commit then close
conn.commit();
conn.close()

