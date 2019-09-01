# Django-demo
Summaried guide to using python's django framework, taken from django tutorial

## Table of Content ##
- [Getting Started](#getting-started)
	- [Framework Overview](#overview)
	- [Installation](#installation)
		- [Installing Django](#installing-django)
		- [Create New Project](#create-new-project)
		- [Create New Application](#create-new-application)
	- [Configure Project](#configure-project)
		- [Database Setup](#database-setup)
		- [Register Application](#register-application)
-[Using Django](#using-django)
	- [Create Model](#create-model)
	- [Create View](#create-view)
	- [Create Template](#create-template)
		- [Extending Template](extending-template)

	
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

	django-admin startproject [project name]
	
### Create New Application
In terminal, `cd` to [project name] directory

	# python manage.py startapp [app name]

### Configure Project
Edit file `settings.py` in the [project name] **submodule** directory
#### Database Setup
Edit the `DATABASES` section in `settings.py`
##### Database Engine
The project use which type of database
- django.db.backends.sqlite3
- django.db.backends.postgresql
- django.db.backends.mysql
- django.db.backends.oracle
- ...
#### User
database user
#### Password
database user's password
#### Host
database host

#### Register Application
Edit the `INSTALLED_APPS` section in `settings.py`

Add the [app name] element to the `INSTALLED_APPS` array

# Using Django
## Create Model
