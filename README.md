# Work at Olist - Call API

# Description

This project is a challenge for a job opening in Olist. It's like a Call Receiver, the API will receive Start Calls and End Calls and the API will return the bills of subscribers number, accordingly with the period sent as parameter.

Deployed app at Heroku: https://desolate-fortress-35658.herokuapp.com/

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


# API documentation

This API works with 3 simple endpoints:

## Call Start Endpoint
This endpoint works at the **/call/** , the parameters needed to send to create a Call Start is 'call_id', 'source', 'destination' and 'timestamp'. The 'id' and 'record_type' fields are automatically generated. 
Besides that the source and destination number will only accept 10 or 11 numbers.

Post data:
```
{
    "call_id": 1,
    "source": "99778855443",
    "destination": "9988221132",
    "timestamp": "2018-02-28T21:57:13Z"
}
```
Response data:
```
{
    "id": 1,
    "call_id": 1,
    "record_type": "start",
    "source": "99778855443",
    "destination": "9988221132",
    "timestamp": "2018-02-28T21:57:13Z"
}
```
## Call End Endpoint
This endpoint works at the **/callend/** , the parameters needed to send to create a Call End is 'call_id' and 'timestamp'. The 'id' and 'record_type' fields are automatically generated. 

Post data:
```
{
    "call_id": 1,
    "timestamp": "2018-02-28T22:57:13Z"
}
```
Response data:
```
{
    "id": 1,
    "record_type": "end",
    "call_id": 1,
    "timestamp": "2018-02-28T22:57:13Z"
}
```
The call records are automatically created after a call_start id matches a call_end id.

## Phone Bill Endpoint
This endpoint works at the **/bills/** , the only parameter required is 'subscriber' and you can set 'period' with format 'mm/YYYY' to search for a period of bills for that subscriber. If the period parameter is not sent, the API will return the last closed month bill.
 

Post data:
```
{
    "subscriber": "99988526423",
    "period": "02/2016"
}
```
Works as - /bills/?subscriber=99988526423&period=02/2016

Response data:
```
{
    "subscriber": "99988526423",
    "period": "2/2016",
    "total": "R$ 11,16",
    "bills": [
        {
            "destination": "9993468278",
            "start_date": "2016-02-29",
            "start_time": "12:00:00",
            "duration": "2:00:00",
            "price": "R$ 11,16"
        }
    ]
}
```