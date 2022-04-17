
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug =True
    app.config ['SQLALCHEMY_DATABASE_URI']= 'postgresql://localhost/login'
else:
    app.debug =False
    app.config ['SQLALCHEMY_DATABASE_URI']= ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class login(db.Model):
    __tablename__= 'User'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(500))
    last_name=db.Column(db.String(500))
    username=db.Column(db.String(500))
    password=db.Column(db.String(500))

    def __init__(self,first_name,last_name,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first name']
        last_name = request.form['last name']
        username = request.form['username']
        password = request.form['password']

        print(first_name,last_name,username,password)

    if db.session.query(login)!='':
        data = login(first_name,last_name,username,password)
        db.session.add(data)
        db.session.commit()
        return render_template('success.html')



if __name__ == '__main__':
    
    app.run()
