import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import *

from models import setup_db, Movie, Actor
from dateutil.parser import *

from auth import AuthError, requires_auth

# add migration

# check weather actor name is in database
# def check_actors(actors_names):
#   actors = []

#   for name in actors_names:
#     actor = Actor.query.filter(Actor.name == name).one_or_none()
#     if actor is not None:
#       actors.append(actor)
#     else:
#       print(name + ' is not in the database. Please add it to actors database first')
#       abort (404)
  
#   return actors

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)


  
  '''
  Set up CORS. Allow '*' for origins.
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  '''
  Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Contril-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
    return response

  '''
  Create an endpoint to handle GET requests 
  for all available movies.
  '''
  @app.route('/movies', methods = ['GET'])
  @requires_auth('get: movies')
  def get_movies(payload):
    results = Movie.query.order_by(Movie.id).all()
    movies = [movie.format() for movie in results]
    
    if len(movies) == 0:
        abort(404)

    return jsonify({
      'success': True,
      'movies': movies,
      'total_movies': len(movies)
    })

  '''
  Create an endpoint to handle GET requests 
  for all available actors.
  '''
  @app.route('/actors', methods = ['GET'])
  @requires_auth('get: actors')
  def get_actors(payload):
    results = Actor.query.order_by(Actor.id).all()
    actors = [actor.format() for actor in results]
    
    if len(actors) == 0:
        abort(404)

    return jsonify({
      'success': True,
      'actors': actors,
      'total_actors': len(actors)
    })

  ''' 
  Create an endpoint to DELETE movie using a movie ID. 
  '''
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete: movies')
  def delete_movie(payload, movie_id):
    try:
      movie = Movie.query.get(movie_id)

      if movie is None:
        abort(404)
      else:
        title = movie.title
        movie.delete()

      return jsonify({
        'success': True,
        'deleted_id': movie_id,
        'deleted_movie': title
      })
    
    except Exception:
      abort(422)

  ''' 
  Create an endpoint to DELETE actor using a actor ID. 
  '''
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete: actors')
  def delete_actor(payload, actor_id):
    try:
      actor = Actor.query.get(actor_id)

      if actor is None:
        abort(404)
      else:
        name = actor.name
        actor.delete()

      return jsonify({
        'success': True,
        'deleted_id': actor_id,
        'deleted_actor': name
      })
    
    except Exception:
      abort(422)

  '''
  # Create an endpoint to POST a new actor, 
  # which will require the name, age and gender
  '''
  @app.route('/actors', methods=['POST'])
  @requires_auth('post: actors')
  def add_actor(payload):
    body = request.get_json()
    
    try:
      name = body.get('name', None)
      age = body.get('age', None)
      gender = body.get('gender', None)

      new_actor = Actor(name = name, age = age, gender = gender)
      new_actor.insert()
      
      return jsonify({
          'success': True,
          'added actor': name
        })
    
    except Exception:
      abort(422)

  '''
  # Create an endpoint to POST a new movie, 
  # which will require the title, release date and actors
  '''
  @app.route('/movies', methods=['POST'])
  @requires_auth('post: movies')
  def add_movie(payload):
    body = request.get_json()

    try:
      title = body.get('title', None)
      releaseDate1 = body.get('releaseDate', None)
      releaseDate = parse(releaseDate1).date()
      actors_names = body.get('actors_names', None)

      new_movie = Movie(title = title, releaseDate = releaseDate)

      for name in actors_names:
        actor = Actor.query.filter(Actor.name == name).one_or_none()
        if actor is not None:
          new_movie.actors.append(actor)
        else:
          print(name + ' is not in the database. Please add it to actors database first')
          abort (404)
          
      new_movie.insert()

      cast = [actor.format() for actor in new_movie.actors]

      return jsonify({
          'success': True,
          'added movie': new_movie.format(),
          'cast': cast
        })
    
    except Exception:
      abort(422)
  '''
  # Create an endpoint to update an actor, 
  # which may require the name, age and gender
  '''
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch: actors')
  def update_actor(payload, actor_id):
      actor = Actor.query.get(actor_id)
      if actor is None:
        abort(404)
      
      body = request.get_json()
      try:
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        if name is not None:
            actor.name = name
        if age is not None:       
            actor.age = age
        if gender is not None:       
            actor.gender = gender
        
        actor.update()
          
      except Exception:
        abort(401)

      return jsonify({
          'success': True,
          'updated actor': actor.format()
      })

  '''
  # Create an endpoint to update a movie, 
  # which may require the title, release date and actors
  '''
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch: movies')
  def update_movie(payload, movie_id):
      movie = Movie.query.get(movie_id)
      if movie is None:
        abort(404)
      
      body = request.get_json()
      actors = []

      try:
        title = body.get('title', None)
        releaseDate = body.get('releaseDate', None)
        actors_names = body.get('actors_names', None)
        if title is not None:
          movie.title = title
        if releaseDate is not None:       
          movie.releaseDate = parse(releaseDate).date()
        if actors_names is not None:
          for name in actors_names:
            actor = Actor.query.filter(Actor.name == name).one_or_none()
            if actor is not None:
              actors.append(actor)
            else:
              print(name + ' is not in the database. Please add it to actors database first')
              abort (404)
                
        if actors != []:
          movie.actors = actors

        movie.update()
          
      except Exception:
          abort(401)
      
      cast = [actor.format() for actor in movie.actors]

      return jsonify({
          'success': True,
          'updated movie': movie.format(),
          'cast': cast
      })


  ''' 
  # Create error handlers for all expected errors  
  '''
  @app.errorhandler(401)
  def unauthorized(error):
    return jsonify({
      'success': False,
      'error': 401,
      'message': 'Unauthorized' 
    }), 401

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'Not found' 
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'Unprocessable' 
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'Bad request' 
    }), 400

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': 'Method not allowed' 
    }), 405

  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      'success': False,
      'error': 500,
      'message': 'Internal server error' 
    }), 500

  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
      response = jsonify(ex.error)
      response.status_code = ex.status_code
      return response

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)