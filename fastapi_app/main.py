from fastapi import FastAPI, Query
import sqlite3

app = FastAPI()

@app.get("/sales-summary")
async def sales_summary(
    start_date: str = Query(...),
    end_date: str = Query(...),
    category: str = Query(...),
    store_location: str = Query(...)
):
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    query = """
        SELECT SUM(TotalSale) AS TotalSales, ProductName
        FROM Sales
        WHERE Date BETWEEN? AND?
        AND Category =?
        AND StoreLocation =?
        GROUP BY ProductName
        ORDER BY TotalSales DESC
        LIMIT 3;
    """

    cursor.execute(query, (start_date, end_date, category, store_location))
    results = cursor.fetchall()

    conn.close()

    return {"TotalSales": results[0][0], "TopProducts": [row[1] for row in results]}