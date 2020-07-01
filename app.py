import os
from flask import Flask,request,jsonify,abort,render_template
from flask_cors import CORS

from models import setup_db, Actor, Movie
from auth import requires_auth,AuthError

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    @app.route('/') # INDEX
    #@requires_auth('get:actors')
    def get_greeting():
        greeting = "Hello, there are no movies" 
        actors = Actor.query.all()
        movies = Movie.query.all()
        return render_template('main.html', actors=actors, movies=movies)

    @app.route('/coolkids') # MOTIVATIONAL ENDPOINT
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/login')
    def login():
        return "No probls"

    '''
    ACTOR ENDPOINTS GET, POST, PATCH, DELETE
    '''
    @app.route('/actors', methods=['GET']) #READ ACTORS
    @requires_auth('get:actor')
    def retrieve_actors(payload):
        actors = Actor.query.all()
        selected_actors = [actor.format() for actor in actors]
        return jsonify({
            "success":True,
            "total_actors":len(Actor.query.all()),
            "actors": selected_actors
        })
    
    @app.route('/actors', methods=['POST']) #CREATE ACTOR
    @requires_auth('post:actor')
    def create_actors(payload):
        body = request.get_json()
        if body.get('name') is None or body.get('age') is None or body.get('gender') is None:
            abort(422)
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
    @requires_auth('patch:actor')
    def update_actor(payload,actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).first()
        body = request.get_json()
        if not actor:
            abort(404)
        if body.get("name"):
            actor.name = body.get("name")
        if body.get("age"):
            actor.age = body.get("age")
        if body.get("gender"):
            actor.gender = body.get("gender")
        actor.update()
        return jsonify({
            "success":True,
            "updated":actor_id,
            "total_actors": len(Actor.query.all())
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE']) #DELETE ACTOR
    @requires_auth('delete:actor')
    def remove_actor(payload,actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).first()
        if not actor:
            abort(404)
        actor.delete()
        actors = Actor.query.all()
        selected_actors = [actor.format() for actor in actors]
        return jsonify({
            "success":True,
            "deleted": actor_id,
            "total_actors": len(Actor.query.all()),
            "actors": selected_actors
        })

    '''
    ENDPOINTS FOR MOVIES
    '''
    @app.route('/movies',methods=['GET']) # RETRIEVE MOVIES
    @requires_auth('get:movies')
    def retrieve_movies(payload):
        movies = Movie.query.all()
        selected_movies = [movie.format() for movie in movies]
        return jsonify({
            "success":True,
            "movies":selected_movies,
            "total_movies" :len(Movie.query.all())
        })

    @app.route('/movies',methods=['POST']) # ADD NEW MOVIE
    @requires_auth('post:movies')
    def create_movie(payload):
        body = request.get_json()
        if body.get('title') is None or body.get('releasedate') is None:
            abort(422)
        new_title = body.get('title',None)
        new_releasedate = body.get('releasedate',None)

        new_movie = Movie(title=new_title,releasedate=new_releasedate)
        new_movie.insert()
        return jsonify({
          'success':True,
          'created':new_movie.id,
          'total_movies': len(Movie.query.all())})

    @app.route('/movies/<int:movie_id>',methods=['PATCH']) #UPDATE A MOVIE 
    @requires_auth('patch:movies')
    def update_movie(payload,movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).first()
        if not movie:
            abort(404)
        body = request.get_json()
        if body.get('title') is None and body.get('releasedate') is None:
            abort(422)
        if body.get("title"):
            movie.title = body.get("title")
        if body.get("releasedate"):
            movie.releasedate = body.get("releasedate")
        movie.update()
        return jsonify({
            "success":True,
            "updated":movie_id,
            "total_movies": len(Movie.query.all())
        })

    @app.route('/movies/<int:movie_id>',methods=['DELETE']) # DELETE A MOVIE 
    @requires_auth('delete:movies')
    def remove_movie(payload,movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).first()
        if not movie:
            abort(404)       
        movie.delete()
        movies = Movie.query.all()
        selected_movies = [movie.format() for movie in movies]
        return jsonify({
            "success":True,
            "total_movies": len(movies),
            "deleted":movie_id,
            "movies": selected_movies
        })

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