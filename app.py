import os
from flask import Flask
from models import setup_db, Actor, Movie
from flask_cors import CORS

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

    return app

app = create_app()

if __name__ == '__main__':
    app.run()