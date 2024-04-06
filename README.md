Telecom Customer Management System
This is a Django project to manage customers and plans for a telecom company.

Features
Manage customers - add, view, update, delete
Manage plans - add, view, update, delete
Assign plans to customers
Manage customer plan status and renewals
Usage
Install dependencies
pip install -r requirements.txt



Run migrations
python manage.py makemigrations
python manage.py migrate



Run development server
python manage.py runserver



The app will be available at http://127.0.0.1:8000

The admin interface can be accessed at http://127.0.0.1:8000/admin

Run tests
python manage.py test



API Endpoints
The API includes the following endpoints

apicustomers - CRUD for customers
apiplans - CRUD for plans
apicustomerplans - CRUD for customer plans
Tech Stack
Django
Django REST Framework
SQLite database