from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Request, url_for, redirect, render_template ,session
from flask_login import *
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'sanya123'

db = SQLAlchemy(app)
login_manager = LoginManager()

# login_manager.init_app(app)
def _init_(self, username, email, password):
   self.username = username
   self.email = email
   self.password = password


class User(UserMixin, db.Model):
    username = db.Column(db.String(25), primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(80), nullable=True)

class seats(UserMixin, db.Model):
    seat = db.Column(db.String(25),  unique=True, primary_key=True)
    price = db.Column(db.String(80), nullable=True)

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

def test_connection():
    with app.app_context():
        db.create_all()
        app.run(debug=True)


@app.route('/')
def index():
    return "Hey!"
        
@app.route("/user/signup", methods=["POST"])
def signup():
    if(Request.method == 'POST'):
        req = Request.get_json()
        username = req['username']
        email = req['email']
        password = req['password']
        # check_user = User.query.filter_by(name=name).first()
        obj = User(username=username,email=email,password=password)
        db.session.add(obj)
        db.session.commit()
        return "Signup Successful"
    else:
        return "Signup Unsuccessful"
        
@app.route('/user/signin', methods=['POST'])
def signin():
    if(Request.method == 'POST'):
        req = Request.get_json()
        email = req['email']
        password = req['password']
        check_user = User.query.filter_by(email=email).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return "Logged in successfully"
            else:
                return "Incorrect Password"
        else:
            return "No such user"
        

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('/'))

@app.route('/user/fetch_prices', methods=['POST'])
def fetch_prices():
    if(Request.method=='POST'):
        req=Request.get_json()
        seat = req['seat']
        check_user = seats.query.filter_by(seat=seat).first()
        if(check_user is not None):
           return "Seat found"    
        else:
            return "No Such Seat"

test_connection()

# if __name__ == '__main__':
#     # from waitress import serve
#     app.run(debug=True)