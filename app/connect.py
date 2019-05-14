#!/usr/bin/python
from psycopg2 import connect
import psycopg2.extras
from app import config

def db_connect(query, values, params):
    conn = None
    try:
        params = config.db_config(params)
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, values)
        conn.commit()
      
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
         if conn:
             conn.close()
 
#if __name__ == '__main__':
#    connect()
