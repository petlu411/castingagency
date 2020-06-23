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

    '''
    ACTOR ENDPOINTS GET, POST, PATCH, DELETE
    '''
    @app.route('/actors', methods=['GET']) #READ ACTORS
    def retieve_actors():
        actors = Actor.query.all()
        selected_actors = [actor.format() for actor in actors]
        return jsonify({
            "success":True,
            "total_actors":len(Actor.query.all()),
            "actors": selected_actors
        })
    
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

    @app.route('/actors/<int:actor_id>',methods=['PATCH']) # UPDATE ACTOR 
    def update_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).first()
        actor.update()
        return "UNDER CONSTRUCTION Cant update "+actor.name

    @app.route('/actors/<int:actor_id>', methods=['DELETE']) #DELETE ACTOR
    def remove_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).first()
        if not actor:
            abort(404)
        actor.delete()
        return jsonify({
            "success":True,
            "id": actor_id,
            "total_actors": len(Actor.query.all())
        })

    '''
    ENDPOINTS FOR MOVIES
    '''
    @app.route('/movies',methods=['GET'])
    def retrieve_movies():
        movies = Movie.query.all()
        selected_movies = [movie.format() for movie in movies]
        return jsonify({
            "success":True,
            "movies":selected_movies,
            "total_movies" :len(Movie.query.all())
        })

    @app.route('/movies',methods=['POST'])
    def create_movie():
        body = request.get_json()

        new_title = body.get('title',None)
        new_releasedate = body.get('releasedate',None)
        
        new_movie = Movie(title=new_title,releasedate=new_releasedate)
        new_movie.insert()
        return jsonify({
          'success':True,
          'created':new_movie.id,
          'total_movies': len(Movie.query.all())})


    '''
    --> ERROR HANDLING SECTION <--
    '''
    #404 error
    @app.errorhandler(404) 
    def not_found(error):
        return jsonify({
        'success': False,
        'error' : 404,
        'message': 'Resource not found'
        }),404

    #422 error
    @app.errorhandler(422)
    def unprocessed_entity(error):
        return jsonify({
        'success': False,
        'error' : 422,
        'message' : 'Could not process entity'
        }),422

    return app

app = create_app()

if __name__ == '__main__':
    app.run()