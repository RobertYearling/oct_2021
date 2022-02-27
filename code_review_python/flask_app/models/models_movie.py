from flask_app.config.mysqlconnection import connectToMySQL

db = 'movies_db'

class Movie:
    def __init__(self, data) :
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.genre = data['genre']
        self.release_date = data['release_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies"
        results = connectToMySQL(db).query_db(query)
        movies = []
        for movie in results:
            movies.append(cls(movie))
        return movies

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO movies ( title, description, genre, release_date )
                VALUES ( %(title)s, %(description)s, %(genre)s, %(release_date)s );
                """
        return connectToMySQL(db).query_db(query, data)