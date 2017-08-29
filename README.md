[![Build Status](https://travis-ci.org/gabriel-lima/api-segmentation.svg?branch=master)](https://travis-ci.org/gabriel-lima/api-segmentation)

[![Coverage Status](https://coveralls.io/repos/github/gabriel-lima/api-segmentation/badge.svg)](https://coveralls.io/github/gabriel-lima/api-segmentation)

# Challenge

See how consuming the API Segmentation through [Doc API](DOCS.md) 

### Prerequisites

You need have installed python=3.6.2 and Postgres=9.6.4. But, if you want a shortcut to set up this application I created a Docker configuration.

### Installing

With Docker you just need run:

```
docker-compose build
```

### Running server

To run with Docker:
```bash
docker-compose up -d
```

Or at folder if installed on local machine, run:
```bash
./manage.py runserver
```

The application running in `http://localhost:8000`.

## Running the tests

To run all tests:
```bash
docker-compose run --rm web ./manage.py test -v2
```

Or:
```bash
./manage.py test -v2
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
