# PURPOSE

This is my project -- Casting Agency -- aimed at connecting actors and with movies. I do it as a part of the Udacity Full Stack Dev Nanodegree.

# SETUP 

## Virtual Env

Use virtual env https://virtualenv.pypa.io/en/latest/

`python3 -m venv venv; . venv/bin/activate`

## Install Requirements
`pip3 install -r requirements.txt`


# API Endpoints 

## Actors

## Movies



## TODO  - list of remaining activities
Here is a list of things I still have to do. I will edit it as I go through the project

* Define Roles for access: Casting Assistant (Actor(R) + Movie(R), Casting Director (Actor(CRUD)+Movie(RU)), Executive Producer (Actor (CRUD) + Movie (CRUD))
    - Add CRUD for Actor DONE
    - Add CRUD for Movie DONE
    - Set Auth0 Roles  DONE
* Implement Auth0 authentication
* Set up testcases for each endpoint (4 endpoints * 2 models * 2 tests)
* Model Movies (title, release date) and Actors (name, gender, age)

https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
YOUR_DOMAIN = petrus.eu.auth0.com
API_IDENTIFIER = castingagency
YOUR_CLIENT_ID = PK8rkuIqdNWccsq1Ru8QLscR1qlCrqkt
YOUR_CALLBACK_URI = localhost:5000

https://petrus.eu.auth0.com/authorize?audience=castingagency&response_type=token&client_id=PK8rkuIqdNWccsq1Ru8QLscR1qlCrqkt&redirect_uri=localhost:5000

Assistant login: 
assistant@casting.agency
Summer13

Director login:
director@casting.agency
Udacity15

Producer loging:
producer@casting.agency
Winter14