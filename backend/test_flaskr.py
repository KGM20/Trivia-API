import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('user1',
                                                             'letmein',
                                                             'localhost:5432',
                                                             self
                                                             .database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'Who was the producer for the \
                        famous videogames saga Metal Gear?',
            'answer': 'Hideo Kojima',
            'difficulty': 5,
            'category': 5
        }

        self.wrong_datatypes_question = {
            'question': 'Is this question going to be accepted?',
            'answer': 'No',
            'difficulty': 1,
            'category': 'Something that is not an integer'
        }

        self.search_term = {
            'searchTerm': 'Metal Gear'
        }

        self.search_term_that_does_not_exist = {
            'searchTerm': '¿¬¬uwu|ñ'
        }

        self.quiz_questions = {
            'previous_questions': [16, 19, 17],
            'quiz_category': {"type": {"id": 2, "type": "Art"}, "id": "1"}
        }

        self.quiz_questions_with_id_that_does_not_exist = {
            'previous_questions': [16, 19, 17],
            'quiz_category': {
                                "type": {
                                    "id": 1234567890,
                                    "type": "Art"
                                },
                                "id": "1235467890"}
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for
    expected errors.
    """

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_405_requesting_categories_with_wrong_method(self):
        res = self.client().post('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')

    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))

    def test_404_requesting_questions_beyond_valid_page(self):
        res = self.client().get('/questions?page=1234567890')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_question(self):
        res = self.client().delete('/questions/10')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_delete_a_non_existing_question(self):
        res = self.client().delete('/question/1234567890')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_create_question_with_wrong_datatype(self):
        res = self.client().post('/questions',
                                 json=self.wrong_datatypes_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_search_questions(self):
        res = self.client().post('/questions', json=self.search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_404_searching_question_that_does_not_exist(self):
        res = self.client().post('/questions',
                                 json=self.search_term_that_does_not_exist)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_get_questions_by_category(self):
        res = self.client().get('/categories/5/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])

    def test_404_searching_question_by_category_that_does_not_exist(self):
        res = self.client().get('/categories/1234567890/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_get_questions_to_play_quiz(self):
        res = self.client().post('/quizzes', json=self.quiz_questions)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_try_to_play_quiz_with_non_existing_category(self):
        res = self.client().post('/quizzes',
                                 json=self
                                 .quiz_questions_with_id_that_does_not_exist)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
