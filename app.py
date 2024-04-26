"""
This is the main module for the WheelEase application. 
It contains the Flask app and the routes for the application.
"""
from config import Config
from flask import Flask, render_template, request, redirect, url_for, jsonify
import datafunc
import os

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

@app.route('/')
def home():
    """
    Home page route
    """ 
    return render_template('home.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/scheduling')
def scheduling():
    return render_template('courses.html')

@app.route('/enrollment')
def enrollment():
     return render_template('enrollment.html')

@app.route('/instructors')
def instructors():
      return render_template('instructors.html')

@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

@app.route('/login')
def login():
     return render_template('login.html')

@app.route('/students/get')
def get_students():
    return datafunc.get_students()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
