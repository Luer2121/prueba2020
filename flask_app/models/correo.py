from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class Correo:

    db = "esquema_correo"
    def __init__(self,data):
        self.id = data['id']
        self.correo = data['correo']
        self.created_at = data['created_at']
        self.updatd_at = data['updated_at']

    db="esquema_correo"
    @classmethod
    def guardar(cls,data):
        query = "INSERT INTO correos (correo) VALUES (%(correo)s);"
        result = connectToMySQL('esquema_correo').query_db(query,data)
        return result   

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM correos;"
        results = connectToMySQL('esquema_correo').query_db(query)
        correos = []
        for u in results:
            correos.append( cls(u) )
        return correos

    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM correos WHERE id = %(id)s;"
        return connectToMySQL('esquema_correo').query_db(query,data)

    @staticmethod
    def is_valid(correo):
        is_valid = True
        query = "SELECT * FROM correos WHERE correo = %(correo)s;"
        results = connectToMySQL(Correo.db).query_db(query,correo)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(correo['correo']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid