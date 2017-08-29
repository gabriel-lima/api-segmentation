[![Build Status](https://travis-ci.org/gabriel-lima/rd-challenge.svg?branch=master)](https://travis-ci.org/gabriel-lima/rd-challenge)

# Challenge

### Prerequisites

You need have installed python=3.6.2 and MySQL=5.7.14. But, if you want a shortcut to set up this application I created a Docker configuration.

### Installing

With Docker you need just run:

```
docker-compose build
```

### Running server

To run with Docker, you need just:
```bash
docker-compose up -d
```

Or at folder /project, run:
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

Application deployed on Heroku through link: https://rd-station-challenge-rails-app.herokuapp.com/

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [MySQL](https://www.mysql.com/) - The database used
* [Travis CI](https://travis-ci.org/) - The Continuos Integration
* [Docker](https://www.docker.com/) - The container engine used
* [Heroku](https://www.heroku.com/) - The Clound application plataform

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

[Creating a new Rails application project with Docker](https://github.com/IcaliaLabs/guides/wiki/Creating-a-new-Rails-application-project-with-Docker)
