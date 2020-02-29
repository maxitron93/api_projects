## Setting up
Creating a new project
```
django-admin startproject project_name
```
<br>

Migrate database
```
python manage.py migrate
```
<br>

Create superuser
```
python manage.py createsuperuser
```
<br>

Add rest_framework to installed apps in `settings.py`
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
