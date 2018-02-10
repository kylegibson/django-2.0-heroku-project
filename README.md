# django-2.0-heroku-project


## Features

* Bootstrap4 base template
* HAML templates
* Basic view/url configuration example
* Whitenoise for static file serving
* Waitress WSGI server
* pipenv


## Local Quick start

```
ln -s dev.env .env
pipenv install --dev --python=3.6
pipenv shell

python manage.py migrate
python manage.py runserver
```

### Local with DEBUG = False

If you want to run locally,
with `DEBUG = False`,
make sure you run

```
python manage.py collectstatic
```

Otherwise,
the admin site
among other things,
will not work.

## Heroku Quick Deploy

```
heroku create

ln -s dev.env .env
pipenv install --dev --python=3.6
pipenv shell
heroku addons:attach heroku-postgresql:hobby-dev
heroku config:set DJANGO_SECRET_KEY=$(python manage.py generate_secret_key)
heroku config:set DJANGO_ALLOWED_HOSTS='<appname>.herokuapp.com'
heroku config:set DJANGO_SECURE_SSL_HOST='<appname>.herokuapp.com'
heroku config:set DJANGO_DEBUG=yes

git push heroku master

heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open
```
