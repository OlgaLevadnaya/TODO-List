**Project name:**

API for TODO List application

**Author of the project:**

Olga Levadnaya

**Description of the project:**

Realization API for **TODO List** application.

**Technologies:**
- Python
- Django
- DRF
- JWT + Djoser


---

**Usage:**
1. Clone the repository to your computer.

2. Deploy and activate virtual environment in the project directory.
```
# Command for Windows:
python -m venv venv
source venv/Scripts/activate

# Command for Linux and macOS:
python3 -m venv venv
source venv/bin/activate
```
3. Install project dependencies:

```
pip install -r requirements.txt
```

4. Apply migrations:

```
# Command for Windows:
python manage.py migrate

# Command for Linux and macOS:
python3 manage.py migrate
```

---

**Available endpoints:**

- *api/v1/tasks/* (GET, POST): getting the list of tasks or creating a new task;

- *api/v1/tasks/{id}/* (GET, PUT, PATCH, DELETE): gettind, editing or deleting the post with identifier **id**;

- *api/v1/categories/* (GET): getting the list of categories;

- *api/v1/categories/{id}/* (GET): gettind a list of tasks in category with identifier **id**.

---

This is the second version of the project. In the second version added authorization and users can see olny their tasks now.

In plans:

- improve the User model (in the first version we redefined User model to have more flexibility);

- include number of days until deadline;

- a simple frontend to everybody can try this app;

- deployment on a remote server.
