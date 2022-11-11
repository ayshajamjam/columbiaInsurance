"""
To run locally:
    virtual machine: source virtual/bin/activate
    python3 app.py --debug
Go to http://localhost:8111 in your browser.

References (code taken from online sites):
Login/Authentication: https://github.com/PrettyPrinted/youtube_video_code/blob/master/2020/02/10/Creating%20a%20Login%20Page%20in%20Flask%20Using%20Sessions/flask_session_example/app.py

After cloning, make virtual env
source virtual/bin/activate
export FLASK_ENV=development
export FLASK_APP=app.py
Pip install flask
pip install Flask-SQLAlchemy
pip3 install Flask-WTF
To fix psycopg2 error:
sudo pip3 install psycopg2-binary
pip install psycopg2-binary --user

Tips: If you get a NoType error, just delete your cookies
"""

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, flash, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, DateField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'databases'

DATABASEURI = "postgresql://aj2604:316@34.75.94.195/proj1part2"
engine = create_engine(DATABASEURI)

current_user = None

# Create a Form Class
class NewUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    uni = StringField("UNI", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    school = StringField("School", validators=[DataRequired()])
    submit = SubmitField("Submit")
class LoginForm(FlaskForm):
    uni = StringField("UNI", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
class NewReviewForm(FlaskForm):
    date_of_visit = DateField("Date of Visit", validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=1, max=5)])
    review_content = TextAreaField("Review Content", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Runs at beginning of every web request; sets up db connection
@app.before_request
def before_request():
    try:
        g.conn = engine.connect()
        g.user = current_user

    except:
        print("uh oh, problem connecting to database")
        import traceback; traceback.print_exc()
        g.conn = None

# Runs at end of every web request; closes the database connection
# If you don't, the database could run out of memory
@app.teardown_request
def teardown_request(exception):
  try:
    g.user = current_user
    g.conn.close()
  except Exception as e:
    pass

# ROUTES

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/doctors')
def doctors():
    cursor = g.conn.execute("SELECT * FROM doctors")
    all_doctors = []
    for result in cursor:
        all_doctors.append(result)
    cursor.close()
    context = dict(data = all_doctors)

    return render_template("doctors.html", **context)

@app.route('/doctors/<npi>')
def doctor(npi):
    cursor = g.conn.execute("SELECT * FROM doctors")
    doctor_info = []
    for result in cursor:
        if result['npi'] == npi:
            doctor_info.append(result)
    cursor.close()

    cursor = g.conn.execute("SELECT * FROM doctors AS D, writes AS W, reviews AS R WHERE D.npi = W.npi AND W.review_id=R.review_id")
    doctor_reviews = []
    for result in cursor:
        if result['npi'] == npi:
            doctor_reviews.append(result)
    cursor.close()
    
    context = dict(info = doctor_info[0], reviews = doctor_reviews)
    return render_template("doctor.html", **context)

@app.route('/users')
def users():
    cursor = g.conn.execute("SELECT * FROM studentPatients")
    all_users = []
    for result in cursor:
        all_users.append(result)
    cursor.close()
    context = dict(data = all_users)
    return render_template("users.html", **context)

@app.route('/users/<uni>')
def user(uni):
    if not current_user or g.user != uni:
        flash("You do not have access to other students' profiles")
        return redirect(url_for('users'))

    # Get only user information
    cursor = g.conn.execute("SELECT * FROM studentPatients")
    user_info = []
    for result in cursor:
        if result['uni'] == uni:
            user_info.append(result)
    cursor.close()
    
    # Get specific user + saved doctors
    cursor = g.conn.execute("SELECT * FROM studentPatients AS S, saves AS V, doctors AS D WHERE S.uni = V.uni AND D.npi=V.npi")
    saved_doctors = []
    for result in cursor:
        if result['uni'] == uni:
            saved_doctors.append(result)
    cursor.close()

    # Get specific user + reviews
    cursor = g.conn.execute("SELECT * FROM studentPatients AS S, writes AS W, reviews AS R WHERE S.uni = W.uni AND W.review_id=R.review_id")
    user_revs = []
    for result in cursor:
        if result['uni'] == uni:
            user_revs.append(result)
    cursor.close()
    
    # Get specific user + appointments
    cursor = g.conn.execute("SELECT * FROM studentPatients AS S, doctors AS D, appointments AS A, schedules AS H WHERE S.uni = H.uni AND D.npi = H.npi AND A.apt_id=H.apt_id")
    user_apts = []
    for result in cursor:
        if result['uni'] == uni:
            user_apts.append(result)
    cursor.close()

    context = dict(info = user_info[0], saved = saved_doctors, reviews = user_revs, appointments = user_apts)
    return render_template("user.html", **context)

@app.route('/newUser', methods=['GET','POST'])
def newUser():
    first_name = None
    last_name = None
    uni = None
    password = None
    age = None
    school = None
    form = NewUserForm()
    if form.validate_on_submit():
        # Grab information
        first_name = form.first_name.data
        last_name = form.last_name.data
        uni = form.uni.data
        password = form.password.data
        age = form.age.data
        school = form.school.data
        # Set fields empty again
        form.first_name.data = ''
        form.last_name.data = ''
        form.uni.data = ''
        form.password.data = ''
        form.age.data = ''
        form.school.data = ''
        # Push to database
        args = (first_name, last_name, uni, password, age, school)
        # g.conn.execute("INSERT INTO studentpatients VALUES (%s, %s, %s, %s, %d, %s)", args)
        flash("Form Submitted Successfully")
    return render_template("newUser.html", 
        first_name=first_name,
        last_name = last_name,
        uni = uni,
        password = password,
        age = age,
        school = school,
        form=form)

@app.route('/reviews/<review_id>')
def review(review_id):
    cursor = g.conn.execute("SELECT * FROM doctors AS D, writes AS W, reviews AS R WHERE D.npi = W.npi AND W.review_id=R.review_id")
    review_result = []
    for result in cursor:
        if result['review_id'] == int(review_id):
            review_result.append(result)
    cursor.close()
    context = dict(data = review_result[0])

    return render_template("review.html", **context)

@app.route('/newReview/<npi>', methods=['POST', 'GET'])
def newReview(npi):
    date_of_visit = None
    rating = None
    review_content = None

    form = NewReviewForm()
    if form.validate_on_submit():
        date_of_visit = form.date_of_visit.data
        rating = form.rating.data
        review_content = form.review_content.data
        form.date_of_visit.data = ''
        form.rating.data = ''
        form.review_content.data = ''

        args = (date_of_visit, rating, review_content)
        # g.conn.execute("INSERT INTO reviews VALUES (%s, %s, %s, %d, %s)", args)
        flash("Form Submitted Successfully")
    return render_template("newReview.html",
        date_of_visit = date_of_visit,
        rating = rating,
        review_content = review_content,
        form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Find correct user
            cursor = g.conn.execute("SELECT * FROM studentpatients")
            users = []
            for result in cursor:
                if result['uni'] == form.uni.data:
                    users.append(result)
            cursor.close()
            
            if users:
                user = users[0]
                # Password verification
                if(form.password.data == user['password']):
                    flash("Login successful")
                    global current_user 
                    current_user = user.uni
                    url = 'users/' + str(user.uni)
                    return redirect(url)
                else:
                    flash("Wrong Password")
            else:
                flash("User does not exist")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    global current_user
    if current_user == None:
        flash("No one is signed in")
    else:
        flash("Logout Successful")
        current_user = None
    return redirect(url_for('index'))

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
