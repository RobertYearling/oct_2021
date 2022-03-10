from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.trip_model import Trip
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/travels')
def get_all():
    if 'user_id' not in session:
        return redirect('/')
    trips = Trip.get_all()
    return render_template('travels.html', trips = trips)

# Add New Trip take us to the page
@app.route('/add_destination')
def add_travel():
    return render_template('new_trip.html')

# Going to Add New Trip
@app.route('/add_new', methods=['POST'])
def add_new():
    data = {
        'destination' : request.form['destination'],
        'description' : request.form['description'],
        'from_date' : request.form['from_date'],
        'to_date' : request.form['to_date'],
        'user_id' : session['user_id']
    }
    Trip.create_trip(data)
    return redirect('/travels')


#  View Trip
@app.route('/trip/<int:trip_id>')
def get_one(trip_id):
    data = {
        'id' : trip_id
    }
    trip = Trip.get_one(data)
    return render_template('trip.html', trip = trip)