from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls):
        query = """
                SELECT * 
                FROM ninja
                ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_ninjas = []
        for all_ninja in results:
            all_ninjas.append(cls(all_ninja))
        return all_ninjas

    @classmethod
    def save_ninja(cls,data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW())
                ;"""
        return connectToMySQL(cls.DB).query_db(query,data)