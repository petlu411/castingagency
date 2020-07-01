# PURPOSE

This is my project -- Casting Agency -- aimed at connecting actors and with movies. I do it as a part of the Udacity Full Stack Dev Nanodegree.

# SETUP 

## Virtual Env

Use virtual environment for convenience: https://virtualenv.pypa.io/en/latest/

`python3 -m venv venv; . venv/bin/activate`

## Install Requirements
`pip3 install -r requirements.txt`


# API Endpoints 
## Actors
- GET '/actors'  - returns a list of actors
- POST '/actors' - used to create a new actor. include 'name','age' and 'gender' in body.
- PATCH '/actors/<int:actor_id>' - used to update actor field. Include one or more of 'name','age' or 'gender' in body to update
- DELETE '/actors/<int:actor_id>' - used to delete an actor.
## Movies
- GET '/movies' - returns a list of movies
- POST '/movies' - used to create a new movie. include 'title' and 'releasedate' in body.
- PATCH '/movies/<int:movie_id>' - used to update movie field. Include one or more of 'title' or 'releasedate' in body to update
- DELETE '/movies/<int:movie_id>' - used to delete a movie.


## RBAC Info
There are three roles defined:

# Assistants
 - Can view actors and movies.

# Directors
 - Can do everything an Assistant can
 - Can create, update and delete actors
 - Can update movies

# Producers
- Can do everything a Director can
- Can create and delete movies



## Notes for testing

https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
YOUR_DOMAIN = petrus.eu.auth0.com
API_IDENTIFIER = castingagency
YOUR_CLIENT_ID = PK8rkuIqdNWccsq1Ru8QLscR1qlCrqkt
YOUR_CALLBACK_URI = https://casting-agency-411.herokuapp.com/ (localhost:5000 if locally run)

login: https://petrus.eu.auth0.com/authorize?audience=castingagency&response_type=token&client_id=PK8rkuIqdNWccsq1Ru8QLscR1qlCrqkt&redirect_uri=https://casting-agency-411.herokuapp.com/

logout: https://petrus.eu.auth0.com/v2/logout

Assistant login: 
assistant@casting.agency
Summer13


Director login:
director@casting.agency
Udacity15

Producer loging:
producer@casting.agency
Winter14

logout via -> '/logout'

{
    "error": 404,
    "message": "Resource not found",
    "success": false
}