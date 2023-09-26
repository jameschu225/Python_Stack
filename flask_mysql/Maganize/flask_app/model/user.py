from flask_app.configs.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user"

        allusers = connectToMySQL('magazines').query_db(query)

        return allusers

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s,%(email)s,%(password)s)"

        return connectToMySQL('magazines').query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE user SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id =%(id)s;"

        return connectToMySQL('magazines').query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM user where email = %(email)s"

        result = connectToMySQL('magazines').query_db(query, data)
        login_user = result
        return login_user

    @classmethod
    def get_user_by_id(cls, user_id):
        query = "SELECT * FROM user where id = %(id)s"

        data = {
            "id": user_id
        }

        result = connectToMySQL('magazines').query_db(query, data)
        register_user = result
        return register_user[0]
    
    @staticmethod
    def validation(data, allusers):

        is_valid = True

        if len(data["fname"]) <3:
            flash("First name must be at least 3 characters", "register")
            is_valid = False

        if  data["fname"].isnumeric():
            flash("First name must be String", "register")
            is_valid = False

        if len(data["lname"]) <3:
            flash("Last name must be at least 3 characters", "register")
            is_valid = False

        if  data["lname"].isnumeric():
            flash("Last name must be String", "register")
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!!", "register")
            is_valid = False

        for user in allusers:
            if data["email"] == user["email"]:
                flash("Email already used!!", "register")
                is_valid = False
        
        if len(data["password"]) <8:
            flash("Password must be at least 8 characters", "register")
            is_valid = False

        if data["password"] != data["confirm"]:
            flash("Password does not match", "register")
            is_valid = False           
        
        return is_valid
    
    @staticmethod
    def login_validation(data):

        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!!", 'login')
            is_valid = False

        
        if not User.get_user_by_email(data):
            flash("Email is not registered!!", "login")
            is_valid = False

        if data["password"] == "":
            flash("Invalid password !!", "login")
            is_valid = False

        return is_valid
    
    @staticmethod
    def update_validation(data):

        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!!", 'update_user')
            is_valid = False

        
        if len(data["fname"]) <3:
            flash("First name must be at least 3 characters", "update_user")
            is_valid = False

        if len(data["lname"]) <3:
            flash("Last name must be at least 3 characters", "update_user")
            is_valid = False

        return is_valid