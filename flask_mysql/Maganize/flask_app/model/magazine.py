from flask_app.configs.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.model import user


class magazine:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.user_id = data['user_id']
        self.creator = None
        self.subs = None

    @classmethod
    def get_all_mags_with_creator(cls):
        query = "SELECT * FROM  magazine LEFT JOIN user ON user.id = user_id"

        result = connectToMySQL( "magazines").query_db(query)
        print(result)
        all_mags = []
        for row in result:

                one_mag = cls(row)

                one_mag_creator = {
                    "id" : row["user.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "email" : row["email"],
                    "password" : row["password"],
                }
                creator = user.User(one_mag_creator)

                one_mag.creator = creator

                all_mags.append(one_mag)

        return all_mags
    
    @classmethod
    def get_mag_by_id(cls, mag_id):
        query = "SELECT * FROM magazine WHERE id = %(select_id)s"
        data = {
                'select_id': mag_id
                }
        result = connectToMySQL( "magazines").query_db(query,data)

        return result
    
    @classmethod
    def get_mag_by_creator(cls, user_id):
        query = "SELECT * FROM magazine WHERE user_id = %(select_id)s"
        data = {
                'select_id': user_id
                }
        result = connectToMySQL( "magazines").query_db(query,data)

        return result
    
    @staticmethod
    def mag_validation(data):

            is_valid = True

            if len(data["title"]) <2:
                flash("Title must be at least 2 characters", "create_mag")
                is_valid = False

            if len(data["description"]) <10:
                flash("Description must be at least 10 characters", "create_mag")
                is_valid = False

            return is_valid
    
    @classmethod
    def creat_mag(cls, data):
            query = "INSERT INTO magazine (title, description, user_id) VALUES (%(title)s, %(description)s, %(user_id)s);"

            return connectToMySQL( "magazines").query_db(query, data)
    
    @classmethod
    def delete(cls, mag_id):
        query = """DELETE from magazine where id = %(delete_id)s"""
        data = {
            'delete_id': mag_id
        }
        return connectToMySQL('magazines').query_db(query, data)
    
    @classmethod
    def subscribe(cls, data):
        query = "INSERT INTO magazine_has_user (magazine_id, user_id) VALUES (%(subscribe_id)s, %(user_id)s);"

        return connectToMySQL('magazines').query_db(query, data)
    
    @classmethod
    def get_subscribe_by_mag(cls, mag_id):
        query = "SELECT * FROM magazine_has_user WHERE magazine_id = %(select_id)s"
        data = {
                'select_id': mag_id
                }
        subscribe = connectToMySQL('magazines').query_db(query, data)

        subscriber = []
        for row in subscribe:
            sub = user.User.get_user_by_id(row["user_id"])
            one_mag_subscriber = {
                    "id" : sub["id"],
                    "first_name" : sub["first_name"],
                    "last_name" : sub["last_name"],
                    "email" : sub["email"],
                    "password" : sub["password"],
                }
            suber = user.User(one_mag_subscriber)
            subscriber.append(suber)
        return subscriber
    
    @classmethod
    def get_count_subscribe_by_mag(cls, user_id):
        query = "SELECT *, COUNT(*) FROM magazine_has_user LEFT JOIN magazine ON magazine.id = magazine_id WHERE magazine_has_user.user_id = %(select_id)s GROUP BY magazine_id;"
        data = {
                'select_id': user_id
                }
        count = connectToMySQL('magazines').query_db(query, data)
        all_mags_with_count = []
        for row in count:
            one_mag = cls(row)
                
            one_mag.subs = row["COUNT(*)"]
            all_mags_with_count.append(one_mag)
        return all_mags_with_count