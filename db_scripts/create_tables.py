import psycopg2
from db_config import host, user, password, db_name


try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )
    connection.autocommit = True
    
    # the cursor for perfoming database operations
        
    # create a new tables
    #
    # Users
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY, 
                name VARCHAR(128) NOT NULL,
                login VARCHAR(128) UNIQUE NOT NULL,
                email VARCHAR(128),
                password VARCHAR(255) NOT NULL
                );"""
            )

        print("[INFO] Table Users created successfully")
    

    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")