from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

class Dojos:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas= []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        result = connectToMySQL( "dojos_and_ninjas_schema").query_db(query)

        all_dojos = []
        for row in result:
            all_dojos.append(cls(row))

        return all_dojos
    
    @classmethod
    def creat_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, now());"

        return connectToMySQL( "dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_dojos_with_ninjas(cls, dojo_id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        data = {
            "dojo_id": dojo_id
        }
        result = connectToMySQL( "dojos_and_ninjas_schema").query_db(query, data)
        dojo = cls(result[0])
        for row in result:
            ninja_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                'last_name' : row["last_name"],
                'age' : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row ["ninjas.updated_at"],
                "dojo_id": row ["dojo_id"]
            }
            dojo.ninjas.append(ninjas.Ninjas(ninja_data))
        print(dojo.ninjas[0].age)
        return dojo