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
### GET '/actors'  
This endpoint returns a list of actors.
Available to producers, directors and assistants.
Successful response example:
```
{
    "actors": [
        {
            "age": "23",
            "gender": "female",
            "id": 1,
            "name": "Olive Person"
        },
        {
            "age": "29",
            "gender": "female",
            "id": 6,
            "name": "Johanna Andersson"
        },
        {
            "age": "29",
            "gender": "male",
            "id": 11,
            "name": "Lenny Wild"
        },
        {
            "age": "45",
            "gender": "female",
            "id": 10,
            "name": "Lenny Wild"
        },
        {
            "age": "15",
            "gender": null,
            "id": 13,
            "name": "Whale-man"
        }
    ],
    "success": true,
    "total_actors": 5
}
```

### POST '/actors' 
This endpoint is used to create a new actor. Request should include 'name','age' and 'gender' in body.
Available to producers and directors
Successful response example:
```
{
    "created": 14,
    "success": true,
    "total_actors": 6
}
```
### PATCH '/actors/<int:actor_id>' 
This endpoint is used to update actor field. Include one or more of 'name','age' or 'gender' in body to update.
Available to producers and directors
Successful response example:
```
{
    "success": true,
    "total_actors": 6,
    "updated": 14
}
```
### DELETE '/actors/<int:actor_id>' 
This endpoint is used to delete an actor.
Available to producers and directors
Successful response example:
```
{
    "actors": [
        {
            "age": "23",
            "gender": "female",
            "id": 1,
            "name": "Olive Person"
        },
        {
            "age": "29",
            "gender": "female",
            "id": 6,
            "name": "Johanna Andersson"
        },
        {
            "age": "29",
            "gender": "male",
            "id": 11,
            "name": "Lenny Wild"
        },
        {
            "age": "45",
            "gender": "female",
            "id": 10,
            "name": "Lenny Wild"
        },
        {
            "age": "45",
            "gender": "female",
            "id": 14,
            "name": "Henrietta Ford"
        }
    ],
    "deleted": 13,
    "success": true,
    "total_actors": 5
}
```
## Movies
### GET '/movies' 
This endpoint returns a list of movies.
Available to producers, directors and assistants.
Successful response example:
```
{
    "movies": [
        {
            "id": 3,
            "releasedate": "2018-03-04",
            "title": "The life of an Ant"
        },
        {
            "id": 5,
            "releasedate": "2020-01-01",
            "title": "The horror"
        },
        {
            "id": 6,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 10,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 9,
            "releasedate": "2020-06-01",
            "title": "Wild West 2"
        },
        {
            "id": 12,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 13,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 14,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        }
    ],
    "success": true,
    "total_movies": 8
}
```
### POST '/movies'
This endpoint is used to create a new movie. Request should include 'title' and 'releasedate' in body.
Available to producers and directors.
Successful response example:
```
{
    "created": 15,
    "success": true,
    "total_movies": 9
}
```
### PATCH '/movies/<int:movie_id>' 
This endpoint is used to update movie field. Include one or more of 'title' or 'releasedate' in body to update.
Available to producers and directors.
Successful response example:
```
{
    "success": true,
    "total_movies": 9,
    "updated": 15
}
```
### DELETE '/movies/<int:movie_id>' 
This endpoint is used to delete a movie. Only available for producers.
Successful response example:
```
{
    "deleted": 15,
    "movies": [
        {
            "id": 3,
            "releasedate": "2018-03-04",
            "title": "The life of an Ant"
        },
        {
            "id": 5,
            "releasedate": "2020-01-01",
            "title": "The horror"
        },
        {
            "id": 6,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 10,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 9,
            "releasedate": "2020-06-01",
            "title": "Wild West 2"
        },
        {
            "id": 12,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 13,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        },
        {
            "id": 14,
            "releasedate": "2020-06-01",
            "title": "The Wild West"
        }
    ],
    "success": true,
    "total_movies": 8
}
```

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

