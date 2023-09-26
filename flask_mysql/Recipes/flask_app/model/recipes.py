from flask_app.configs.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.model import user

class Recipe:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def creat_recipe(cls, data):
            query = "INSERT INTO receipt (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"

            return connectToMySQL( "receipt").query_db(query, data)
    
    @classmethod
    def get_all_recipes_with_creator(cls):
        query = "SELECT * FROM user LEFT JOIN receipt ON user_id = user.id "

        result = connectToMySQL( "receipt").query_db(query)
        print(result)
        all_receipts = []
        if "receipt.id" in result:
            for row in result:

                one_receipt = cls(row)

                one_receipt_creator = {
                    "id" : row["id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "email" : row["email"],
                    "password" : row["password"],
                }
                creator = user.User(one_receipt_creator)

                one_receipt.creator = creator

                all_receipts.append(one_receipt)

        return all_receipts
    
    @classmethod
    def get_recipes_by_id(cls,recipt_id):
        query = "SELECT * FROM receipt WHERE id = %(select_id)s"
        data = {
                'select_id': recipt_id
                }
        result = connectToMySQL( "receipt").query_db(query,data)

        return result
    
    @classmethod
    def update(cls, data):
        query = "UPDATE receipt SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id =%(id)s"
        
        return connectToMySQL( "receipt").query_db(query,data)
    @classmethod
    def delete(cls, receipt_id):
        query = """DELETE from receipt where id = %(delete_id)s"""
        data = {
            'delete_id': receipt_id
        }
        return connectToMySQL('receipt').query_db(query, data)

    @staticmethod
    def recipe_validation(data):

            is_valid = True

            if len(data["name"]) <3:
                flash("Name must be at least 3 characters", "create_recipe")
                is_valid = False

            if len(data["description"]) <3:
                flash("Description must be at least 3 characters", "create_recipe")
                is_valid = False

            if len(data["instructions"]) <3:
                flash("Instructions must be at least 3 characters", "create_recipe")
                is_valid = False

            if  not data["date_made"]:
                flash("Date made must not be blank", "create_recipe")
                is_valid = False

            if  "under_30" not in data:
                flash("under_30 must not be blank", "create_recipe")
                is_valid = False

            return is_valid