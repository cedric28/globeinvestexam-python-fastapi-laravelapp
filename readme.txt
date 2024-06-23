# Fullstack Developer Interview Exercise

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Running the FastAPI Application

1. Navigate to the `fastapi_app` directory.
2. Build and run the Docker container:
   docker build -t fastapi_app .
   docker run -d -p 80:80 fastapi_app

4. Navigate to the laravel_app directory.
5. Build and run the Docker container:
    docker build -t laravel_app .
    docker run -d -p 8000:80 laravel_app

### To run the python scripts, follow these steps:
1. Generate the dataset using `python generate_data.py`.
2. Load and transform the data using `python processing_data.py`.
3. Store the data in an SQLite database using `python store_data.py`.
4. Data Visualization using `python data_visualization.py`.

API Endpoint
The FastAPI application provides an endpoint /sales-summary to query sales data with the following query parameters:

start_date
end_date
category
store_location

Laravel Integration
The Laravel application fetches data from the FastAPI endpoint and displays it in a user-friendly format on the 'http://localhost:8000/sales-summary' route.