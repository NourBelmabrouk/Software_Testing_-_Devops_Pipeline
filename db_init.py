import sqlite3


def create_db(database_filename):
    connection = sqlite3.connect(database_filename)
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute(
        "CREATE TABLE Users (ID INTEGER PRIMARY KEY, NAME TEXT NOT NULL,PHONE NUMERIC NOT NULL, EMAIL TEXT NOT NULL, JOB TEXT NOT NULL);")
    cur.execute("""
        INSERT INTO Users (NAME,PHONE,EMAIL,JOB) VALUES ('Lee',5068675309,'lee@aol.com','student'),
        ('Kory',2033892256,'kory@aol.com','UX Developer'),
        ('Laura',7480989947,'laura@aol.com','Project Manager')
        ;""")
    
    connection.commit()
    connection.close()
