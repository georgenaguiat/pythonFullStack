from mysqlconnection import connectToMySQL

class User:
    DB = 'users_cr'
    def __init__(self,  data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_user(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL(cls.DB).query_db(query)
        peoples = []
        for people in results:
            peoples.append(cls(people))
        return peoples
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM users WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = """UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)
        
    @classmethod
    def destroy(cls,data):
        query = """DELETE FROM users WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)