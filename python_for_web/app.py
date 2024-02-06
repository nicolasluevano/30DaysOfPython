from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/thirty_days_of_python'
app.config['SECRET_KEY'] = 'secret_key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

app.app_context().push()


#create Models direcotry and add all models to it
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    country = db.Column(db.String())
    city = db.Column(db.String())
    age = db.Column(db.Integer())

    def __repr__(self):
        return f"Student('{self.name}', '{self.country}, '{self.city}', '{self.age}')"


@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    students_list = []

    for student in students:
        student_data = {
            'id': student.id,
            'name': student.name,
            'country': student.country,
            'city': student.city,
            'age': student.age
        }
        students_list.append(student_data)

    return Response(json.dumps(students_list), mimetype='application/json')
    # return jsonify([student.to_json() for student in students])

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')


@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        content = request.form.get('content')
        words = content.split()
        word_set = set(words)
        content_length = len(words)

        def letter_count(content):
            count = 0
            for letter in content:
                count += 1
            return count

        def most_frequent_word(words):
            freq_word = words[0]
            count = 0
            for word in words:
                current_frequency = words.count(word)
                if current_frequency > count:
                    count = current_frequency
                    freq_word = word
            return freq_word
        
        def word_dict(words):
            word_dict = {}
            for word in words:
                if word not in word_dict:
                    word_dict[word] = 1
                elif word in word_dict:
                    word_dict[word] += 1
            sorted_dict = dict(sorted(word_dict.items(), key=lambda x:x[1], reverse=True))
            return sorted_dict

        total_letters = letter_count(content)
        most_freq_word = most_frequent_word(words)
        sorted_dict = word_dict(words)

        return render_template(
            'result.html',
            content=content,
            content_length=content_length,
            total_letters=total_letters,
            most_freq_word=most_freq_word,
            word_set=word_set,
            sorted_dict=sorted_dict
        )


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
    return redirect(url_for('result'))


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host='0.0.0.0', port=port)