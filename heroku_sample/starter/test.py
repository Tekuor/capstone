import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

DIRECTOR_TOKEN = os.environ['DIRECTOR']
# ASSISTANT_TOKEN = os.environ['ASSISTANT']
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
            "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg"
        }

        self.new_actor = {
            'name':'Actor One',
            'age':30,
            'gender':'female'
        }

        # self.search = {
        #     'searchTerm':'African'
        # }

        # self.wrong_search = {
        #     'searchTerm':[]
        # }

        # self.quiz_data = {
        #     'previous_questions': [],
        #     'quiz_category': {'type': "Entertainment", 'id': '5'}
        # }

        # self.wrong_quiz_data = {
        #     'previous_questions': [],
        #     'quiz_category': '5'
        # }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

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

    def test_update_movie(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        self.new_movie['title'] = 'Updated Movie'
        res = self.client().patch('/movies/1', headers=headers, json=self.new_movie)
        print('res', res)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

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
    
    def test_get_all_actors(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        res = self.client().get('/actors', headers=headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

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

    def test_update_actor(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + PRODUCER_TOKEN}

        self.new_actor['name'] = 'Second Actor'
        res = self.client().patch('/actors/1', headers=headers, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

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

    # def test_422_if_create_question_unprocessible_entity(self):
    #     res = self.client().post('/questions', json=self.wrong_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessible entity')

    # def test_search_questions(self):
    #     res = self.client().post('/questions/search', json=self.search)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['total_questions'])

    # def test_422_if_search_questions_unprocessible_entity(self):
    #     res = self.client().post('/questions/search', json=self.wrong_search)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessible entity')

    # def test_get_category_questions(self):
    #     res = self.client().get('/categories/3/questions')
    #     data = json.loads(res.data)
        
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(data['current_category'])

    # def test_404_if_category_cannot_be_found(self):
    #     res = self.client().get('/categories/500/questions')
    #     data = json.loads(res.data)
        
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_get_quiz(self):
    #     res = self.client().post('/quizzes', json=self.quiz_data)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['question'])

    # def test_422_if_unprocessible_entity_quiz(self):
    #     res = self.client().post('/quizzes', json=self.wrong_quiz_data)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessible entity')

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/42')
    #     data = json.loads(res.data)

    #     question = Question.query.filter(Question.id == 42).one_or_none()
        
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertEqual(data['deleted'], 42)
    #     self.assertEqual(question, None)

    # def test_422_if_question_does_not_exist(self):
    #     res = self.client().delete('/questions/200')
    #     data = json.loads(res.data)
        
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessible entity')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()