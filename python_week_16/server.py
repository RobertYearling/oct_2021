from crypt import methods
from flask import Flask, render_template, request, redirect, session
import requests, os
app = Flask(__name__)

app.secret_key = "Py Is Life"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    zipcode = request.form['zipcode']
    headers = os.environ.get("KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={headers}"
    response = requests.get(url)
    print(response.json())
    # print(response.json()['weather'][0]['main'])
    session['main'] = response.json()['weather'][0]['main']
    # print(response.json()['name'])
    session['name'] = response.json()['name']
    # print(response.json()['main']['temp'])
    session['temp'] = response.json()['main']['temp']
    # print(response.json()['main']['humidity'])
    session['humidity'] = response.json()['main']['humidity']
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)