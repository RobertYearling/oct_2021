from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL

db = 'trip_db'

class User():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create_user(cls, data):
        query = """
                INSERT INTO users ( name, user_name, email, password )
                VALUES ( %(name)s, %(user_name)s, %(email)s, %(pw_hash)s );
                """
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def user_validator(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['name']) < 3:
            flash('Name must be at least 3 characters')
            is_valid = False
        if len(data['user_name']) < 3:
            flash('Username must be at least 3 characters')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        # Check to see if the Email is already in the db
        # query = "SELECT * FROM users WHERE email = %(email)s"
        # results = connectToMySQL('login_reg').query_db(query, data)
        # ---------------
        # Check to see if the Email is already in the db
        connection = connectToMySQL(db)
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connection.query_db(query, data)
        if len(results) != 0:
            flash('This email is already being used')
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Password does not matchie")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])