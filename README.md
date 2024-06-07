# Marrisa

## Requirements

To run the code in this project, you need:

Python 3.12 or later

## Installation

### Installing Poetry

#### Mac

🍎 To install Poetry on macOS, you can use the following command in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Linux

🐧 To install Poetry on Linux, you can use the following command in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python -
```

#### Windows

💻 To install Poetry on Windows, you can use the following command in PowerShell:

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org/install.ps1 -UseBasicParsing).Content | python
```

verify installation

```bash
poetry --version
```

📦 For more detail about installation you can follow the instructions in the [official documentation](https://python-poetry.org/docs/#installation).

### Installing Dependencies

🛠️ After installing Poetry, navigate to the project directory

```bash
cd marrisa
```

and run the following command to install dependencies:

```bash
poetry install
```

## Running migration

🚀 To run database migration, following these step:

### 1. Configure Alembic

Edit alembic.ini file to set your database URL, find this in line 63

```bash
sqlalchemy.url = postgresql://user:password@localhost/dbname

```

### 2. Create a new migration

run this command

```bash
alembic revision --autogenerate -m "Initial migration"
```

### 3. Apply the migration:

run this command

```bash
alembic upgrade head
```

if you are getting error like this

```bash
LINE 3:  id UUID DEFAULT uuid_generate_v4() NOT NULL,
                         ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
```

try to enable the uuid-ossp Extension in PostgreSQL.

Connect to your PostgreSQL database and run these sql command:

```bash
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

## Running the Project

### Using Uvicorn

🚀 To run the project with Uvicorn, use the following command:

```bash
uvicorn main:app
```

### Using FastAPI Command

💨 Alternatively, you can use the FastAPI command to run the project:

```bash
fastapi dev main.py
```

## Accessing the Application

🌐 Once the project is running, you can access the application at:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Documentation and CRUD Operations

📝 To view the API documentation and perform CRUD operations, visit:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## To test the APIs

🧪 In this page - [http://127.0.0.1:8000/docs] you will see all the endpoints.
You can click on any endpoint and then click on "Try it out" to test the API.
