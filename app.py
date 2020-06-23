import os
from flask import Flask,request,jsonify,abort
from flask_cors import CORS

from models import setup_db, Actor, Movie

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/') # INDEX
    def get_greeting():
        greeting = "Hello, there are no movies" 
        movies = Movie.query.all()
        if movies:
            greeting = movies
        return greeting

    @app.route('/coolkids') # MOTIVATIONAL ENDPOINT
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"


    @app.route('/actors', methods=['POST']) #CREATE ACTOR
    def create_actors():
        body = request.get_json()

        new_name = body.get('name',None)
        new_age = body.get('age',None)
        new_gender = body.get('gender',None)

        new_actor = Actor(name=new_name,age=new_age,gender=new_gender)
        new_actor.insert()

        return jsonify({
          'success':True,
          'created':new_actor.id,
          'total_actors': len(Actor.query.all())})

    @app.route('/actors', methods=['GET']) #READ ACTORS
    def retieve_actors():
        actors = Actor.query.all()
        selected_actors = [actor.format() for actor in actors]
        return jsonify({
            "success":True,
            "total_actors":len(Actor.query.all()),
            "actors": selected_actors

        })

    return app

app = create_app()

if __name__ == '__main__':
    app.run()