# Half-Moon- my yoga teacher webapp, built on a Flask webserver with Bootstrap templates


## Core Files

[.gitignore](gitignore) - I put my .venv and __pycache__ files here

[Procfile](Procfile) - This is specific to Heroku deployment, and possibly other enviroments

[requirements.txt](requirements.txt) - This file is used to keep track of all the libraries that need to be installed. 

		pip install -r requirements.txt

[run.py](run.py) - This file specifies the server setup

		python run.py

[runtime.txt](runtime.txt) - This is another file specific to Heroku deployment. It specifies which version of Python should be used for the project. 

[app/__init__.py](app/__init__.py) - This is where the app is initialized. 

[app/views.py](app/views.py) - This is where I listed the templates to render, each of them with routes. 

SETUP (for Windows 10):

1. Python 3.4 or higher, installed with pip.

2. Install virtualenv via pip: pip install virtualenv

3. Open command line- with cd command, navigate to the folder you want to create your project in- then: mkdir project name

4. Create a new virtual environment - `virtualenv venv`

5. activate the virtual environment by `venv\Scripts\activate`

6. install Flask inside of our virtual environment: pip install flask

7. with cd, navigate to the app folder

8. set environment variable FLASK_APP to the name of our app, run: set FLASK_APP=views.py

9. run the server with: `flask run`

10. copy the web link that was output after running the server, and paste it to your browser: http://127.0.0.1:5000/
navigate through the pages: http://127.0.0.1:5000/yoga, /massage, /contact, /pricelist
