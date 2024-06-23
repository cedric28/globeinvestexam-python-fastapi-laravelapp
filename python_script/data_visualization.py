import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("sales_data.csv")

# Calculate the total sales for each date
df["Date"] = pd.to_datetime(df["Date"])
df["TotalSale"] = df["Price"] * df["QuantitySold"]
daily_sales = df.groupby("Date")["TotalSale"].sum()

# Save the daily sales data to a CSV file
daily_sales.to_csv("daily_sales.csv", index=True)

# Load the daily sales data
daily_sales = pd.read_csv("daily_sales.csv", index_col="Date")

daily_sales.plot(kind="line")
plt.title("Total Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()