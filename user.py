import sqlite3
from flask_restful import Resource
from flask import request

class User:
    def __init__(self,id,username,password): # HERE I HAVE CREATED THERE VARIABLE
                                             # THESE ARE USERNAME,PASSWORD AND UNIQUE ID FOR EACH PERSON
        self.id = id
        self.username = username
        self.password = password
    @classmethod
    def find_by_username(clss,username):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        q1 = "SELECT * FROM user WHERE username=?"
        result = cursor.execute(q1,(username,))
        row = result.fetchone()
        if row:
            user = clss(*row)
        else:
            user = None
        return user
    @classmethod
    def find_by_id(clss,id):
        conn = sqlite3.connect('data.db') #we are connecting the database to connect to the server
        cursor = conn.cursor() #conn the server to the cursor

        q1 = "SELECT * FROM user WHERE id=?" #select the row from the table
        result = cursor.execute(q1,(id,)) #on the basis of id we are fetching the data that id not present then we insert the data in the database
        row = result.fetchone() #Here we fetch the one result
        if row:
            user = clss(*row) #does there is any row present inside it or not
        else:
            user = None
        return user



class SignUp(Resource): #Here we create one signup method that post the username password to the web server
    def post(self):
        data = request.get_json() #We request for the data to get jsonified object

        conn = sqlite3.connect('data.db')  # connection establishment to sqlite3 database
        cursor = conn.cursor() # cursor object is created

        q1 = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,username TEXT,password TEXT)" # we are creating table if not present 
        cursor.execute(q1) #executing the cursor object
        q2 = "INSERT INTO user VALUES(NULL,?,?)" # inserting value in database
        cursor.execute(q2,(data['username'],data['password'])) #executing q2 in the database

        conn.commit() # connection is commited to get the result
        conn.close() # we close the connection
        return {"message":"user created"}
