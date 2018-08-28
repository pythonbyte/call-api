# Work at Olist - Call API

# Description

This project is a challenge for a job opening in Olist. It's like a Call Receiver, the API will receive Start Calls and End Calls and the API will return the bills of subscribers number, accordingly with the period sent as parameter.

# Installing

First step of installation is having Pipenv installed in your machine, if you doesn't have just use the below command:

``` $ pip install pipenv ```

Now after cloned the repository all you need to do is:

```
$ cd callapi/
$ pipenv install
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Remember that if there is no intention to use Heroku, need to comment dj_database_url in settings, the line in the bottom with dj_database as well and set your own database before migrate.

# Testing

To test the application use:
```
$ python manage.py test
```

# Work Enviroment

* **Computer**         - Dell Inspiron 15
* **Operating System** - Linux manjaro 4.14.65-1-MANJARO
* **Text Editor**      - Sublime Text v3.1.1
* **Python** - 3.7.0
* **Django** - 2.1 
* **djangorestframework** - 3.8.2
