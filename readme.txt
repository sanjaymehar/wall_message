For running project

1-install python
2-pip-
  1 python -m pip install Django
  2 python -m pip install djangorestframework

3-Go to project directory :
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

End points

1-'http://127.0.0.1:8000/admin/' for admin access
2-'http://127.0.0.1:8000/createuser/' for register new user
3-'http://127.0.0.1:8000/all/' for getting all message 
4-'http://127.0.0.1:8000/craetewall/' for creating message data for only Authenticated(registered user)
5-'http://127.0.0.1:8000/updateewall/<int:pk>' for updating specific message for only Authenticated(registered user) + only owner of specfic message can update that message
6-'http://127.0.0.1:8000/deleteewall/<int:pk>' for delete specific message for only Authenticated(registered user) + only owner of specfic message can delete that message
7-'http://127.0.0.1:8000/getdata/<int:pk>' for getting single specific message (guest and registered user)
8-'http://127.0.0.1:8000/api-auth/login' for login 
8-'http://127.0.0.1:8000/api-auth/logout' for logout 


superuser 
username = admin
password = admin

