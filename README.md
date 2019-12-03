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

###Base URL

This API runs on your local computer, using the server provided by Flask framework, which the default port to work is the 5000.
```
http://localhost:5000
      or
http://127.0.0.1:5000
```
If you have configured your Flask to run on another port, then you change the '5000' for the port you selected to work on.

###Error Handling

####Response Codes

All the errors are returned in JSON format with the following structure:
```
{
	'success': False,
	'error': 422,
	'message': 'unprocessable entity'
}
```

####Error types

The API handles the following error codes:
  
- 400: Bad Request
- 404: Not Found
- 405: Method Not Allowed
- 422: Unprocessable entity
- 500: Internal server error