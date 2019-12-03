# Full Stack API Final Project

## Full Stack Trivia

This project is a trivia application created with the wish of learning and acquire experience as a full-stack developer. 
Users can do the following actions within the app:

- Display questions - both all questions and by category. 
- Delete questions.
- Add questions and require that they include question and answer text.
- Search for questions based on a text query string.
- Play the quiz game, randomizing either all questions or within a specific category.

This is a part of the Full-Stack Web Developer Nanodegree course of Udacity, designed to focus on applying skills to struct and implement API endpoints.

The backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

## Full Stack Trivia API  Frontend

### Getting Setup

#### Installing Dependencies

##### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

##### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

### Running Your Frontend

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## Full Stack Trivia API Backend

### Getting Started

#### Installing Dependencies

##### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

##### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

### Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Reference

### Base URL

This API runs on your local computer, using the server provided by Flask framework, which the default port to work is the 5000.
```
http://localhost:5000
      or
http://127.0.0.1:5000
```
If you have configured your Flask to run on another port, then you change the '5000' for the port you selected to work on.

### Error Handling

#### Response Codes

All the errors are returned in JSON format with the following structure:
```
{
	'success': False,
	'error': 422,
	'message': 'unprocessable entity'
}
```

#### Error types

The API handles the following error codes:
  
- 400: Bad Request
- 404: Not Found
- 405: Method Not Allowed
- 422: Unprocessable entity
- 500: Internal server error

### Endpoints

- GET '/categories'
- GET '/questions'
- GET '/categories/integer:category_id/questions'
- POST '/questions'
- POST '/quizzes'
- DELETE '/questions/integer:question_id'

#### GET /categories

- Returns a dictionary of category objects and a success argument.
- Request Arguments: None.
- Sample: `curl http://127.0.0.1:5000/categories`
 ```
{
	'1' : "Science",
	'2' : "Art",
	'3' : "Geography",
	'4' : "History",
	'5' : "Entertainment",
	'6' : "Sports"
}
```

#### GET /questions

- Returns a dictionary of category objects, a list of questions from all categories with a pagination by 10 questions, an integer with total of questions value and a success argument.
- Request Arguments: Optional 'page' with integer value starting from 1, if not provided is 1 by default.
- Sample: `curl http://127.0.0.1:5000/questions?page=1`
 ```
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 23
}
```

#### GET /categories/integer:category_id/questions

- Returns a list of questions from the category id provided on URL with a pagination by 10 questions, an integer with total of questions value, a dictionary with the current category object and a success argument.
- Request Arguments: Optional 'page' with integer value starting from 1, if not provided is 1 by default.
- Sample: `curl http://127.0.0.1:5000/categories/3/questions?page=1`
 ```
{
  "current_category": {
    "id": 5,
    "type": "Entertainment"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Skyshock",
      "category": 5,
      "difficulty": 3,
      "id": 30,
      "question": "Who is the most popular League of Legends caster in Latin America?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

#### POST /questions

The route will look for creating questions if there is no 'searchTerm' index on the JSON object argument provided.

##### For creating questions

- Creates a new question using the submitted questions, answer, category and difficulty. Returns a success value.
- Request Arguments: A JSON object with question object structure (string:question, string:answer, integer:category and integer:difficulty)
- Sample: `curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question": "2 + 2?", "answer": "4", "category": 1, "difficulty": 1}'`
 ```
{
  "success": true
}
```

##### For searching questions

- Returns a list of questions that match (case-insensitive and partial string) the search term on the question string with a pagination by 10 questions, an integer with total of questions value and a success argument.
- Request Arguments: A JSON object with 'searchTerm' index with string value. Optional 'page' with integer value starting from 1, if not provided is 1 by default.
- Sample: `curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"searchTerm": "title"}'`
 ```
{
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}

```

#### POST /quizzes

- Returns a question object from the category provided on the arguments, if not category provided, the returned question will be any category, the question will be randomly selected and it cannot repeat from the ones on the list of previous questions argument, if there are no questions left that can be selected, then returns a question argument with False value.
- Request Arguments: A JSON object with the previous questions list and a type dictionary with a category object.
- Sample: `curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": {"id": 2, "type": "Art"}}}'`
```
{
  "question": {
    "answer": "Escher",
    "category": 2,
    "difficulty": 1,
    "id": 16,
    "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
  },
  "success": true
}
```

#### DELETE /questions/integer:question_id

- Deletes a question that matches the given id on the URL. Returns a success value.
- Request Arguments: None
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/13`
 ```
{
  "success": true
}
```

## Authors

Frontend by Udacity Developers Team
Backend by Kevin "KGM20" Cruz