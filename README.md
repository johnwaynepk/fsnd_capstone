# Full Stack Capstone Agency Project

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the Postgres database.  

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the agency_backup.psql file provided. From the `starter` folder in terminal run:
```bash
createdb agency
psql agency < agency_backup.psql 
```

## Running the server

From within the `starter` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py;
export FLASK_ENV=development
flask run --reload
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## Endpoints
GET '/movies'
- Fetch a list of movies, each of which has id, title and release date.
- Request Arguments: None
- Returns: An object that includes a list of movies, number of total movies, and success status. 
- Sample: curl http://localhost:5000/movies

{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/actors'
- Fetch a list of actors, each of which has id, name, age and gender. 
- Request Arguments: None
- Returns: An object that includes a list of actors, number of total actors, and success status. 
- Sample: curl http://localhost:5000/movies
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
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
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }
  ], 
  "success": true, 
  "total_questions": 23
}

POST '/movies'
- Post a new movie, which will require the title, release date and cast names. 
- Request Arguments: A json object that includes title, release date, and a list of cast names.
- Returns: An object that includes the movie details, cast names and success status. 
- Sample: curl -X PATCH -H "Content-Type: application/json" -d ‘{“title”:”Big”, “releaseDate”:”1988-1-1”, “actors_names”:[”Tom Hanks”]}’ http://localhost:5000/movies
{
  "added question": "What movie earned Tom Hanks his third straight Oscar nomination in 1996?", 
  "success": true
}

POST '/actors'
- Post a new actor, which will require the name, age, and gender. 
- Request Arguments: A json object that includes name, age and gender.
- Returns: An object that includes the actor name, and success status. 
- Sample: curl -X PATCH -H "Content-Type: application/json" -d ‘{“name”:“Tom Hanks”, “age”:63, “gender”:“male”}’ http://localhost:5000/actors
{
  "added question": "What movie earned Tom Hanks his third straight Oscar nomination in 1996?", 
  "success": true
}

DELETE '/movies/<movie_id>'
- DELETE movie using a movie ID. 
- Request Arguments: None.
- Returns: An object that includes the id and title of the deleted movie, and success status. 
- Sample: curl -X DELETE http://localhost:5000/movies/37

DELETE '/actors/<actor_id>'
- DELETE actor using an actor ID. 
- Request Arguments: None.
- Returns: An object that includes the id and name of the deleted movie, and success status. 
- Sample: curl -X DELETE http://localhost:5000/actors/37

PATCH '/movies/<movie_id>'
- Patch a new movie, which will require the title, release date or cast names. 
- Request Arguments: A json object that includes title, release date, or a list of cast names.
- Returns: An object that includes the updated movie details, cast names and success status. 
- Sample: curl -X PATCH -H "Content-Type: application/json" -d ‘{“title”:”Big”, “releaseDate”:”1988-1-1”, “actors_names”:[”Tom Hanks”]}’ http://localhost:5000/movies/3
{
  "added question": "What movie earned Tom Hanks his third straight Oscar nomination in 1996?", 
  "success": true
}

PATCH '/actors/<actor_id>'
- Patch a new actor, which will require the name, age, or gender. 
- Request Arguments: A json object that includes name, age or gender.
- Returns: An object that includes the updated actor details, and success status. 
- Sample: curl -X PATCH -H "Content-Type: application/json" -d ‘{“name”:“Tom Hanks”, “age”:63, “gender”:“male”}’ http://localhost:5000/actors/3
{
  "added question": "What movie earned Tom Hanks his third straight Oscar nomination in 1996?", 
  "success": true
}

## AUTH0 and Permissions
API permissions
-  `delete: actors`
-  `delete: movies`
-  `get: actors`
-  `get: movies`
-  `patch: actors`
-  `patch: movies`
-  `post: actors`
-  `post: movies`

Roles
- Casting Assistant
    -  `get: actors`
    -  `get: movies`
- Casting Director
    -  `delete: actors`
    -  `get: actors`
    -  `get: movies`
    -  `patch: actors`
    -  `patch: movies`
    -  `post: actors`
- Executive Producer
    - can perform all actions

## Error Handling
Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 400,
    "message": "Bad request"
}
The API will return three error types when requests fail:

400: Bad Request
401: Unauthorized
404: Not Found
422: Unprocessable
405: Method not Allowed
500: Internal Server Error

## Endpoints Testing
The role of Executive Producer is used. To run the tests, run
```
dropdb agency_test
createdb agency_test
psql agency_test < agency_backup.psql 
python test_app.py 
```
## Role-based Testing
Test endpoints with [Postman](https://getpostman.com). 
- Import the postman collection `./starter/udacity-fsnd-capstone.postman_collection.json`
- Run the collection and correct any errors.