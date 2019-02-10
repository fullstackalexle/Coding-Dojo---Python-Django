from flask import Flask, render_template 
app = Flask(__name__)    

@app.route('/')
def index():
    return render_template('index.html', rows=8, cols=8, bgColor1="red", bgColor2="black")

@app.route('/<x>')
def custom_grid_x(x):
    return render_template('index.html', rows=int(x), cols=8, bgColor1="red", bgColor2="black")

@app.route('/<x>/<y>')
def custom_grid_x_y(x, y):
    return render_template('index.html', rows=int(x), cols=int(y), bgColor1="red", bgColor2="black")

@app.route('/<x>/<y>/<color1>/<color2>')
def custom_grid_and_color(x, y, color1, color2):
    return render_template('index.html', rows=int(x), cols=int(y), bgColor1=color1, bgColor2=color2)

if __name__=="__main__":
    app.run(debug=True)