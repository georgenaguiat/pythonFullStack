from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
import re
from flask import flash, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    DB = 'login_registrations'
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, user_data):
        if not User.validation_user(user_data):
            return False
        user_data = user_data.copy()
        user_data['password'] = bcrypt.generate_password_hash(user_data['password'])
        query = """
                INSERT
                INTO users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
                ;"""
        user_id = connectToMySQL(cls.DB).query_db(query, user_data) 
        session['user_id'] = user_id
        session['user_name'] = f"{user_data['first_name']} {user_data['last_name']}"
        return user_id
            
    @classmethod
    def get_all_users(cls):
        query = """
                SELECT *
                FROM users
                ;"""  
        results = connectToMySQL(cls.DB).query_db(query)
        peoples = []
        for people in results:
            peoples.append(cls(people))
        return peoples
    
    @classmethod
    def get_one_user(cls, user_id):
        query = """
                SELECT *
                FROM users
                WHERE id = %(id)s
                ;"""
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls, email):
        data = {
            'email': email
        }
        query = """
                SELECT *
                FROM users
                WHERE email = %(email)s
                ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            this_user = cls(results[0])
            return this_user
        return False
    
    @classmethod
    def user_login(cls, user_data):
        this_user = cls.get_by_email(user_data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, user_data['password']):
                session['user_id'] = this_user.id
                session['user_name'] = f"{this_user.first_name} {this_user.last_name}"
                return True
        flash('Invalid Email/Password', 'login_error')
        return False

    @staticmethod
    def validation_user(user_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if not user_data['first_name']:
            flash('First Name is required', 'registration_error')
        elif len(user_data['first_name']) < 2:
            flash('First Name must be at least 2 characters', 'registration_error')
            is_valid = False
        if not user_data['last_name']:
            flash('Last Name is required', 'registration_error')
        elif len(user_data['last_name']) <2:
            is_valid = False
            flash('Last Name must be at least 2 characters.', 'registration_error')
        if not user_data['email']:
            flash('Email is required', 'registration_error')
        elif User.get_by_email(user_data['email']):
            flash('Email has already been taken, please try again.', 'registration_error')
            is_valid = False
        if not EMAIL_REGEX.match(user_data['email']):
            flash('Invalid email address')
            is_valid = False
        if not user_data['password']:
            flash('Password is required', 'registration_error')
        elif len(user_data['password']) < 8:
            flash('Password must be at least 8 characters.', 'registration_error')
            is_valid = False
        elif not any(char.isdigit() for char in user_data['password']):
            flash('Password must contain at least one digit.', 'registration_error')
            is_valid = False
        elif not any(char.isupper() for char in user_data['password']):
            flash('Password must contain at least one uppercase letter.', 'registration_error')
            is_valid = False
        if not user_data['confirm_password']:
            flash('Confirm Password is required', 'registration_error')
            is_valid = False
        if user_data['password'] != user_data['confirm_password']:
            flash('Password need to match.', 'registration_error')
            is_valid = False
        return is_valid