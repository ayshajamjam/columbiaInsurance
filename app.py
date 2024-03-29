"""
To run locally:
    virtual machine: source virtual/bin/activate
    python3 app.py --debug
Go to http://localhost:8111 in your browser.

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
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, DateField, TextAreaField, TimeField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import TextArea

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'databases'

DATABASEURI = "postgresql://aj2604:316@34.75.94.195/proj1part2"
engine = create_engine(DATABASEURI)

current_user = None

# Create a Form Class

class LoginForm(FlaskForm):
    uni = StringField("UNI", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
class NewUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    uni = StringField("UNI", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    school = StringField("School", validators=[DataRequired()])
    submit = SubmitField("Submit")
class EditUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    # uni = StringField("UNI", validators=[DataRequired()])
    # password = PasswordField("Password", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    school = StringField("School", validators=[DataRequired()])
    submit = SubmitField("Submit")
class NewReviewForm(FlaskForm):
    date_of_visit = DateField("Date of Visit", validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=1, max=5)])
    content = TextAreaField("Review Content", validators=[DataRequired()])
    submit = SubmitField("Submit")
class EditReviewForm(FlaskForm):
    date_of_visit = DateField("Date of Visit", validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=1, max=5)])
    content = TextAreaField("Review Content", validators=[DataRequired()])
    submit = SubmitField("Submit")
class NewAptForm(FlaskForm):
    apt_date = DateField("Date of Appointment", validators=[DataRequired()])
    apt_time = TimeField("Time of Appointment", validators=[DataRequired()])
    concern_description = TextAreaField("Concern Description", validators=[DataRequired()])
    submit = SubmitField("Submit")
class EditAptForm(FlaskForm):
    apt_date = DateField("Date of Appointment", validators=[DataRequired()])
    apt_time = TimeField("Time of Appointment", validators=[DataRequired()])
    concern_description = TextAreaField("Concern Description", validators=[DataRequired()])
    submit = SubmitField("Submit")
class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
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

    # Check if doctor is saved by current user
    cursor = g.conn.execute("SELECT * FROM saves AS S WHERE S.npi=%s AND S.uni=%s", npi, current_user)
    saved = cursor.fetchone()
    cursor.close()
    
    context = dict(info = doctor_info[0], reviews = doctor_reviews, saved=saved)
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
    cursor = g.conn.execute("SELECT * FROM hospitals AS Q, studentPatients AS S, doctors AS D, appointments AS A, schedules AS H WHERE Q.cms = H.cms AND S.uni = H.uni AND D.npi = H.npi AND A.apt_id=H.apt_id")
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
        g.conn.execute("INSERT INTO studentpatients VALUES (%s, %s, %s, %s, %s, %s)", args)
        global current_user
        current_user = uni
        g.user = current_user
        return redirect("/users/" + current_user)

    return render_template("newUser.html", 
        first_name=first_name,
        last_name = last_name,
        uni = uni,
        password = password,
        age = age,
        school = school,
        form=form)

@app.route('/users/<uni>/edit', methods=['GET','POST'])
def editUser(uni):

    # Get this user's information
    cursor = g.conn.execute("SELECT * FROM studentPatients")
    user_info = []
    for result in cursor:
        if result['uni'] == uni:
            user_info.append(result)
    cursor.close()
    user = user_info[0]

    # Populate form with current information
    form = EditUserForm(request.form, obj = user)

    if form.validate_on_submit():
        # Grab new information
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        school = form.school.data

        # Set fields empty again
        form.first_name.data = ''
        form.last_name.data = ''
        form.age.data = ''
        form.school.data = ''
       
        # Push edits to database
        g.conn.execute("UPDATE studentpatients SET first_name=%s, last_name=%s, age=%s, school=%s WHERE uni=%s", first_name, last_name, age, school, uni)

        flash("Profile Information Updated Successfully")
        global current_user
        current_user = uni
        g.user = current_user
        return redirect("/users/" + current_user)

    return render_template("editUser.html", form=form)

@app.route('/users/<uni>/delete', methods=['GET','DELETE'])
def deleteUser(uni):
    # Push delete to database
    g.conn.execute("DELETE FROM studentpatients WHERE uni=%s", uni)

    flash("Profile Deleted")
    global current_user
    current_user = None
    return redirect('/login')

@app.route('/reviews/<review_id>')
def review(review_id):

    # Find the student who wrote the review
    cursor = g.conn.execute("SELECT uni FROM writes WHERE review_id=%s", review_id)
    writer = cursor.fetchone()
    cursor.close()

    # Get review information
    cursor = g.conn.execute("SELECT * FROM doctors AS D, writes AS W, reviews AS R WHERE D.npi = W.npi AND W.review_id=R.review_id")
    review_result = []
    for result in cursor:
        if result['review_id'] == int(review_id):
            review_result.append(result)
    cursor.close()
    context = dict(data = review_result[0], writer = writer[0])

    return render_template("review.html", **context)

@app.route('/newReview/<npi>', methods=['POST', 'GET'])
def newReview(npi):

    if not current_user:
        flash("Please login to leave a review")
        return redirect("/login")

    date_of_visit = None
    rating = None
    content = None

    form = NewReviewForm()
    if form.validate_on_submit():
        date_of_visit = form.date_of_visit.data
        rating = form.rating.data
        content = form.content.data

        form.date_of_visit.data = ''
        form.rating.data = ''
        form.content.data = ''

        # Get new review id
        review_id = str(add_to_review_count())

        args_review = (review_id, date_of_visit, content, rating)
        g.conn.execute("INSERT INTO reviews VALUES (%s, %s, %s, %s)", args_review)

        date_written = datetime.now()
        args_writes = (npi, current_user, review_id, date_written)
        g.conn.execute("INSERT INTO writes VALUES (%s, %s, %s, %s)", args_writes)

        return redirect("/reviews/" + review_id)

    return render_template("newReview.html",
        date_of_visit = date_of_visit,
        rating = rating,
        content = content,
        form=form)

def add_to_review_count():
    cursor = g.conn.execute("SELECT max(review_id) FROM reviews")
    count = cursor.fetchone()[0] + 1
    cursor.close()
    return count

@app.route('/reviews/<review_id>/edit', methods=['POST', 'GET'])
def editReview(review_id):

    if not current_user:
        flash("Please login to edit your review")
        return redirect("/login")

    cursor = g.conn.execute("SELECT * FROM writes WHERE review_id=%s AND uni=%s", review_id, current_user)
    student = cursor.fetchone()
    cursor.close()

    if not student:
        flash("You do not have access to edit other students' reviews")
        return redirect("/users/" + current_user)

    # Get this review's information
    cursor = g.conn.execute("SELECT * FROM reviews WHERE review_id=%s", review_id)
    review = cursor.fetchone()
    # cursor.close() <<<<<<<<<<<<<< Do I need this?

    # Populate form with current information
    form = EditReviewForm(request.form, obj = review)

    if form.validate_on_submit():
        # Grab new information
        date_of_visit = form.date_of_visit.data
        rating = form.rating.data
        content = form.content.data

        # Set fields empty again
        form.date_of_visit.data = ''
        form.rating.data = ''
        form.content.data = ''
       
        # Push edits to database
        g.conn.execute("UPDATE reviews SET date_of_visit=%s, rating=%s, content=%s WHERE review_id=%s", date_of_visit, rating, content, review_id)

        return redirect("/reviews/" + str(review['review_id']))

    return render_template("editReview.html", form=form)

@app.route('/reviews/<review_id>/delete', methods=['GET','DELETE'])
def deleteReview(review_id):

    if not current_user:
        flash("Please login to delete your review")
        return redirect("/login")

    cursor = g.conn.execute("SELECT * FROM writes WHERE review_id=%s AND uni=%s", review_id, current_user)
    student = cursor.fetchone()
    cursor.close()

    if not student:
        flash("You do not have access to delete other students' reviews")
        return redirect("/users/" + current_user)


    # Push delete to database
    g.conn.execute("DELETE FROM writes WHERE review_id=%s", review_id)
    g.conn.execute("DELETE FROM reviews WHERE review_id=%s", review_id)

    flash("Review Deleted")
    return redirect("/users/" + current_user)

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
        current_user = None
    return redirect(url_for('index'))

@app.route("/doctors/<npi>/save")
def save(npi):
    if not current_user:
        flash("Please login to save a doctor first")
        return redirect(url_for('login'))
    else:
        # Push to database
        args = (current_user, npi)
        g.conn.execute("INSERT INTO saves VALUES (%s, %s)", args)
        return redirect("/doctors/" + npi)

@app.route('/doctors/<npi>/save/delete', methods=['GET','DELETE'])
def deleteSave(npi):

    if not current_user:
        flash("Please login to remove this doctor from your saved list")
        return redirect("/login")
    
    # Push delete to database
    g.conn.execute("DELETE FROM saves WHERE npi=%s AND uni=%s", npi, current_user)
    return redirect("/doctors/" + npi)

@app.route('/apts/<apt_id>')
def apt(apt_id):

    cursor = g.conn.execute("SELECT * FROM schedules WHERE apt_id=%s AND uni=%s", apt_id, current_user)
    student = cursor.fetchone()
    cursor.close()

    if not current_user or not student:
        flash("You do not have access to other students' appointment information")
        return redirect(url_for('users'))

    cursor = g.conn.execute("SELECT * FROM studentPatients AS P, doctors AS D, appointments AS A, schedules AS S, works_at AS W WHERE W.cms = S.cms AND P.uni = S.uni AND D.npi = S.npi AND W.npi = D.npi AND A.apt_id=S.apt_id AND A.apt_id=%s", apt_id)
    apt_result = cursor.fetchone()
    cursor.close()

    # Get Hospital information
    cursor = g.conn.execute("SELECT * FROM hospitals AS H, schedules as S WHERE H.cms = S.cms AND S.npi = %s", apt_result['npi'])
    hospital_info = cursor.fetchone()
    cursor.close()
    context = dict(data = apt_result, hospital = hospital_info)

    return render_template("apt.html", **context)

@app.route('/newApt/<npi>', methods=['POST', 'GET'])
def newApt(npi):

    if not current_user:
        flash("Please login to book an appointment")
        return redirect("/login")

    apt_date = None
    apt_time = None
    concern_description = None

    form = NewAptForm()

    if form.validate_on_submit():
        apt_date = form.apt_date.data
        apt_time = form.apt_time.data
        concern_description = form.concern_description.data

        form.apt_date.data = ''
        form.apt_time.data = ''
        form.concern_description.data = ''

        # Get new appointment id
        apt_id = str(add_to_apt_count())

        args_apt = (apt_id, apt_date, apt_time, concern_description)
        g.conn.execute("INSERT INTO appointments VALUES (%s, %s, %s, %s)", args_apt)

        # Get Hospital information
        cursor = g.conn.execute("SELECT * FROM hospitals AS H, schedules as S WHERE H.cms = S.cms AND S.npi = %s", npi)
        hospital_info = cursor.fetchone()
        cursor.close()

        args_schedules = (npi, hospital_info['cms'], apt_id, current_user)
        g.conn.execute("INSERT INTO schedules VALUES (%s, %s, %s, %s)", args_schedules)

        return redirect("/apts/" + apt_id)

    return render_template("newApt.html",
        apt_date = apt_date,
        apt_time = apt_time,
        concern_description = concern_description,
        form=form)

def add_to_apt_count():
    cursor = g.conn.execute("SELECT max(apt_id) FROM appointments")
    count = cursor.fetchone()[0] + 1
    cursor.close()
    return count

@app.route('/apts/<apt_id>/edit', methods=['POST', 'GET'])
def editApt(apt_id):

    if not current_user:
        flash("Please login to edit an appointment")
        return redirect("/login")

    cursor = g.conn.execute("SELECT * FROM schedules WHERE apt_id=%s AND uni=%s", apt_id, current_user)
    student = cursor.fetchone()
    cursor.close()

    if not student:
        flash("You do not have access to edit other students' appointments")
        return redirect("/users/" + current_user)

    # Get this apts's information
    cursor = g.conn.execute("SELECT * FROM appointments WHERE apt_id=%s", apt_id)
    apt = cursor.fetchone()
    cursor.close()

    # Populate form with current information
    form = EditAptForm(request.form, obj = apt)

    if form.validate_on_submit():
        # Grab new information
        apt_date = form.apt_date.data
        apt_time = form.apt_time.data
        concern_description = form.concern_description.data

        # Set fields empty again
        form.apt_date.data = ''
        form.apt_time.data = ''
        form.concern_description.data = ''

        # Push edits to database
        g.conn.execute("UPDATE appointments SET apt_date=%s, apt_time=%s, concern_description=%s WHERE apt_id=%s", apt_date, apt_time, concern_description, apt_id)

        flash("Appointment Updated Successfully")
        return redirect("/apts/" + str(apt['apt_id']))

    return render_template("editApt.html", form=form)

@app.route('/apts/<apt_id>/delete', methods=['GET','DELETE'])
def deleteApt(apt_id):

    if not current_user:
        flash("Please login to delete an appointment")
        return redirect("/login")

    cursor = g.conn.execute("SELECT * FROM schedules WHERE apt_id=%s AND uni=%s", apt_id, current_user)
    student = cursor.fetchone()
    cursor.close()

    if not student:
        flash("You do not have access to delete other students' appointments")
        return redirect("/users/" + current_user)
    
    # Push delete to database
    g.conn.execute("DELETE FROM schedules WHERE apt_id=%s", apt_id)
    g.conn.execute("DELETE FROM appointments WHERE apt_id=%s", apt_id)

    flash("Appointment Cancelled")
    return redirect("/users/" + current_user)

# Pass stuff to base.html; will pass thing
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    
    docs = []

    # Get data from search box
    query = form.searched.data
    query = query.strip()

    if(len(query) == 0):
        return redirect('/doctors')

    if form.validate_on_submit():

        # Query by specialty or description
        q = f'%{query}%'
        cursor = g.conn.execute("SELECT * FROM doctors WHERE first_name ILIKE %s OR last_name ILIKE %s OR job_title ILIKE %s OR about ILIKE %s", q, q, q, q)
        for result in cursor:
            if (result not in docs):
                docs.append(result)
        cursor.close()

    docs_set = list(set(docs))
    context = dict(data = docs_set)

    return render_template("search_doc.html", **context, form=form, searched=query)


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
