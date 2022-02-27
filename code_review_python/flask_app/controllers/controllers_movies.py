from flask_app import app
from flask import render_template, request, redirect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_movie import Movie

db = "movies_db"

@app.route('/')
def index():
    return render_template('index.html', movies = Movie.get_all())

# add a new movie
# takes us to the form page
@app.route('/add_movie')
def add_movie():
    return render_template('new_movie.html')

@app.route('/new_movie', methods=['POST'])
def create():
    data = {
        'title' : request.form['title'],
        'description' : request.form['description'],
        'genre' : request.form['genre'],
        'release_date' : request.form['release_date']
    }
    Movie.create(data)
    return redirect('/')