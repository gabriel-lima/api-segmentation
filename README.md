[![Build Status](https://travis-ci.org/gabriel-lima/api-segmentation.svg?branch=master)](https://travis-ci.org/gabriel-lima/api-segmentation)

[![Coverage Status](https://coveralls.io/repos/github/gabriel-lima/api-segmentation/badge.svg)](https://coveralls.io/github/gabriel-lima/api-segmentation)

# Challenge

This project is a API REST, so you need read how consuming the API Segmentation through [Doc API](DOCS.md).
I recommend used a tool like [PostMan](https://www.getpostman.com/) to help you consumming it.

### Prerequisites

You need have installed python=3.6.2 and Postgres=9.6.4.
But, if you want a shortcut to set up this application I created a Docker configuration.

### Installing

With Docker you just need run:

```
$ docker-compose build
```

Or, on local machine:
```
$ pip install -r requirements.txt
$ psql -c "CREATE DATABASE test_app_database;" -U postgres
$ ./manage.py migrate
```

### Running server

To run with Docker:
```
$ docker-compose up -d
```

Or at folder if installed on local machine, run:
```
$ ./manage.py runserver
```

The application running in `http://localhost:8000`.

## Running the tests

The application have any layers of tests, with: unit tests, functional tests and integration tests.
The tests are in any layers of application, each layer have a folder called tests.

To run all tests:
```
$ docker-compose run --rm web ./manage.py test -v2
```

Or:
```
$ ./manage.py test -v2
```

## Deployment

Application deployed on Heroku through link: https://rd-station-challenge-api.herokuapp.com/

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Clean Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html) - The application's architecture
* [Postgres](https://www.postgresql.org/) - The database used
* [Travis CI](https://travis-ci.org/) - The Continuos Integration
* [Docker](https://www.docker.com/) - The container engine used
* [Heroku](https://www.heroku.com/) - The Clound application plataform
