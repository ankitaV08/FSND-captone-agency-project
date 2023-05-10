FSND-capstone-project
The Udacity Fullstack Developer Nanodegree Capstone Project builds an API from scratch and hosts it using all the knowledge and abilities learned in the courses.
Casting Agency Specifications
* The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
* Models:
* Movies with attributes title and release date
* Actors with attributes name, age and gender
* Endpoints:
* GET /actors and /movies
* DELETE /actors/ and /movies/
* POST /actors and /movies and
* PATCH /actors/ and /movies/
* Roles:
* Casting Assistant
* Can view actors and movies
* Casting Director
* All permissions a Casting Assistant has and…
* Add or delete an actor from the database
* Modify actors or movies
* Executive Producer
* All permissions a Casting Director has and…
* Add or delete a movie from the database
* Tests:
* One test for success behavior of each endpoint
* One test for error behavior of each endpoint
* At least two tests of RBAC for each role

Local Development Setup
Setup virtual environment
To create a virtual environment, run the venv module as a script in the FSND-Capstone-Project directory:
py -m venv env
Once you’ve created the virtual environment, activate it.
source env/Scripts/activate
Install dependencies
Use pip to install the required dependencies.
pip install -r requirements.txt
Run the server
Start the server using the FLASK development server:
export FLASK_APP=app
export FLASK_ENV=development # enables debug mode
flask run

