from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Flask"

@app.route('/dessert')
def dessert_one():
    return "I love ice cream"

@app.route('/dessert/<name>')
def desserts(name):
    return f"{name.capitalize()} loves ice cream"

@app.route('/dessert_name/<string:name>')
def dessert_name(name):
    return f"{name} Pie"

@app.route('/flask')
def first_flask():
    return render_template('index.html')

@app.route('/display')
def flask_num():
    return render_template('index.html', html = 5)

@app.route('/display/<int:num>')
def flask_with_num(num):
    return render_template('index.html', html = num)

@app.route('/display/<int:num>/<string:color>')
def flask_with_color(num, color):
    return render_template('index.html', html = num, htmlc = color)

@app.route('/num/<int:x>')
def number(x):
    return str(x)




if __name__=="__main__":
    app.run(debug=True)