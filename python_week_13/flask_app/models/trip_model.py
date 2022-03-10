from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User

db = 'trip_db'

class Trip:
    def __init__(self, data):
        self.id = data['id']
        self.destination = data['destination']
        self.description = data['description']
        self.from_date = data['from_date']
        self.to_date = data['to_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM trips"
        results = connectToMySQL(db).query_db(query)
        # print(results)
        trips = []
        for trip in results:
            trips.append(cls(trip))
        return trips

    @classmethod
    def create_trip(cls, data):
        query = """
                INSERT INTO trips ( destination, description, from_date, to_date, user_id )
                VALUES ( %(destination)s, %(description)s, %(from_date)s,  %(to_date)s,  %(user_id)s );
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM trips WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])