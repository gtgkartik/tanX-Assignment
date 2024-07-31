# Orders Analysis Application
## Demo Video



https://github.com/user-attachments/assets/b2699b05-06c0-4795-a741-a72aac5d299b


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

# Results 
![image](https://github.com/user-attachments/assets/838b8dd1-4ceb-434f-8c94-ac53df185fe1)

![image](https://github.com/user-attachments/assets/a22fc187-284e-4d7d-8c2f-b7f477d5cdf0)

![image](https://github.com/user-attachments/assets/215e5ca5-14bb-4c9f-b3de-be04c9f6d67a)

![image](https://github.com/user-attachments/assets/a156360a-e576-4d76-a5e7-8f55f0d9e671)

# Testing Results
![image](https://github.com/user-attachments/assets/a9137290-35a7-48f1-b6fe-68336150a7db)


# Using Docker Swarm 

```sh 
     docker swarm init
```

```sh 
    docker stack deploy -c docker-compose.yml orders_app
```

```sh 
    docker stack services orders_app
```
### scale out using  docker swarm
```sh 
    docker service scale orders_app_app=3
```
### check status of services
```sh
    docker stack services orders_app
```

### Running tests 
```sh 
docker build -f Dockerfile.test -t orders_test .


