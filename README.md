# Flask Boilerplate

##### Version: 0.1

## Author
[Daniel Abeles](https://twitter.com/Daniel_Abeles)

## About

For a long time I created my Flask applications from scratch or assembled them from
previous pieces of code. Therefore, I created this boilerplate that will be the
codebase for every Flask app that I'll produce in the future. Some of the parts
in this boilerplate are originated from various code bases, therefore they are
credited in the Credits section.

## Features

* Login Management
* Captcha
* API blueprints
* App factory
* Database support

## How-To

To setup the application follow these steps:

### Create a virtual environment

```bash
pyenv virtualenv venv
pyenv activate venv
pip install -r requirements.txt
```

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
