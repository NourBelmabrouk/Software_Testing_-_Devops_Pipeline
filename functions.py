from ntpath import join
import sqlite3
import os



def insert_data(name, phone, email, job):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    connection.execute(
    "INSERT INTO Users (NAME,PHONE,EMAIL,JOB) VALUES (?,?,?,?);",(name,phone,email,job,))
    connection.commit()

def modify_data(the_id, col_name, user_input):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    if col_name == 'name':
        connection.execute(
        "UPDATE Users SET NAME=? WHERE ID=?;", (user_input,the_id,))
    elif col_name == 'phone':
        connection.execute(
        "UPDATE Users SET PHONE=? WHERE ID=?;", (user_input,the_id,))
    elif col_name == 'email':
        connection.execute(
        "UPDATE Users SET EMAIL=? WHERE ID=?;", (user_input,the_id,))
    elif col_name == 'job':
        connection.execute(
        "UPDATE Users SET JOB=? WHERE ID=?;", (user_input,the_id,))
    
    
    connection.commit()


def delete_data(the_id):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    connection.execute(
        "DELETE FROM USERS WHERE ID=?;",(the_id,))
    connection.commit()


def get_all_rows_from_table():
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    users = cur.execute("SELECT * FROM USERS;").fetchall()
    connection.close()
    return users 
    