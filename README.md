# columbiaInsurance

To run locally:

    source virtual/bin/activate
    
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
