from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', phrase="hello", times=5)

def hello_dojo():
	return 'Dojo!'

@app.route('/say/<name>')
def hi_person(name):
	try:
		value = int(name)
		return "Please pass in a name"
	except ValueError:
		pass  # it was a string, not an int.
		return 'Hi %s' % (name)

@app.route('/hello/<name>')
def hello_person(name):
	return render_template("name.html", some_name=name)

@app.route('/repeat/<number>/<word>')
def repeat_word(number, word):
	if number.isdigit() and word.isdigit() == False:
		output = ""
		for i in range(int(number)):
			output += word
		return output
	elif number.isdigit() == False:
		return "Please pass in a number of times to repeat"
	elif word.isdigit() == True:
		return "Please pass in a word that is not a number"

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/play')
def play():
	return render_template("play.html",num=3, bgColor="lightblue")

@app.route('/play/<num_boxes>')
def play_num(num_boxes):
	return render_template("play.html",num=int(num_boxes), bgColor="lightblue")

@app.route('/play/<num_boxes>/<color>')
def play_num_color(num_boxes, color):
	return render_template("play.html",num=int(num_boxes), bgColor=color)

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

@app.route('/success')
def success():
  return "success"

@app.route('/<error>')
def error(error):
	return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.