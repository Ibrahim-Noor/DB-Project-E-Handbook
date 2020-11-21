# DB-Project-E-Handbook
your sql db should have a name "djangoRawSQL"
All the library requirements are written in requirements.txt file.
If you face the error "mysqlclient 1.4.0 or newer is required". Go into your virtual environment folder eg. env and then go to lib/python3.8/site-packages/django/db/backends/mysql/base.py and change the follwoing lines

if version < (1, 4, 0):
  raise ImproperlyConfigured('mysqlclient 1.4.0 or newer is required; you have %s.' % Database.__version__)
  
to this 
if version < (1, 4, 0):
	pass
  
and then run again, your issue would be solved.
