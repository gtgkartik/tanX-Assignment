# Orders Analysis Application

### Prerequisites
- Docker
- Docker Compose

### Build and Run
To build and run the application:

1. Clone the repository:
   ```sh
   git clone https://github.com/gtgkartik/tanX-Assignment.git
   cd tanX-Assignment
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