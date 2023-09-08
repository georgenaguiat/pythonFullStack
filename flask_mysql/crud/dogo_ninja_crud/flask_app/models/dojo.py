from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = """
                SELECT * 
                FROM dojos
                ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_dojos = []
        for all_dojo in results:
            all_dojos.append(cls(all_dojo))
        return all_dojos

    @classmethod
    def create(cls,data):
        query = """ INSERT 
                    INTO dojos (name, created_at, updated_at)
                    VALUES (%(name)s, NOW(), NOW())
                    ;"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def dojo_with_ninjas(cls, id):
        data = { 'id' : id }
        query = """
                SELECT * 
                FROM dojos 
                LEFT JOIN ninjas
                ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s
                ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo_list = []
        for dojo_row_db in results:
            ninja_data = cls(dojo_row_db)
            ninja_data = ninja.Ninja({
                'id' : dojo_row_db['ninjas.id'],
                'first_name' : dojo_row_db['first_name'],
                'last_name' : dojo_row_db['last_name'],
                'age' : dojo_row_db['age'],
                'created_at' : dojo_row_db['ninjas.created_at'],
                'updated_at' : dojo_row_db['ninjas.updated_at']
            })
            dojo_list.append(ninja_data)
        print(dojo_list)
        return dojo_list
    
    @classmethod
    def get_one_dojo(cls, id):
        data = { 'id' : id }
        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return cls(results[0])