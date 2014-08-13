Readme for Django Rest quickstart:

Resources:
http://www.django-rest-framework.org/tutorial/quickstart#quickstart

TODO:
1. Create database in MySQL and update settings.py
2. The first time running python manage.py syncdb, be sure to create a user/password for authenticate to the django rest framework
3. Use Postman or CURL to accees the url.  Be sure to include the username/password:
   CURL:  curl http://localhost:8000/users/ -u appuser:test

   Postman:
	    url: http://localhost:8000/users/
	    basic auth: appuser/test


