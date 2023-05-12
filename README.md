Motivation
I am in software industry where having knowledge of full stack development will help people do their job efficiently. I developed this project to make use of the knowledge acquired in this nanodegree and hence gain confidence in these skills. This is also an opportunity for me to contribute something to the open-source community by building this full stack project.

Intro : FSND-capstone-project
The Udacity Fullstack Developer Nanodegree Capstone Project builds an API from scratch and hosts it using all the knowledge and abilities learned in the courses.


Casting Agency Specifications
* The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
 Models:
    * Movies with attributes title and release date
    * Actors with attributes name, age and gender
 Endpoints:
    * GET /actors and /movies
    * DELETE /actors/ and /movies/
    * POST /actors and /movies and
    * PATCH /actors/ and /movies/
 Roles:
    * Casting Assistant
        * Can view actors and movies
    * Casting Director
        * All permissions a Casting Assistant has and�
        * Add or delete an actor from the database
        * Modify actors or movies
    * Executive Producer
        * All permissions a Casting Director has and�
        * Add or delete a movie from the database
 Tests:
    * One test for success behavior of each endpoint
    * One test for error behavior of each endpoint
    * At least two tests of RBAC for each role

Local Development Setup
    Setup virtual environment:
    To create a virtual environment, run the venv module as a script in the FSND-Capstone-Project directory:
        py -m venv env
    Once you've created the virtual environment, activate it.
        source env/Scripts/activate
    Install dependencies
    Use pip to install the required dependencies.
        pip install -r requirements.txt
    Run the server
    Start the server using the FLASK development server:
    On Linux : export
        export FLASK_APP=app.py
        export FLASK_ENV=development # enables debug mode
    On Windows : set
        set FLASK_APP=app.py
        set FLASK_ENV=development # enables debug mode
        flask run

Database setup
    With Postgres running, create a postgres_deployment_capstone_ankita database.
    Populate the database using the agency.psql file provided. In terminal run:
        psql postgres_deployment_capstone_ankita < agency.psql

API Documentation

#### GET '/movies'
Returns a list of all available movies and  success value.
Sample curl: 
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" https://render-deployment-capstone-ankita.onrender.com/movies

Sample response output:
{
    "movies": [
        {
            "id": 2,
            "release": "18-08-2022",
            "title": "Bullet Train"
        },
        {
            "id": 3,
            "release": "13-06-2018",
            "title": "Piku"
        }
    ],
    "success": true
}

#### GET '/actors'
Returns a list of all available actors and  success value.
Sample curl: 
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" https://render-deployment-capstone-ankita.onrender.com/actors

Sample response output:
{
    "actors": [
        {
            "age": "38",
            "gender": "female",
            "id": 1,
            "name": "Blake Lively"
        },
        {
            "age": "39",
            "gender": "female",
            "id": 3,
            "name": "Deepika Padukone"
        },
        {
            "age": "45",
            "gender": "male",
            "id": 4,
            "name": "Brad Pitt"
        }
    ],
    "success": true
}

#### POST '/add-movie'
Returns the new movie posted and a success value.
Sample curl: 
curl https://render-deployment-capstone-ankita.onrender.com/add-movie -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{
    "title":"Piku",
    "release":"13-06-2018"
}'
Sample response output:
{
    "movie": {
        "id": 3,
        "release": "13-06-2018",
        "title": "Piku"
    },
    "success": true
}

#### POST '/add-actor'
Returns the new actor added and a success value.
Sample curl: 
curl https://render-deployment-capstone-ankita.onrender.com/add-actor -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{
    "name":"Brad Pitt",
    "age":"45",
    "gender":"male"
}'
Sample response output:
{
    "actor": {
        "age": "45",
        "gender": "male",
        "id": 4,
        "name": "Brad Pitt"
    },
    "success": true
}

#### PATCH '/movies/<int:id>'
Returns the updated movie and a success value.
Sample curl:
curl https://render-deployment-capstone-ankita.onrender.com/movies/1 -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{
    "title":"Red",
    "release":"17-10-2022"
}'
Sample response output:
{
    "movie": {
        "id": 1,
        "release": "17-10-2022",
        "title": "Red"
    },
    "success": true
}

#### PATCH '/actors/<int:id>'
Returns the updated actor and a success value.
Sample curl:
curl https://render-deployment-capstone-ankita.onrender.com/actors/1 -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{
    "name":"Blake Lively",
    "age":"38",
    "gender":"female"
}'
Sample response output:
{
    "actor": {
        "age": "38",
        "gender": "female",
        "id": 1,
        "name": "Blake Lively"
    },
    "success": true
}

#### DELETE '/movies/<int:id>'
Returns the id of the deleted movie and a success value.
curl https://render-deployment-capstone-ankita.onrender.com/movies/1 -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" 

Sample response output:
{
    "delete": 1,
    "success": true
}

#### DELETE '/actors/<int:id>'
Returns the id of the deleted actor and a success value.
curl https://render-deployment-capstone-ankita.onrender.com/actors/2 -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" 

Sample response output:
{
    "delete": 2,
    "success": true
}

Run the Server
    From within the ./src directory first ensure you are working using your created virtual environment.

    To run the server, execute:

        chmod +x setup.sh
        source setup.sh

Running the API
    API endpoints can be accessed via https://render-deployment-capstone-ankita.onrender.com

    Auth0 information for endpoints that require authentication can be found in setup.sh.



