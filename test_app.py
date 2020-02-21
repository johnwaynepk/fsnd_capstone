import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

class AgencyTestCase(unittest.TestCase):
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
        self.new_actor = {
            'name': 'Huge Grant', 
            'age': 60, 
            'gender': 'male'
        }

        self.existing_actor = {
            'name': 'Robin Wright', 
            'age': 56, 
            'gender': 'female'
        }

        self.bearer_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16TTJPVVF6UlRRd09EZzNRak5CUlVJeE9EUTNNRGc1Umprek1FVTRSa0kxTVRKQ09URkVNQSJ9.eyJpc3MiOiJodHRwczovL2p3YXluZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWUyM2VjZDU4M2Q2MTkwZTk2MWRjNjQ3IiwiYXVkIjoiQWdlbmN5IiwiaWF0IjoxNTgyMTc2NDkxLCJleHAiOjE1ODIyNDg0OTEsImF6cCI6InVzREZ0dDFRTnFMblFvNXphbFFMajQ4SFUxY3d0MUtBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6IGFjdG9ycyIsImRlbGV0ZTogbW92aWVzIiwiZ2V0OiBhY3RvcnMiLCJnZXQ6IG1vdmllcyIsInBhdGNoOiBhY3RvcnMiLCJwYXRjaDogbW92aWVzIiwicG9zdDogYWN0b3JzIiwicG9zdDogbW92aWVzIl19.cvjwAnceoukv7elJFf6NoK2XMzj-6PqjWBJsLw8rpPf8QuXSh11HwjVJ_Ja6-SVv_pSpFp2-my99sLP_Mubzt2DI4aGIyIeUuaM_ckB-9Kk0HVnAc15wa-92rHDp8YAPd2rbpDgz0mGDicMtajXvEI7ldeZKJkRjHxN5w-WJooXm5owGFWlKb-TxeAZDhC5gvvtzCnFUiH6mdsfJRUHGGtDcbd0GsullikvAXEAVtznXW2jA5yOKt-_Pk2KLByvkzfw8Gib_08HElZiHBZ4PK9lohVlTafdU-deu1Gl-QfxFefrwvHN9AIQWAAVTDbCSVhXr6U5OyLzVsM0WOlcc-g'

        # self.bearer_token = os.environ.get("BEARER_TOKEN")
        print(self.bearer_token)                
        self.new_movie = {
            'title': 'Cloud Atlas',
            'releaseDate': '2012-10-26',
            'actors_names': ['Tom Hanks']
        }

        self.existing_movie = {
            'title': 'Big',
            'releaseDate': '1984-3-10',
            'actors_names': ['Tom Hanks']
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_actors(self):
        res = self.client().get('/actors', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

    def test_405_if_get_actor_not_allowed(self):
        res = self.client().get('/actors/1000', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')

    def test_get_movies(self):
        res = self.client().get('/movies', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])

    def test_405_if_get_movie_not_allowed(self):
        res = self.client().get('/movies/1000', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        actor = Actor.query.get(1)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted_id'], 1)
        self.assertTrue(data['deleted_actor'])
        
    def test_422_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        actor = Actor.query.get(1)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted_id'], 1)
        self.assertTrue(data['deleted_movie'])
        
    def test_422_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_add_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added actor'])
    
    def test_405_if_add_actor_not_allowed(self):
        res = self.client().post('/actors/45', json=self.new_actor, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')    

    def test_add_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added movie'])
        self.assertTrue(data['cast'])
    
    def test_405_if_add_movie_not_allowed(self):
        res = self.client().post('/movies/45', json=self.new_movie, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')    
    
    def test_update_actor(self):
        res = self.client().patch('/actors/6', json=self.existing_actor, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated actor'])
    
    def test_405_if_update_actor_not_allowed(self):
        res = self.client().patch('/actors', json=self.existing_actor, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')    

    def test_update_movie(self):
        res = self.client().patch('/movies/2', json=self.existing_movie, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated movie'])
    
    def test_405_if_update_movie_not_allowed(self):
        res = self.client().patch('/movies', json=self.existing_movie, headers = {'authorization':self.bearer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
