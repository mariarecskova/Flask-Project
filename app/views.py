from flask import Flask, jsonify, render_template, url_for
from app import app
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template ('home.html')

@app.route("/layout")
def layout():
	return render_template ('layout.html')

@app.route("/yoga")
def yoga():
	return render_template ('yoga.html')

@app.route("/massage")
def massage():
	return render_template ('massage.html')

@app.route("/contact")
def contact():
	return render_template ('contact.html')

@app.route("/pricelist")
def pricelist():
	return render_template ('pricelist.html')

if __name__ == '__main__':
	app.run(debug=True)