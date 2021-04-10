import os
from flask import Flask, request, jsonify, abort
from models import setup_db, Movie, Actor
from flask_cors import CORS
from auth.auth import AuthError, requires_auth

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
    def retrieve_movies():
        selection = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_items(request, selection)

        if len(current_movies) == 0:
            abort(404)

        return jsonify({
        'success': True,
        'movies': current_movies
        })

    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movie(id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)

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
    def create_movie():
        body = request.get_json()

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        try:
            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()

            selection = Movie.query.order_by(Movie.id).all()
            current_movies = paginate_items(request, selection)

            return jsonify({
                'success': True,
                'created': movie.id,
                'movies': current_movies,
                'total_movies': len(Movie.query.all())
            })

        except:
            abort(422)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    # @requires_auth('patch:drinks')
    def update_movie(payload,id):
        try:
            body = request.get_json()
            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)

            if 'title' in body:
                movie.title = body.get('title', None)
            if 'release_date' in body:
                movie.recipe = body.get('release_date', None)

            movie.update()

            return jsonify({
                'success': True,
                'movie': movie
            })

        except:
            abort(422)

    @app.route('/actors')
    def retrieve_actors():
        selection = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_items(request, selection)

        if len(current_actors) == 0:
            abort(404)

        return jsonify({
        'success': True,
        'actors': current_actors
        })

    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if actor is None:
                abort(404)

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
    def create_actor():
        body = request.get_json()

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        try:
            actor = Actor(title=new_title, release_date=new_release_date)
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
    # @requires_auth('patch:drinks')
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

            actor.update()

            return jsonify({
                'success': True,
                'actor': actor
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
        'message': "server error"
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
        'message': "unprocessible entity"
        }), 422

    return app

app = create_app()

if __name__ == '__main__':
    app.run()