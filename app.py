import os
from flask import Flask, request, jsonify, abort
from models import setup_db, Movie, Actor, MovieRoles
from flask_cors import CORS
from auth.auth import AuthError, requires_auth
import sys
import json

ITEMS_PER_PAGE = 10

def paginate_items(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * ITEMS_PER_PAGE
  end = start + ITEMS_PER_PAGE

  items = [item.format() for item in selection]
  current_items = items[start:end]

  return current_items

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/movies')
    @requires_auth('get:movies')
    def retrieve_movies(payload):
        selection = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_items(request, selection)

        if len(current_movies) == 0:
          abort(404)

        try:
            return jsonify({
            'success': True,
            'movies': current_movies
            })
        except:
            sys.exc_info()
            abort(404)

    @app.route('/movies/<int:id>', methods=['GET'])
    @requires_auth('patch:movies')
    def get_movie(payload, id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            roles = MovieRoles.query.filter(MovieRoles.movie_id == id).all()
            for role in roles:
                role.format()

            if movie is None:
                abort(404)

            return jsonify({
                'success': True,
                'movie': movie.format(),
                # 'roles': roles
            })

        except:
            abort(422)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)

            roles = MovieRoles.query.filter(MovieRoles.movie_id == id).all()
            for role in roles:
                role.delete()

            movie.delete()
            selection = Movie.query.order_by(Movie.id).all()
            current_movies = paginate_items(request, selection)

            return jsonify({
                'success': True,
                'deleted': id,
                'movies': current_movies,
                'total_movies': len(Movie.query.all())
            })

        except:
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        body = request.get_json()

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)
        new_image_url = body.get('image_url', None)
        new_roles = body.get('roles', None)
        new_description = body.get('description', None)

        try:
            movie = Movie(title=new_title, release_date=new_release_date, image_url=new_image_url, description=new_description)
            movie.insert()

            if(len(new_roles)):
                for role in new_roles:
                    new_role = MovieRoles(actor_id=role['actor_id'], movie_id=movie.id, role=role['role'])
                    new_role.insert()

            selection = Movie.query.order_by(Movie.id).all()
            current_movies = paginate_items(request, selection)

            return jsonify({
                'success': True,
                'created': new_role.id,
                'movies': current_movies,
                'total_movies': len(Movie.query.all())
            })

        except:
            abort(422)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, id):
        try:
            body = request.get_json()
            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)
           
            if 'title' in body:
                movie.title = body.get('title', None)
            if 'release_date' in body:
                movie.release_date = body.get('release_date', None)
            if 'image_url' in body:
                movie.image_url = body.get('image_url', None)
            if 'description' in body:
                movie.description = body.get('description', None)

            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.format()
            })

        except:
            abort(422)

    @app.route('/actors')
    @requires_auth('get:actors')
    def retrieve_actors(payload):
        selection = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_items(request, selection)

        if len(current_actors) == 0:
            abort(404)

        return jsonify({
        'success': True,
        'actors': current_actors
        })

    @app.route('/actors/<int:id>', methods=['GET'])
    @requires_auth('patch:actors')
    def get_actor(payload, id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if actor is None:
                abort(404)

            return jsonify({
                'success': True,
                'actor': actor.format()
            })

        except:
            abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if actor is None:
                abort(404)

            roles = MovieRoles.query.filter(MovieRoles.actor_id == id).all()
            for role in roles:
                role.delete()

            actor.delete()
            selection = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_items(request, selection)

            return jsonify({
                'success': True,
                'deleted': id,
                'actors': current_actors,
                'total_actors': len(Actor.query.all())
            })

        except:
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        body = request.get_json()

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_image_url = body.get('image_url', None)

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender, image_url=new_image_url)
            actor.insert()

            selection = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_items(request, selection)
            
            return jsonify({
                'success': True,
                'created': actor.id,
                'actors': current_actors,
                'total_actors': len(Actor.query.all())
            })

        except:
            abort(422)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload,id):
        try:
            body = request.get_json()
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if actor is None:
                abort(404)

            if 'name' in body:
                actor.name = body.get('name', None)
            if 'age' in body:
                actor.age = body.get('age', None)
            if 'gender' in body:
                actor.gender = body.get('gender', None)
            if 'gender' in body:
                actor.image_url = body.get('image_url', None)

            actor.update()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })

        except:
            abort(422)

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
        'success': False,
        'error': 404,
        'message': "resource not found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
        'success': False,
        'error': 500,
        'message': error['error']
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
        'success': False,
        'error': 400,
        'message': "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
        'success': False,
        'error': 401,
        'message': "unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
        'success': False,
        'error': 403,
        'message': "forbidden"
        }), 403

    @app.errorhandler(405)
    def invalid_method(error):
        return jsonify({
        'success': False,
        'error': 405,
        'message': "invalid method"
        }), 405

    @app.errorhandler(409)
    def duplicate_resource(error):
        return jsonify({
        'success': False,
        'error': 409,
        'message': "duplicate resource"
        }), 409

    @app.errorhandler(422)
    def not_processable(error):
        return jsonify({
        'success': False,
        'error': 422,
        'message': error['error']
        }), 422

    @app.errorhandler(AuthError)
    def errorFailed(error):
        return jsonify({
        "success": False, 
        "error": error.status_code,
        "message": error['error']
        }), error.status_code

    return app

app = create_app()

if __name__ == '__main__':
    app.run()