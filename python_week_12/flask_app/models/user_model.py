from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL

db = 'class_demo_db'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = """
                INSERT INTO users ( first_name, last_name, email, password )
                VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s );
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def user_validator(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) < 3:
            flash('First name must be at least 3 characters')
            is_valid = False
        if len(data['last_name']) < 3:
            flash('last name must be at least 3 characters')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is an invalid address")
            is_valid = False
        connect = connectToMySQL(db)
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connect.query_db(query, data)
        if len(results) != 0:
            flash('This email is already being used')
            is_valid = False
        if len(data['password']) < 8:
            flash('Password must be at least 8 characters')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Password no matchie')
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])