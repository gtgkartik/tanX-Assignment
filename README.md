# Orders Analysis Application

## Description
This application performs data analysis on customer orders from an online store. It calculates the total revenue for each month, product, and customer, and identifies the top 10 customers by revenue.

## Setup

### Prerequisites
- Docker
- Docker Compose

### Build and Run

To build and run the application:

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
    ```
2. Build and start the application service:

```sh
    docker-compose up --build app
```
This will start the application and run the orders_analysis.py script.

Run Tests
To build and run the test service:

Build and start the test service:

```sh
docker-compose up --build test
```

This will start the test service and run the unit tests using unittest.