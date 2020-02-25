# Full Stack Capstone Agency Project

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the Postgres database.  

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the agency_backup.psql file provided. From the `04_capstone` folder in terminal run:
```bash
createdb agency
psql agency < agency_backup.psql 
```

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py;
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## Endpoints
GET '/movies'
- Fetch a list of movies, each of which has id, title and release date.
- Request Arguments: None
- Returns: An object that includes a list of movies, number of total movies, and success status. 
- Sample: curl http://localhost:5000/movies
{
    "movies": [
        {
            "id": 1,
            "release date": "Wed, 01 Jan 1986 00:00:00 GMT",
            "title": "Splash"
        },
        {
            "id": 2,
            "release date": "Fri, 01 Jan 1988 00:00:00 GMT",
            "title": "Big"
        }
    ],
    "success": true,
    "total_movies": 2
}

GET '/actors'
- Fetch a list of actors, each of which has id, name, age and gender. 
- Request Arguments: None
- Returns: An object that includes a list of actors, number of total actors, and success status. 
- Sample: curl http://localhost:5000/actors
{
    "actors": [
        {
            "age": 42,
            "gender": "male",
            "id": 1,
            "name": "Zheng Xu"
        },
        {
            "age": 63,
            "gender": "male",
            "id": 5,
            "name": "Tom Hanks"
        },
        {
            "age": 53,
            "gender": "female",
            "id": 6,
            "name": "Robin Wright"
        },
        {
            "age": 64,
            "gender": "male",
            "id": 7,
            "name": "Gary Sinise"
        }
    ],
    "success": true,
    "total_actors": 4
}

POST '/movies'
- Post a new movie, which will require the title, release date and cast names. 
- Request Arguments: A json object that includes title, release date, and a list of cast names.
- Returns: An object that includes the movie details, cast names and success status. 
- Sample: curl -X POST -H "Content-Type: application/json" -d ‘{“title”:”Catch me if you can”, “releaseDate”:”2002-12-25”, “actors_names”:[”Tom Hanks”]}’ http://localhost:5000/movies
{
    "added movie": {
        "id": 19,
        "release date": "Wed, 25 Dec 2002 00:00:00 GMT",
        "title": "Catch me if you can"
    },
    "cast": [
        {
            "age": 63,
            "gender": "male",
            "id": 5,
            "name": "Tom Hanks"
        }
    ],
    "success": true
}

POST '/actors'
- Post a new actor, which will require the name, age, and gender. 
- Request Arguments: A json object that includes name, age and gender.
- Returns: An object that includes the actor name, and success status. 
- Sample: curl -X POST -H "Content-Type: application/json" -d ‘{“name”:“Tom Hanks”, “age”:63, “gender”:“male”}’ http://localhost:5000/actors
{
    "added actor": "Tom Hanks",
    "success": true
}

DELETE '/movies/<movie_id>'
- DELETE movie using a movie ID. 
- Request Arguments: None.
- Returns: An object that includes the id and title of the deleted movie, and success status. 
- Sample: curl -X DELETE http://localhost:5000/movies/37
{
    "deleted_id": 37,
    "deleted_movie": "Catch me if you can",
    "success": true
}

DELETE '/actors/<actor_id>'
- DELETE actor using an actor ID. 
- Request Arguments: None.
- Returns: An object that includes the id and name of the deleted movie, and success status. 
- Sample: curl -X DELETE http://localhost:5000/actors/37
{
    "deleted_actor": "Tom Cruise",
    "deleted_id": 37,
    "success": true
}

PATCH '/movies/<movie_id>'
- Patch a new movie, which will require the title, release date or cast names. 
- Request Arguments: A json object that includes title, release date, or a list of cast names.
- Returns: An object that includes the updated movie details, cast names and success status. 
- Sample: curl -X PATCH -H "Content-Type: application/json" -d ‘{“title”:”Splash”, “releaseDate”:”1986-1-1”, “actors_names”:[”Tom Hanks”]}’ http://localhost:5000/movies/3
{
    "cast": [Tom Hanks],
    "success": true,
    "updated movie": {
        "id": 3,
        "release date": "Wed, 01 Jan 1986 00:00:00 GMT",
        "title": "Splash"
    }
}

PATCH '/actors/<actor_id>'
- Patch a new actor, which will require the name, age, or gender. 
- Request Arguments: A json object that includes name, age or gender.
- Returns: An object that includes the updated actor details, and success status. 
- Sample: curl -X PATCH -H "Content-Type: application/json" -d ‘{“name”:“Tom Hanks”, “age”:63, “gender”:“male”}’ http://localhost:5000/actors/3
{
    "success": true,
    "updated actor": {
        "age": 63,
        "gender": "male",
        "id": 3,
        "name": "Tom Hanks"
    }
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
```bash
dropdb agency_test
createdb agency_test
psql agency_test < agency_backup.psql 
python test_app.py 
```
## Heroku Deployment and Testing
App is hosted at: https://fsnd-capstonejl.herokuapp.com/

### Authentication
User can use the [Auth0 link](https://jwayne.auth0.com/authorize?audience=Agency&response_type=token&client_id=usDFtt1QNqLnQo5zalQLj48HU1cwt1KA&redirect_uri=https://fsnd-capstonejl.herokuapp.com/) to sign up or log in.
3 demo users have been set up for testing:
- Casting Assistant
    -  email: jl@gmail.com
    -  password: mypassword123!`
- Casting Director
    -  email: liujw2000@hotmail.com
    -  password: mypassword123!
- Executive Producer
    -  email: welt.liu@gmail.com
    -  password: mypassword123!

### Role-based Testing
Test Heroku endpoints with [Postman](https://getpostman.com). 
- Import the postman collection `./udacity-fsnd-capstone.postman_collection.json`
- Run the collection.