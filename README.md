# django-app-project2

This is the second formal project after django practice

## Run Locally

**OS**: Ubuntu  
**Editor**: Visual Studio Code

Clone the project

```bash
git clone git@github.com:noumanrafi0/django-app-project2.git
```

Go to the project directory

```bash
cd my-cd django-app-project2/
code .
```

Install environment and activate

```bash
python3 -m venv env
source env/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

Make log directory, make migrations, migrate and runserver

```bash
mkdir log
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

### TASK 3

A Complete Django Application with Custom User Model, Custom Authentication Middleware, Auto Populate any field in the User Model that will be generated automatically on the save method call

### TASK 3.1

Create custom middleware logging user's IP and request information in txt file with proper formatting
