# CRM System using Python Django and MySQL

This is a CRM (Customer Relationship Management) system built using Python Django and MySQL. It provides basic functionalities such as login, adding records, updating records, and deleting records.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Python 3.x
* pip
* MySQL Server

### Installing
1. Clone the repository

``` git clone https://github.com/your_username/crm-system.git ```

2. Install requirements

``` pip install -r requirements.txt ```

3. Create a MySQL database and update the settings in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_username',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4. Run migrations

` python manage.py migrate `

5. Create a superuser

` python manage.py createsuperuser `

6. Start the development server

` python manage.py runserver`


## Usage

1. Login using the credentials of the superuser created in step 5 of the installation.

2. Navigate to the records page and add records by clicking the "Add Record" button.

3. Update or delete records by clicking the respective buttons next to the records.

### Built With
* Python - Programming language 
* Django - Web framework
* MySQL - Relational database management system

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
* Django documentation
* Bootstrap - Front-end framework
