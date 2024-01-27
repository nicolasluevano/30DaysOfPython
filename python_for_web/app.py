from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/thirty_days_of_python'
app.config['SECRET_KEY'] = 'secret_key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

app.app_context().push()


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

        total_letters = letter_count(content)
        most_freq_word = most_frequent_word(words)

        return render_template(
            'result.html',
            content=content,
            content_length=content_length,
            total_letters=total_letters,
            most_freq_word=most_freq_word,
            word_set=word_set
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