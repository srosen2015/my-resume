from flask_script import Manager
from my_resume import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    berkow = Professor(name='Kathryn Berkow', department='Accounting & MIS')
    wang = Professor(name='Jiannan Wang', department='Accounting & MIS')
    spotts = Professor(name='Robert Spotts', department='Accounting & MIS')
    sicilia = Professor(name='Dominic Sicilia', department='Business Administration')
    course1 = Course(course_number= 'MISY 262', title='Fundamentals of Business Analytics', description='Learning how to use the basic tools and methods of data analytics for business.')
    course2 = Course(course_number='MISY 350', title='Web Application Development', description='Fundamentals of web development, including Python and Flask.')
    course3 = Course(course_number='MISY 225', title='Introduction to Programming Business Applications', description='Learning how to use Java.')
    course4 = Course(course_number='BUAD 309', title='Introduction to Organization Behavior', description='Management of the marketing functions in different business aspects.')
    db.session.add(berkow)
    db.session.add(wang)
    db.session.add(spotts)
    db.session.add(sicilia)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
