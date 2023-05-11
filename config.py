import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres_deployment_capstone_ankita_user:u68XDYDJhI3FxlCGiWz2MMhFR9YEU1dO@dpg-che17abhp8ubgo1m13jg-a.oregon-postgres.render.com/postgres_deployment_capstone_ankita'
SQLALCHEMY_TRACK_MODIFICATIONS = False
