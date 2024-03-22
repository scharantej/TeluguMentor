
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    exercises = db.relationship('Exercises', backref='lesson', lazy=True)

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    lessons = Lessons.query.all()
    return render_template('lessons.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson = Lessons.query.get_or_404(lesson_id)
    exercises = Exercises.query.filter_by(lesson_id=lesson_id).all()
    return render_template('lesson.html', lesson=lesson, exercises=exercises)

@app.route('/exercises')
def exercises():
    exercises = Exercises.query.all()
    return render_template('exercises.html', exercises=exercises)

@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    if request.method == 'POST':
        answer = request.form.get('answer')
        exercise_id = request.form.get('exercise_id')
        exercise = Exercises.query.get_or_404(exercise_id)

        if answer == exercise.answer:
            return redirect(f'/lesson/{exercise.lesson_id}')
        else:
            return redirect('/exercises')

if __name__ == '__main__':
    app.run(debug=True)
