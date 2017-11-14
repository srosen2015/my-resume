from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/courses')
def all_courses():
    courses = [
        ['MISY262', 'Fundamentals of Business Analytics', 'You will learn how to do analytics and prediction models using R programming.'],
        ['MISY350', 'Business Application Development II', 'You will learn full stack web development'],
        ['MISY225', 'Introduction to Programming Business Applications', 'Introduction to Programming Business Applications']
    ]
    return render_template('all-courses.html', courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    app.run()
