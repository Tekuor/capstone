# Casting Agency

This project is the capstone project for my Udacity Fullstack Developer nanodegree. The project is to help simplify the process of creating movies and managing and assigning actors to those movies. There are 3 main users of this system these are: Executive Producer, Casting Director ans Casting Assistant. The Casting Assistant can view actors and movies. The Casting Director can add or delete actors, modify actors and movies and view actors and movies. The Executive Producer can perform all acctions the Casting Assistant and Casting Director can perform including adding or deleting a movie.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 

## Getting Started

### Pre-requisites and Local Development 
Developers using this project should already have Python3, pip and node installed on their local machines.

#### Frontend
The frontend for this project can be found in this repository https://github.com/Tekuor/capstone_frontend#capstone-frontend
#### Backend

From the root folder run `pip install requirements.txt`. All required packages are included in the requirements file with environment variables in the setup.sh file. 

To run the application run the following commands: 
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `app.py` file in our root folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

### Tests
In order to run tests navigate to the backend folder and run the following commands: 

```
dropdb agency_test
createdb agency_test
python test.py
```

The first time you run the tests, omit the dropdb command. 

All tests are kept in that file and should be maintained as updates are made to app functionality.

### API Reference
All endpoints require a Bearer token. The role a user has determines what they can access.
#### Casting Assistant
Can view actors and movies

#### Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies

#### Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database
## Error Handling
Errors are returned as JSON objects in the following format:

```bash
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
The API will return one of these error types when requests fail:

404: Resource Not Found
422: Not Processable
500: server error
400: bad request
401: unauthorized
403: forbidden
405: invalid method
409: duplicate resource
```

## GET /movies
General:
Returns a list of movie objects and success value
Sample: curl http://127.0.0.1:5000/movies

```bash
{
    "movies": [
        {
            "id": 1,
            "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg",
            "release_date": "Mon, 07 Jun 2021 00:00:00 GMT",
            "title": "The princess and the frog"
        }
    ],
    "success": true
}
```

## GET /actors
General:
Returns a list of actor objects and success value
Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
Sample: curl http://127.0.0.1:5000/actors

```bash
{
    "actors": [
        {
            "age": 25,
            "gender": "female",
            "id": 1,
            "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg",
            "name": "Actor1"
        }
    ],
    "success": true
}
```

## POST /actors
General:
Creates a new actor using the name, age , gender and image_url. Returns the id of the created question, success value, total actors, and actor list.
curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{
    "name":"Actor1",
    "age": 25,
    "gender":"female",
    "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg"
}'

```bash
{
    "actors": [
        {
            "age": 25,
            "gender": "female",
            "id": 1,
            "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg",
            "name": "Actor1"
        }
    ],
    "created": 1,
    "success": true,
    "total_actors": 1
}
```

## POST /movies
General:
Creates a new movie using the title, release_date, and image_url. Returns the id of the created question, success value, total movies, and movie list.
curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{
    "title":"The princess and the frog",
    "release_date":"2021/06/07",
    "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg"
}'

```bash
{
    "actors": [
        {
            "age": 25,
            "gender": "female",
            "id": 1,
            "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg",
            "name": "Actor1"
        }
    ],
    "created": 1,
    "success": true,
    "total_actors": 1
}
```

## PATCH /movies/{movie_id}
General:
Updates the movie of the given ID if it exists. Returns the movie object of the updated movie and success value.
curl -X PATCH http://127.0.0.1:5000/movies/1 -X PATCH -H "Content-Type: application/json" -d '{
    "title": "The princess"
}'
```bash
{
    "movie": {
        "id": 1,
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg",
        "release_date": "Mon, 07 Jun 2021 00:00:00 GMT",
        "title": "The princess"
    },
    "success": true
}
```

## PATCH /actors/{actor_id}
General:
Updates the actor of the given ID if it exists. Returns the actor object of the updated actor and success value.
curl -X PATCH http://127.0.0.1:5000/actors/1 -X PATCH -H "Content-Type: application/json" -d '{
    "name": "Actor2"
}'
```bash
{
    "actor": {
        "age": 25,
        "gender": "female",
        "id": 2,
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Princess_and_the_Frog_poster.jpg/220px-The_Princess_and_the_Frog_poster.jpg",
        "name": "Actor2"
    },
    "success": true
}
```

## DELETE /movies/{movie_id}
General:
Deletes the movie of the given ID if it exists. Returns the id of the deleted movie, success value, total movies, and movie list.
curl -X DELETE http://127.0.0.1:5000/movies/1
```bash
{
    "deleted": 1,
    "movies": [],
    "success": true,
    "total_movies": 0
}
```

## DELETE /actors/{actor_id}
General:
Deletes the actor of the given ID if it exists. Returns the id of the deleted actor, success value, total actors, and actor list.
curl -X DELETE http://127.0.0.1:5000/actors/1
```bash
{
    "actors": [],
    "deleted": 1,
    "success": true,
    "total_actors": 0
}
```

### Deployment
The project is deployed on heroku and can be accessed with this link https://casting-agency-pro.herokuapp.com
### Authors
Gifty Mate-Kole
