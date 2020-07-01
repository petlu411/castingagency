# PURPOSE

This is my project -- Casting Agency -- aimed at connecting actors and with movies. I do it as a part of the Udacity Full Stack Dev Nanodegree.

# SETUP 

## Virtual Env

Use virtual environment for convenience: https://virtualenv.pypa.io/en/latest/

`python3 -m venv venv; . venv/bin/activate`

## Install Requirements
`pip3 install -r requirements.txt`

## Testing in POSTman
Please find defined tests in the collectionfile `Casting Agency.postman_collection.json`
To test the RBAC, I have provided tokens in the bottom of this README.

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


# Roles
There are three roles defined:

## Assistants
 - Can view actors and movies.

## Directors
 - Can do everything an Assistant can
 - Can create, update and delete actors
 - Can update movies

## Producers
- Can do everything a Director can
- Can create and delete movies

# Data Models

## Actors
 An actor has three properties and an id:
  - id = Column(Integer, primary_key=True)
  - name = Column(String)
  - age = Column(Integer)
  - gender = Column(String)

## Movies
A movie has two properties and an id:
  - id = Column(Integer, primary_key=True,nullable=False)
  - title = Column(String,nullable=False)
  - releasedate = Column(String)

  
# Notes for testing

## General information
- YOUR_DOMAIN = petrus.eu.auth0.com
- API_IDENTIFIER = castingagency
- YOUR_CLIENT_ID = PK8rkuIqdNWccsq1Ru8QLscR1qlCrqkt
- YOUR_CALLBACK_URI = https://casting-agency-411.herokuapp.com/ (localhost:5000 if locally run)

login: https://petrus.eu.auth0.com/authorize?audience=castingagency&response_type=token&client_id=PK8rkuIqdNWccsq1Ru8QLscR1qlCrqkt&redirect_uri=https://casting-agency-411.herokuapp.com/

logout: https://petrus.eu.auth0.com/v2/logout

## Feel free to test using these pre-defined credentials:
Assistant login: 
assistant@casting.agency Pass:Summer13

Director login:
director@casting.agency Pass:Udacity15

Producer loging:
producer@casting.agency Pass:Winter14

