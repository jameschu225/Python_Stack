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

        all_users = []
        for row in result:
            all_users.append(cls(row))

        return all_users 

    @classmethod
    def create(cls, data):
        query = """INSERT INTO USERS (first_name, last_name, email, created_at) values (%(fname)s, %(lname)s, %(email)s, now());"""

        return connectToMySQL('users_shcema').query_db(query, data)
    
    @classmethod
    def delete(cls, user_id):
        query = """DELETE from USERS where id = %(delete_id)s"""
        data = {
            'delete_id': user_id
        }
        return connectToMySQL('users_shcema').query_db(query, data)
    
    @classmethod
    def get_one(cls, user_id):
        query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM USERS WHERE id =%(select_id)s ;"
        data = {
                'select_id': user_id
                }
        result = connectToMySQL('users_shcema').query_db(query, data)

        one_user = result
        
        return one_user
    
    @classmethod
    def update(cls, data):
        query = "UPDATE USERS SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = now() WHERE id =%(id)s;"

        return connectToMySQL('users_shcema').query_db(query, data)