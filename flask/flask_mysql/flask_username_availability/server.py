from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL 

app = Flask(__name__)
app.secret_key = 'sdf796sdfj987dsfsf8ds0982dfl'

@app.route("/")
def index():
    return render_template("wall.html")

@app.route("/username", methods=['POST'])
def username():
    found = False
    mysql = connectToMySQL('ajaxWall')        # connect to the database
    query = "SELECT username from users WHERE users.username = %(user)s;"
    data = { 'user': request.form['username'] }
    result = mysql.query_db(query, data)
    if result:
        found = True
    return render_template('partials/username.html', found=found)  # render a partial and return it
    # Notice that we are rendering on a post! Why is it okay to render on a post in this scenario?
    # Consider what would happen if the user clicks refresh. Would the form be resubmitted?

@app.route("/usersearch")
def search():
    if len(request.args.get('name')) > 0:
        mysql = connectToMySQL("ajaxWall")
        query = "SELECT * FROM users WHERE username LIKE %%(name)s;"
        data = {
            "name" : request.args.get('name') + "%"  # get our data from the query string in the url
        }
        results = mysql.query_db(query, data)
        print(results)
        if results != False:
            return render_template("success.html", users = results) # render a template which uses the results
        else:
            return render_template("wall.html")
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)