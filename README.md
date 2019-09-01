# Django-demo
Summaried guide to using python's django framework, taken from django tutorial

## Table of Content
- [Getting Started](#getting-started)
	- [Framework Overview](#overview)
	- [Installation](#installation)
		- [Installing Django](#installing-django)
		- [Create New Project](#create-new-project)
		- [Create New Application](#create-new-application)
	- [Configure Project](#configure-project)
		- [Database Setup](#database-setup)
		- [Register Application](#register-application)
- [Using Django](#using-django)
	- [Create Model](#create-model)
		- [Create Migration File](#create-migration-file)
		- [Migrate Models](#migrate-models)
	- [Create View](#create-view)
		- [Create New Views](#create-new-views)
		- [Register Views To application URLS](#register-views-to-application-urls)
		- [Register Application Views to project URLS](#register-application-views-to-project-urls)
	- [Create Template](#create-template)
		- [Using Code Block](#using-code-block)
		- [Extending Template](#extending-template)
	- [Django Admin](#django-admin)
		- [About](#about)
		- [#Getting Started](#getting-started-with-django-admin)
			- [Create Super User](#create-a-super-user)
			- [Register Application to Admin Interface](#register-application-to-admin-interface)
	
## Getting Started
### Overview
#### About Django
Django is a MVT (**M**odel-**V**iew-**T**emplate) where:

- Model is where the framework interacting with the database (write query to be executed)
- View is where the data taken from model is manipulated
- Template is how the data is presented to the end user

##### MVT Example
	For the index page listing products to be rendered: 
	- The framework first get data (queried by the Model), 
	- Passed it to the View (to break them into parts), 
	- And continue to passed it to the Template, where it is displayed in a segmented list with link to the next/previous part
	
##### Django: Project vs. Application
An application is a web application with specific purpose (showing website content, managing website content, showing website traffic, ...) 

A project is a collection of application

In summary, an application is a module of a website (project)

### Installation

#### Presiquite
- Python 3.x
- Pip

#### Installing Django
In terminal:

	# pip install Django

### Create New Project
In terminal, `cd` to project root directory

	# django-admin startproject [project name]
	
### Create New Application
In terminal, `cd` to [project name] directory

	# python manage.py startapp [app name]

### Configure Project
Edit file `settings.py` in the [project name] **submodule** directory
#### Database Setup
Edit the `DATABASES` section in `settings.py`

**Database Engine**
The project use which type of database
- django.db.backends.sqlite3
- django.db.backends.postgresql
- django.db.backends.mysql
- django.db.backends.oracle
- ...

**User**: database user

**Password**: database user's password

**Host**: database host

#### Register Application
Edit the `INSTALLED_APPS` section in `settings.py`

Add the [app name] element to the `INSTALLED_APPS` array

# Using Django
## Create Model
Edit file `models.py` in [app name] directory

````python
from django.db import models

class TABLE_1 (models.Model):
	FIELD_NAME = models.DATA_TYPE(CONSTRAINT)
	FIELD_NAME =  models.DATA_TYPE(CONSTRAINT)
	
	def __str__(self): 
		#model toString() function
		return self.FIELD_NAME1 + ' ' + self.FIELD_NAME2
	
class TABLE_2 (models.Model):
	FIELD_NAME = models.DATA_TYPE(CONSTRAINT)
	FIELD_NAME =  models.DATA_TYPE(CONSTRAINT)
	FOREIGN_KEY = models.ForeignKey(ANOTHER_MODEL, CONSTRAINT)
	
	def custom_model_function(self):
		# messing with data directly in model instead of through view
		return self.FIELD_NAME2+ len(FIELD_NAME1)
````

### Create Migration File
In terminal, `cd` to [project name] directory

	# python manage.py makemigrations [app name]

### Migrate Models
In terminal, `cd` to [project name] directory

	# python manage.py migrate

## Create View

### Create New Views
Edit the `views.py` in [app name] directory

````html
from django.shortcuts import get_object_or_404, render
from .models import [models to be imported]

def index(request):
    data_set = MODEL.QUERY
    context = {
		'TEMPLATE_VARIABLE': data_set,
		'TEMPLATE_VARIABLE2': 'hello_world',
		}
    return render(request, '[app_name]/TEMPLATE.html', context)

def get_specific_row(request, MODEL_PK):
	data_set = get_object_or_404(MODEL, pk = MODEL_PK)
	return render(request, '[app_name]/TEMPLATE.html', {'TEMPLATE_VARIABLE':data_set})
````

### Register Views To application URLS
Edit the `urls.py` in [app name] directory

````python
from django.urls import path

from . import views

app_name = '[app_name]'
urlpatterns = [
    # ex: /APP_NAME/
    path('', views.index, name='index'),
    # ex: /APP_NAME/5/
    path('<int:MODEL_PK>/', views.VIEW_NAME, name='REFERENCE_NAME'),
]
````
where:

- APP_NAME = namespace for URLS in an application (for another application to refer to this application's view)
- VIEW_NAME = function in `views.py`
- REFERENCE_NAME = name for the template to refer to the view in URL 
- \<int:MODEL_PK\> = parameter to be passed into view from URLS (E.g: GET request)

**Example**

2 applications: CART and PRODUCT

a CART object holds multiple PRODUCTs

in CART's index view, it refer to each PRODUCT detail view

````html
<a href="{% url 'PRODUCT:detail' PRODUCT.id %}">{{ PRODUCT.name }}</a>
````

here:

- APP_NAME = PRODUCT
- REFERENCE_NAME = detail
- MODEL_PK = PRODUCT.id

### Register Application Views to Project URLS
Edit the `[project name]/urls.py` file

````python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('[app_name]/', include('[app_name].urls')),
    path('admin/', admin.site.urls),
]
````
## Create Template
Create a directory named **templates** and a subdirectory [app_name] in [app_name] directory

````sh
# pwd
[project name]/[app_name]
# mkdir -p templates/[app_name]
````
create html files with names matched the TEMPLATEs references in each view

### Extending Template
#### Using Code Block

** IF block **

{% if condition1 %}
	result1
{% elif condition2 %}
	result2
{% else %}
	result3
{% endif %}

** FOR block **

{% for entry in TEMPLATE_VARIABLE %}
	do something
	
{% endfor %}

#### Template Inheritance/Override
In `parent_template.html`:

````html
<!doctype html>
<html lang="en">
  <head>
    <title>{% block title %} default title {% endblock %}</title>
  </head>
  <body>
    <div id = 'container-fluid'>
        {% block content %}
        default content
        {% endblock %}
    </div>
  </body>
</html>
````

In `child_template.html`:

````html
<!-- extending from base template -->
{% extends '[app_name]/base.html' %}

<!-- overriding [title] block -->
{% block title %} Overrided Title {% endblock %}

<!-- overriding [content] block -->
{% block content %}
Overrided content
{% endblock %}
````

## Django Admin
### About
Django Admin is the administrative interface of the whole Django **project**, it is included in the `INSTALLED_APPS` of the project `settings.py` by default

### Getting Started With Django Admin
#### Create A Super User
In terminal, `cd` to [project name] directory

	# python manage.py createsuperuser
	
Enter prompted information

````
Username: [admin username]
Email address: [admin email]
Password: [admin password]
Password (again): [retype password]
Superuser created successfully.
````

#### Register Application To Admin Interface
Edit the `admin.py` in [app name] directory

````python
from django.contrib import admin

from .models import [models to be registered]

admin.site.register(MODEL_NAME)
````
