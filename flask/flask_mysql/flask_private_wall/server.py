from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL 

app = Flask(__name__)
app.secret_key = 'sdf796sdfj987dsfsf8ds0982dfl'

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

import socket

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/show")
def show():
	if session.get('userid'):
		mysql = connectToMySQL("private_wall")
		
		user_query = "SELECT * FROM users WHERE users.id = %(user_id)s;"
		data = {
			"user_id": session['userid']
		}
		user_result = mysql.query_db(user_query, data)

		mysql = connectToMySQL("private_wall")
		messages_query = "SELECT * FROM users JOIN messages ON users.id=messages.sender_id WHERE messages.user_id = %(user_id)s;"
		messages_result = mysql.query_db(messages_query, data)

		mysql = connectToMySQL("private_wall")
		all_users_query = "SELECT * FROM users WHERE id != %(user_id)s;"
		all_users_result = mysql.query_db(all_users_query, data)

		mysql = connectToMySQL("private_wall")
		sent_messages_query = "SELECT * FROM users JOIN messages ON users.id=messages.sender_id WHERE users.id = %(user_id)s;"
		sent_messages_result = mysql.query_db(sent_messages_query, data)

		return render_template("show.html", current_user=user_result[0], messages=messages_result, all_users=all_users_result, sent_messages=sent_messages_result)
	else:
		return redirect("/")

@app.route("/register", methods=['POST'])
def register_user():
	valid = True
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address!")
		valid = False
	if len(request.form['fname']) < 2:
		flash("Please enter a valid first name.")
		valid = False
	if len(request.form['lname']) < 2:
		flash("Please enter a valid last name.")
		valid = False
	if len(request.form['password']) < 8:
		flash("Password should be 8 characters long.")
		valid = False
	if request.form['password'] != request.form['password_confirm']:
		flash("Password did not match confirmation.")
		valid = False

	if valid == False:
		return redirect("/")
	else:
		pw_hash = bcrypt.generate_password_hash(request.form['password'])

		mysql = connectToMySQL("private_wall")
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password_hash)s, NOW(), NOW());"
		data = { 
			"fname": request.form['fname'],
			"lname": request.form['lname'],
			"email": request.form['email'],
			"password_hash": pw_hash
		}
		result = mysql.query_db(query, data)
		session['userid'] = str(result)
		return redirect("/show")

@app.route("/login", methods=['POST'])
def login_user():
	mysql = connectToMySQL("private_wall")
	query = "SELECT * FROM users WHERE email = %(email)s;"
	data = { "email" : request.form["email"] }
	result = mysql.query_db(query, data)
	if result:
		if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
			session['userid'] = str(result[0]['id'])
			return redirect("/show")
	flash("You could not be logged in")
	return redirect("/")

@app.route("/logout")
def logout_user():
	session.clear()
	return redirect("/")

@app.route("/messages/send", methods=['POST'])
def send_message():
	mysql = connectToMySQL("private_wall")
	query = "INSERT INTO messages (content, user_id, sender_id, created_at, updated_at) VALUES (%(content)s, %(user_id)s, %(sender_id)s, NOW(), NOW());"
	data = {
		"content": request.form['message_content'],
		"user_id": request.form['receiver_id'],
		"sender_id": session['userid']
	}
	mysql.query_db(query, data)

	mysql = connectToMySQL("private_wall")
	receiving_user_query = "SELECT * FROM users WHERE users.id = %(user_id)s;"
	data = {
		"user_id": request.form['receiver_id']
	}
	result = mysql.query_db(receiving_user_query, data)

	flash("You just sent a message to %s %s" % (result[0]['first_name'], result[0]['last_name']))
	return redirect("/show")

@app.route("/messages/delete", methods=['POST','DELETE'])
def delete_message():
	mysql = connectToMySQL("private_wall")
	message_query = "SELECT * FROM messages WHERE messages.id = %(message_id)s;"
	data = { "message_id": request.form['delete_message_id'] }
	result = mysql.query_db(message_query, data)

	if int(result[0]['user_id']) == int(session['userid']):
		mysql = connectToMySQL("private_wall")
		query = "DELETE FROM messages WHERE messages.id = %(message_id)s;"
		data = { "message_id": request.form['delete_message_id'] }
		mysql.query_db(query, data)
		flash("You've just deleted a message!")
		return redirect("/show")
	else:
		# ip_address = socket.gethostbyname(socket.gethostname())
		# return render_template("danger.html", message_id=request.form['delete_message_id'], ip_add=ip_address)
		return render_template("danger.html", message_id=request.form['delete_message_id'])

if __name__ == "__main__":
    app.run(debug=True)