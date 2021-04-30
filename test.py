import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

DIRECTOR_TOKEN = os.environ['DIRECTOR']
ASSISTANT_TOKEN = os.environ['ASSISTANT']
PRODUCER_TOKEN = os.environ['PRODUCER']

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.username = 'postgres'
        self.password = '123456'
        self.url = 'localhost:5432'
        self.database_path  = "postgresql://{}:{}@{}/{}".format(self.username, self.password, self.url, self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {
            'title':'First Movie',
            'release_date':'2021/06/07',
            "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg",
            "roles": []
        }

        self.new_actor = {
            'name':'Actor One',
            'age':30,
            'gender':'female'
        }

        self.wrong_movie = {
            'title': 5,
            'release_date': 8,
            "image_url": 2
        }

        self.wrong_actor = {
            'age':'30',
            'gender':90
        }
    
    def tearDown(self):
        """Executed after reach test"""
        self.app = create_app()
        self.db.init_app(self.app)
        with self.app.app_context():
            self.db.drop_all()

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_all_movies(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_404_sent_requesting_movies_beyond_valid_page(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}
        
        res = self.client().get('/movies?page=300', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_movie(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().post('/movies', headers=headers, json=self.new_movie)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['total_movies'])

    def test_422_if_create_movie_unprocessible_entity(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().post('/movies', headers=headers, json=self.wrong_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessible entity')

    def test_update_movie(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        self.new_movie['title'] = 'Updated Movie'
        res = self.client().patch('/movies/1', headers=headers, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_422_if_update_movie_unprocessible_entity(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().patch('/movies/109', headers=headers, json=self.wrong_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessible entity')

    def test_delete_movie(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        self.client().post('/movies', headers=headers, json=self.new_movie)
        res = self.client().delete('/movies/2', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['total_movies'])

    def test_422_if_movie_does_not_exist(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().delete('/movies/200', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessible entity')
    
    def test_get_all_actors(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().get('/actors', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
    
    def test_404_sent_requesting_actors_beyond_valid_page(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}
        
        res = self.client().get('/actors?page=300', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_actor(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().post('/actors', headers=headers, json=self.new_actor)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    def test_422_if_create_actor_unprocessible_entity(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().post('/actors', headers=headers, json=self.wrong_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessible entity')

    def test_update_actor(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        self.new_actor['name'] = 'Second Actor'
        res = self.client().patch('/actors/3', headers=headers, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_422_if_update_actor_unprocessible_entity(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().patch('/actors/109', headers=headers, json=self.wrong_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessible entity')

    def test_delete_actor(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        self.client().post('/actors', headers=headers, json=self.new_actor)
        res = self.client().delete('/actors/2', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    def test_422_if_actor_does_not_exist(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().delete('/actors/200', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessible entity')

    def test_director_add_actor(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + DIRECTOR_TOKEN}

        res = self.client().post('/actors', headers=headers, json=self.new_actor)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    def test_403_director_add_movie(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + DIRECTOR_TOKEN}

        res = self.client().post('/movies', headers=headers, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

    def test_assistant_view_movies(self):
        producerHeaders = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + ASSISTANT_TOKEN}

        self.client().post('/movies', headers=producerHeaders, json=self.new_movie)
        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_403_assistant_add_movie(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + ASSISTANT_TOKEN}

        res = self.client().post('/movies', headers=headers, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['description'], 'Permission not found.')

    def test_producer_get_all_movies(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_producer_get_all_actors(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().get('/actors', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()