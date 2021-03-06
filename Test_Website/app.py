import sqlalchemy
import pymysql
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Column, Integer, Text
import csv

from flask import Flask, jsonify, render_template
import config

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{config.pw}@127.0.0.1:3306/wine_db'

# reflect an existing database into a new model
Base = automap_base()
engine = create_engine(f'mysql+pymysql://root:{config.pw}@127.0.0.1:3306/wine_db')

# reflect the tables
Base.prepare(engine, reflect=True)
# matching that of the table name.
# Wine = Base.classes.wine
session = Session(engine)

# class User(db.Model):
#      __table__ = 'users'
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(64),
#         index=False,
#         unique=True,
#         nullable=False)
#     email = db.Column(db.String(80),
#         index=True,
#         unique=True,
#         nullable=False)
#     created = db.Column(db.DateTime,
#         index=False,
#         unique=False,
#         nullable=False)
#     bio = db.Column(db.Text,
#         index=False,
#         unique=False,
#         nullable=True)
#     admin = db.Column(db.Boolean,
#         index=False,
#         unique=False,
#         nullable=False)
                      
                      
#     def __repr__(self):
#         return '<User {}>'.format(self.username)



class MyClass(Base):
    __table__ = Table('wine', Base.metadata,
  
    Column('browser',Text), 
    Column('cabsauv', Integer), 
    Column('pinotnoir', Integer), 
    Column('syrah', Integer),
    Column('sangiovese', Integer), 
    Column('merlot'),
    Column('malbec', Integer), 
    Column('sauvblanc'),
    Column('chard', Integer),
    Column('cheninblanc', Integer),
    Column('reisling', Integer),
    Column('gerwurtzraminer', Integer), 
    extend_existing=True, autoload=True, autoload_with = engine
    )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wine')
def wine():
    return render_template('wine.html')

@app.route('/wine_map')
def wine_map():

    return render_template('wine_map.html')

@app.route("/cabsauv")
def cab():

    return render_template('cabsauv.html')

@app.route("/sauvblanc")
def sb():

    return render_template('sauvblanc.html')

@app.route("/syrah")
def syrah():
    return render_template('syrah.html')

@app.route("/merlot")
def merlot():
    return render_template('merlot.html')

@app.route("/pinotnoir")
def pinonoir():
    return render_template('pinonoir.html')

@app.route("/malbec")
def malbec():
    return render_template('malbec.html')

@app.route("/chard")
def chard():
    return render_template('chard.html')

@app.route("/chenblan")
def chenblan():
    return render_template('chenblan.html')

@app.route("/reisling")
def reisling():
    return render_template('reisling.html')

@app.route("/cabsauv_data", methods= ['GET'])
def cab_data():

    cab = session.query(MyClass.__table__)
    cabdf = pd.DataFrame(cab)
    cabfinal_df = cabdf[['browser','cabsauv']]
    
    return cabfinal_df.to_json(orient = 'records')

@app.route("/syrah_data", methods = ['GET'])
def syrah_data():

    syrah = session.query(MyClass.__table__)
    syrahdf = pd.DataFrame(syrah)
    syrahfinal_df = syrahdf[['browser','syrah']]
    
    return syrahfinal_df.to_json(orient = 'records')

@app.route("/merlot_data", methods = ['GET'])
def merlot_data():

    merlot = session.query(MyClass.__table__)
    merlotdf = pd.DataFrame(merlot)
    merlotfinal_df = cabdf[['browser','merlot']]
    
    return merlotfinal_df.to_json(orient = 'records')

@app.route("/pinotnoir_data", methods = ['GET'])
def pinotnoir_data():

    pinotnoir = session.query(MyClass.__table__)
    pinotnoirdf = pd.DataFrame(pinotnoir)
    pinotnoirfinal_df = pinotnoirdf[['browser','pinotnoir']]
    
    return pinotnoirfinal_df.to_json(orient = 'records')

@app.route("/sangiovese_data", methods = ['GET'])
def sangiovese_data():

    sangiovese = session.query(MyClass.__table__)
    sangiovesedf = pd.DataFrame(sangiovese)
    sangiovesefinal_df = sangiovesedf[['browser','sangiovese']]
    
    return sangiovesefinal_df.to_json(orient = 'records')


@app.route("/sauvblanc_data", methods = ['GET'])
def sauvblanc_data():

    sauvblanc = session.query(MyClass.__table__)
    sauvblancdf = pd.DataFrame(sauvblanc)
    sauvblancfinal_df = sauvblancdf[['browser','sauvblanc']]
    
    return sauvblancfinal_df.to_json(orient = 'records')

@app.route("/chard_data", methods = ['GET'])
def chard_data():
 
    chard = session.query(MyClass.__table__)
    charddf = pd.DataFrame(chard)
    chardfinal_df = charddf[['browser','chard']]
    
    return chardfinal_df.to_json(orient = 'records')

@app.route("/gerwurtz_data", methods = ['GET'])
def gerwurtz_data():

    gerwurtz = session.query(MyClass.__table__)
    gerwurtzdf = pd.DataFrame(gerwurtz)
    gerwurtzfinal_df = gerwurtzdf[['browser','gerwurtz']]
    
    return gerwurtzfinal_df.to_json(orient = 'records')

@app.route("/cheninblanc_data", methods = ['GET'])
def cheninblanc_data():

    cheninblanc = session.query(MyClass.__table__)
    cheninblancdf = pd.DataFrame(cheninblanc)
    cheninblancfinal_df = cheninblancdf[['browser','cheninblanc']]
    
    return cheninblancfinal_df.to_json(orient = 'records')

@app.route("/reisling_data", methods = ['GET'])
def reisling_data():
    
    reisling = session.query(MyClass.__table__)
    reislingdf = pd.DataFrame(reisling)
    reislingfinal_df = reislingdf[['browser','reisling']]
    
    return reislingfinal_df.to_json(orient = 'records')

# @app.route('/contact', methods=['GET', 'POST'])
# def app_user():
#     if request.method == "POST":
#         details = request.form
#         firstName = details['fname']
#         lastName = details['lname']
#         email = details['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO MyUsers(firstName, lastName, email) VALUES (%s, %s, %s)", (firstName, lastName, email))
#         mysql.connection.commit()
#         cur.close()
#         return 'success'
# #     return render_template('contact.html')

# @app.route('/contact', methods=['GET'])
# def create_user():
#     """Create a user."""
#     username = request.args.get('user')
#     email = request.args.get('email')
#     if username and email:
#         new_user = User(username=username,
#                         email=email,
#                         admin=False)
#         db.session.add(new_user)  # Adds new User record to database
#         db.session.commit()  # Commits all changes
#     return make_response(f"{new_user} successfully created!")

if __name__ == '__main__':
       app.run(debug=True)
