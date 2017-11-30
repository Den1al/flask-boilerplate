# Flask Boilerplate

##### Version: 0.1

## About

For a long time I created my Flask application from scratch or assemble it from
previous pieces of code. Therefore, I created this boilerplate that will be the
codebase for every Flask app that I'll produce in the future. Some of the parts
in this boilerplate are originated from various code bases, therefore they are
credited in the Credits section.

## Features

* Login Mangements
* Captcha
* API blueprint
* App factory
* Database

## How-To

To setup the application follow this steps:

### Create a virtual environment

* `pyenv virtualenv venv`
* `pyenv activate venv`
* `pip install -r requirements.txt`

### Configuration

If captcha is desired - please set the following fields in `config.py`:

1. `SHOW_CAPTCHA`
2. `RECAPTCHA_SITE_KEY`
3. `RECAPTCHA_SECRET_KEY`

For more information visit the
[documentation](https://developers.google.com/recaptcha/docs/verify)

### Run

1. python manage.py createdb
2. python manage.py runserver

## Credits

1. [Miguel Grinberg](https://github.com/miguelgrinberg)
