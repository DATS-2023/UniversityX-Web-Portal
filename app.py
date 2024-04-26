"""
This is the main module for the WheelEase application. 
It contains the Flask app and the routes for the application.
"""
from config import Config
from flask import Flask, render_template, request, redirect, url_for, jsonify
import datafunc 
import os
from dataclasses import dataclass

@dataclass
class Courses:
    id:int
    title:str
    departmentid:int
    credit:int
    weight:str

@dataclass
class Courseschedule:
    id:int
    term:int
    termyear:int
    room_id:int
    course_id:int
    instructor_id:int
    weekday:int
    start_time:int
    duration:int

@dataclass
class Department:
    id: int
    name: str
    managerid: int

@dataclass
class Enrollment:
    id: int
    termyear: int
    grade: int
    student_id: int
    course_id: int

@dataclass
class Instructor:
    id:int
    name:str
    department_id:int

@dataclass
class Room:
    id: int
    name: str

@dataclass
class Student:
    id: int
    firstname: str
    lastname: str


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
    courses = [Courses(course[0],course[1],course[2],course[3],course[4]) for course in datafunc.get_table("course")]

    return render_template('courses.html', courses = courses)

@app.route('/scheduling')
def scheduling():
    schedules = [Courseschedule(schedule[0], schedule[1], schedule[2], schedule[3], schedule[4], schedule[5], schedule[6], schedule[7], schedule[8]) for schedule in datafunc.get_table('courseschedule')]
    return render_template('scheduling.html', schedules=schedules)

@app.route('/enrollment')
def enrollment():
    enrollments = [Enrollment(enrollment[0], enrollment[1], enrollment[2], enrollment[3], enrollment[4]) for enrollment in datafunc.get_table('enrollment')]
    return render_template('enrollment.html', enrollments=enrollments)

@app.route('/instructors')
def instructors():
      instructors = [Instructor(instructor[0], instructor[1], instructor[2]) for instructor in datafunc.get_table('instructor')]
      return render_template('instructors.html', instructors=instructors)

@app.route('/rooms')
def rooms():
    rooms = [Room(room[0],room[1]) for room in datafunc.get_table("room")]

    return render_template('rooms.html', rooms = rooms)

@app.route('/rooms/add', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        room_name = request.form['title']
        
        datafunc.add_table('room', 'name', room_name )
    return render_template('add_room.html')

@app.route('/students/get')
def get_students():
    students = [Student(student[0], student[1], student[2]) for student in datafunc.get_table('student')]
    return render_template('students.html', students=students)

@app.route('/login')
def login():
     return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
