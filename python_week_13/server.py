from flask_app import app
from flask_app.controllers import user_controllers
from flask_app.controllers import trip_controllers

if __name__=="__main__":
    app.run(debug=True)