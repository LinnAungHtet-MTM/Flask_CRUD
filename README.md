# Flask Products API

A simple Flask REST API project with **JWT authentication**, **role-based access**, and **SQLAlchemy ORM**.
Supports **user registration**, **login**, **refresh tokens**, and **CRUD operations** for products.

---

## Features

- JWT authentication (Access + Refresh token)
- Role-based authorization (Admin / Guest user)
- Users can only modify their own products
- Admin can modify/delete any product
- SQLAlchemy ORM for database modeling
- MySQL support
- Data validation using Pydantic
- Logging to file (`app.log`)

---

## Tech Stack

- Python 3.10+
- Flask
- Flask-JWT-Extended
- Flask-Migrate
- Flask-SQLAlchemy
- Pydantic
- MySQL / MariaDB
- Poetry (for dependency management)

---

## Setup

1. Clone repository

```bash
git clone https://github.com/LinnAungHtet-MTM/Flask_CRUD.git
cd Flask_CRUD
```

2. Install dependencies

```bash
poetry install
```

3. Copy .env.example to .env

```bash
copy .env.example .env
```

4. Run Application
```bash
poetry run flask run
```
