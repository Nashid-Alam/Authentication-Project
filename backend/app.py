import re
from flask import Flask,render_template,request

app = Flask (__name__)

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

        return render_template('success.html')



if __name__ == '__main__':
    app.debug =True
    app.run()
