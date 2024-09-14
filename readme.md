
# Django User CRUD API
This is User CRUD API built with python Django framework. Mysql is used as a databse.


## Setup

Make sure to have python installed. Check if it is installed or not with below command.

```bash
  python --version
```
Create Virtual Environment & activate it

```bash
  python -m venv <myenvname>
  cd <myenvname>
  Scripts\activate
```
Install necessary dependencies with requirements.txt
```bash
  pip install -r requirements.txt
```
Pull this project
```bash
  git pull https://github.com/Dnyanesh-Bachhav/Django-User-API.git
```
Switch to project directory
```bash
  cd newApp
```

Start server
```bash
  python manage.py runserver
```
If changed in models migrate changes and rerun server
```bash
  python manage.py makemigrations
  python manage.py migrate
```

## Routes in API

**Client Routes:**

**GET api/clients/**

- Description: Fetch the list of all clients.
**POST api/clients/**

- Description: Create a new client.

**GET api/clients/{id}/**

- Description: Retrieve the details of a specific client along with projects assigned to that client.
**PUT api/clients/{id}/**

- Description: Update the full information of a specific client.

**PATCH api/clients/{id}/**
- Description: Partially update the information of a specific client.

**DELETE api/clients/{id}/**
- Description: Delete a specific client.

**Project Routes:**

**POST api/clients/{client_id}/projects/**

- Description: Create a new project for a specific client and assign users to the project.

**GET api/projects/**
- Description: Retrieve a list of all projects assigned to the logged-in user.

## All Set! ✨

And there you have it — the project is up and running like a rocket! 🚀✨

Time to sit back, code, and enjoy the magic of programming. 😎💻

Happy coding, folks! 😄🔧

