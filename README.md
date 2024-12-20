# phase_3_project
By Zuruel Kamande

Database Management with Alembic and CRUD Operations

Overview

This project demonstrates effective database management using Alembic for schema migrations and Python for CRUD operations. The application manages three interconnected entities: Agents, Players, and Performances. It uses SQLite as the database backend for simplicity and portability.

Features

CRUD Operations: Full Create, Read, Update, and Delete functionality for all database tables.

Database Migrations: Alembic is used for version control and schema management.

Testing: Unit tests ensure the reliability of models and database operations.

Project Structure

project/
|
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│
├── database/
│   ├── connection.py
│   ├── setup.py
│
├── models/
│   ├── base.py
│   ├── agent.py
│   ├── player.py
│   ├── performance.py
│
├── main.py
├── tables.db
├── alembic.ini
├── test_models.py

Key Components

database/connection.py: Provides SQLite database connection.

database/setup.py: Runs Alembic migrations or creates tables directly.

models/: Contains ORM classes for Agents, Players, and Performances.

main.py: Implements the main application logic and CRUD operations.

test_models.py: Contains unit tests for the models and database operations.

Database Schema

Tables

Agents:

id (Primary Key)

name (Text)

Players:

id (Primary Key)

name (Text)

agent_id (Foreign Key -> Agents.id)

Performances:

id (Primary Key)

player_id (Foreign Key -> Players.id)

goals (Integer)

assists (Integer)

status (Text)

Setup Instructions

Prerequisites

Python 3.x

SQLite

Alembic

Installation

Clone the repository:

git clone https://github.com/your-repo/project.git
cd project

Install dependencies:

pip install -r requirements.txt

Run Alembic migrations to set up the database:

alembic upgrade head

Alternatively, create tables manually using:

python database/setup.py

Usage

Run the main application:

python main.py

Interact with the application to create, view, update, and delete records.

CRUD Operations

Example: Create an Agent

agent = Agent(name="John Doe")
agent.save()

Example: Read Agents

agents = Agent.list_all()
for agent in agents:
    print(agent)

Example: Update a Player

player = Player.get_by_id(1)
player.name = "Updated Name"
player.save()

Example: Delete a Performance

Performance.delete_by_id(1)

Testing

Run the tests using:

python -m unittest test_models.py

Ensure all tests pass before deployment.

Alembic Workflow

Initialize Alembic:

alembic init alembic

Generate migration files:

alembic revision --autogenerate -m "Initial migration"

Apply migrations:

alembic upgrade head

Future Enhancements

Extend to a web application using Flask or Django.

Add advanced querying and reporting features.

Implement user authentication and access control.

SLIDES PRESENTATION LINK- https://docs.google.com/presentation/d/12FBhSJI6Zz9TE9NOzB9nmmIROtT-FI84K-1nia1LTGM/edit#slide=id.g2d72135ae38_0_390

License

This project is licensed under the MIT License.