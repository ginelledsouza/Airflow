import github.includes.function as f
from psycopg2 import sql
import pandas as pd
import psycopg2


# Connect to an existing database
def establish_connection():
    connection = psycopg2.connect(user = f.user,
                                  password = f.password,
                                  host = f.host,
                                  port = f.port,
                                  database = f.database)

    return connection
 
def execute_query(conn, query):
    ret = 0 
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1

    if 'select' in query.lower():
        ret = cursor.fetchall()
    cursor.close()
    conn.close()
    return ret

def existing_table(conn):
    
    cursor = conn.cursor()

    cursor.execute("""SELECT relname FROM pg_class WHERE relkind='r'
                      AND relname !~ '^(pg_|sql_)';""")
    
    tables = [i[0] for i in cursor.fetchall()]
    
    conn.close()
    
    return tables

def postgresql_to_dataframe(conn, select_query, column_names):
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    tupples = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(tupples, columns=column_names)
    return df

def get_columns_names(conn,table):

    columns = []
    col_cursor = conn.cursor()
    col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
    col_names_str += "table_name = '{}';".format( table )
    try:
        sql_object = sql.SQL(
            col_names_str
        ).format(
            sql.Identifier( table )
        )

        col_cursor.execute( sql_object )
        col_names = ( col_cursor.fetchall() )
        for tup in col_names:
            columns += [ tup[0] ]
        col_cursor.close()

    except Exception as err:
        print ("get_columns_names ERROR:", err)
    return columns