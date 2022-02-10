from mysqlconnection import connectToMySQL

class Artist:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM artists;'
        results = connectToMySQL('artists_class_db').query_db(query)
        artists = []
        for artist in results:
            artists.append(cls(artist))
        return artists

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO artists ( first_name, last_name, email )
                VALUES ( %(first_name)s, %(last_name)s, %(email)s );
                """
        return connectToMySQL('artists_class_db').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = """
                DELETE FROM artists
                WHERE id = %(id)s;
                """
        return connectToMySQL('artists_class_db').query_db(query, data)