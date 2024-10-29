# Task Management API

This project provides a simple Task Management API built with Django and Docker.

## Getting Started

### Prerequisites

Ensure you have Docker and Docker Compose installed on your machine.

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/pawansapkota100/task-management.git
   ```
2. **Copy Environment Variables**  
   First, copy the `env.sample` file to `.env`:

   ```bash
   cp env.sample .env
   ```

3. **Add Data to the `.env` File**  
   Open the `.env` file and add your environment-specific data.

4. **Build and Run the Docker Containers**  
   Use the following commands to build and start the application:

   ```bash
   docker-compose build
   docker-compose up
   ```

   Your server will run at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Running Tests

To run the test cases for the application, use the following command:

```bash
docker exec -it task_management-web-1 python manage.py test
```

## API Endpoints

### View Created Tasks

- **GET** request to retrieve the tasks created by the user:
  http://127.0.0.1:8000/tasks/

### Retrieve a Specific Task

- **GET** request to retrieve a specific task by ID:
  http://127.0.0.1:8000/tasks/1/

### Create a New Task

- **POST** request to create a new task:
  http://127.0.0.1:8000/tasks/

### Mark a Task as Complete

- **POST** request to mark a specific task as complete:
  http://127.0.0.1:8000/tasks/9/complete/

### Update a Task

- **PATCH** request to update a specific task:
  http://127.0.0.1:8000/tasks/7/

### Delete a Task

- **DELETE** request to delete a specific task:
  http://127.0.0.1:8000/tasks/8/

### Filter Tasks by Priority and Status

- **GET** request to filter tasks based on priority and status:
  http://127.0.0.1:8000/tasks/?status=I&priority=H

### Search for a Task by Name

- **GET** request to search for a task by name:
  http://127.0.0.1:8000/tasks/?search=testing%20task
