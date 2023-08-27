from mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM USERS;"

        result = connectToMySQL('users_shcema').query_db(query)
        print(result)

        all_users = []
        for row in result:
            all_users.append(cls(row))

        return all_users 

    @classmethod
    def create(cls, data):
        query = """INSERT INTO USERS (first_name, last_name, email, created_at) values (%(fname)s, %(lname)s, %(email)s, now());"""

        return connectToMySQL('users_shcema').query_db(query, data)
