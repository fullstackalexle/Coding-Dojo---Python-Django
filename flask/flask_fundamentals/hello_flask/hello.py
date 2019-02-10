from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
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
	return 'Hello %s!' % (name)
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
@app.route('/success')
def success():
  return "success"
@app.route('/<error>')
def error(error):
	return "Sorry! No response. Try again."
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.