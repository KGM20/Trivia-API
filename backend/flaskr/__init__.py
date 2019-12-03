import os
import random

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    CORS(app)
    #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    '''
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''
    @app.route('/categories')
    def retrieve_categories():
        categories = db.session.query(Category).order_by(Category.id).all()
        current_categories = [category.format() for category in categories]

        if len(current_categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': current_categories
        })
    '''
    @TODO: 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
    '''
    @app.route('/questions')
    def retrieve_questions():
        selection = db.session.query(Question).order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        if len(current_questions) == 0:
            abort(404)

        categories = db.session.query(Category).order_by(Category.id).all()
        current_categories = [category.format() for category in categories]

        if len(current_categories) == 0:
            abort(404)

        # Waiting for the explanation of what to put on this parameter
        current_category = {'id': 6, 'type': 'Sports'}

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection),
            'categories': current_categories,
            'current_category': current_category
        })
    '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_a_question(question_id):
        question = db.session.query(Question).get(question_id)

        if question is None:
            abort(404)
          
        try:
            question.delete()

            return jsonify({
                'success': True,
            })

        except:
            abort(422)

    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()

        question = body.get('question', None)
        answer = body.get('answer', None)
        difficulty = body.get('difficulty', None)
        category = body.get('category', None)
        searchTerm = body.get('searchTerm', None)

        if searchTerm:
            questions = db.session.query(Question).filter(Question.question.ilike('%'+searchTerm+'%')).all()
            search_questions = paginate_questions(request, questions)

            if len(questions) == 0:
                abort(404)

            # Waiting for the explanation of what to put on this parameter
            current_category = {'id': 6, 'type': 'Sports'}

            return jsonify({
                'success': True,
                'questions': search_questions,
                'total_questions': len(questions),
                'current_category': current_category
            })

        else:
            if question is None or answer is None or difficulty is None or category is None:
                abort(400)

            try:
                question = Question(question=question, answer=answer, difficulty=difficulty, category=category)
                question.insert()

                return jsonify({
                    'success': True,
                })

            except:
                abort(422)

    '''
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''

    '''
    @TODO: 
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''
    @app.route('/categories/<int:category_id>/questions')
    def retrieve_questions_by_given_category(category_id):
        questions = db.session.query(Question).filter(Question.category == category_id).all()
        questions_by_category = paginate_questions(request, questions)

        if len(questions) == 0:
            abort(404)

        # Waiting for the explanation of what to put on this parameter
        current_category = db.session.query(Category).get(category_id).format()

        return jsonify({
            'success': True,
            'questions': questions_by_category,
            'total_questions': len(questions),
            'current_category': current_category
        })

    '''
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        body = request.get_json()

        previous_questions = body.get('previous_questions', None)
        quiz_category = body.get('quiz_category', None)

        if quiz_category['type'] == 'click':
            current_category = 0
        else:
            current_category = quiz_category['type']['id']
        
        #Check if category exists, 0 means all categories, so it's acceptable
        if current_category != 0:
            check_category = db.session.query(Category).get(current_category)
            if check_category is None:
                abort(404)

        if current_category == 0:
            questions = db.session.query(Question).all()
        else:
            questions = db.session.query(Question).filter(Question.category == current_category).all()

        questions_ids = [question.id for question in questions]
        """
        If the previous_questions and questions_ids lists have the same length, it means there are
        no question
        """
        if len(previous_questions) == len(questions_ids):
            random_question = False
    
        else:
            new_question = False
            while not new_question:
                random_question = random.choice(questions_ids)
                if random_question not in previous_questions:
                    new_question = True

            random_question = db.session.query(Question).get(random_question).format()

        return jsonify({
            'success': True,
            'question': random_question
        })

    '''
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not found'
        }), 404

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable entity'
        }), 422

    return app

    