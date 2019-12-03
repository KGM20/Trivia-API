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


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response


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

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection),
            'categories': current_categories,
        })


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


    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()

        question = body.get('question', None)
        answer = body.get('answer', None)
        difficulty = body.get('difficulty', None)
        category = body.get('category', None)
        searchTerm = body.get('searchTerm', None)

        if searchTerm:
            questions = db.session.query(Question) \
                        .filter(Question.question.ilike('%'+searchTerm+'%')) \
                        .all()
            search_questions = paginate_questions(request, questions)

            if len(questions) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'questions': search_questions,
                'total_questions': len(questions)
            })

        else:
            if not question or not answer:
                abort(400)

            try:
                question = Question(question=question, answer=answer,
                                    difficulty=difficulty, category=category)
                question.insert()

                return jsonify({
                    'success': True,
                })

            except:
                abort(422)


    @app.route('/categories/<int:category_id>/questions')
    def retrieve_questions_by_given_category(category_id):
        questions = db.session.query(Question).filter(Question.category
                    == category_id).all()
        questions_by_category = paginate_questions(request, questions)

        if len(questions) == 0:
            abort(404)

        current_category = db.session.query(Category).get(category_id) \
                           .format()

        return jsonify({
            'success': True,
            'questions': questions_by_category,
            'total_questions': len(questions),
            'current_category': current_category
        })


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
            questions = db.session.query(Question) \
                        .filter(Question.category == current_category).all()

        questions_ids = [question.id for question in questions]
        """
        If the previous_questions and questions_ids lists have the same length
        it means there are no questions left
        """
        if len(previous_questions) == len(questions_ids):
            random_question = False
    
        else:
            new_question = False
            while not new_question:
                random_question = random.choice(questions_ids)
                if random_question not in previous_questions:
                    new_question = True

            random_question = db.session.query(Question).get(random_question) \
                              .format()

        return jsonify({
            'success': True,
            'question': random_question
        })


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

    @app.errorhandler(500)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error'
        }), 500

    return app

    