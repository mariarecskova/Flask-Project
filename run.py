#!flask/bin/python
from app import app
HOST='127.0.0.1:5000/'
# Starting on my server, your ip address may be different.
app.run(host=HOST, debug=True)