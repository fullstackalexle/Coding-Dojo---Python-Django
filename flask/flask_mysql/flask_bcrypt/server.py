from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)
app.secret_key = 'sdf796sdfj987dsfsf8ds0982dfl'

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/createUser', methods=['POST'])
def create():
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address!")
		return redirect("/")
	if len(request.form['password']) < 1:
		flash("Please provide a password!")
		return redirect("/")
    # include some logic to validate user input before adding them to the database!
    # create the hash		
	pw_hash = bcrypt.generate_password_hash(request.form['password'])
	print(pw_hash)  
    # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'
    # be sure you set up your database so it can store password hashes this long (60 characters)
	mysql = connectToMySQL("bcrypt")
	query = "INSERT INTO users (email, password) VALUES (%(email)s, %(password_hash)s);"
    # put the pw_hash in our data dictionary, NOT the password the user provided
	data = { "email" : request.form['email'],
             "password_hash" : pw_hash }
	mysql.query_db(query, data)
    # never render on a post, always redirect!
	return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    # see if the email provided exists in the database
    mysql = connectToMySQL("bcrypt")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = { "email" : request.form["email"] }
    result = mysql.query_db(query, data)
    if result:
        # assuming we only have one user with this email, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of emails when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            # if we get True after checking the password, we may put the user id in session
            session['userid'] = result[0]['id']
            # never render on a post, always redirect!
            return redirect('/success')
    # if we didn't find anything in the database by searching by email or if the passwords don't match,
    # flash an error message and redirect back to a safe route
    flash("You could not be logged in")
    return redirect("/")

@app.route('/success')
def success():
	mysql = connectToMySQL("bcrypt")
	query = "SELECT * FROM users WHERE id = %s" % (session['userid'])
	data = {}
	result = mysql.query_db(query, data)
	return render_template("show.html", email=result[0]['email'])

if __name__ == "__main__":
    app.run(debug=True)

