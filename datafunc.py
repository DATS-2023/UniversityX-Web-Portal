import pymysql
import os
from dotenv import load_dotenv

username = os.getenv('MYSQL_USERNAME', None)
password = os.getenv('MYSQL_PASSWORD', None)


def get_table(table):
    connection = pymysql.connect(
        host='localhost', user=username, password=password, db='universityx'
    )

    table_results = None
    print('SELECT * FROM %s', table)

    with connection.cursor() as cursor:

        cursor.execute(f'SELECT * FROM {table}')
        table_results = cursor.fetchall()

    connection.close()

    return table_results
    
def add_table(table, columns, data):
    connection = pymysql.connect(
        host='localhost', user=username, password=password, db='universityx'
    )

    print(f'INSERT INTO {table} ({columns}) VALUES ({data})')

    with connection.cursor() as cursor:
        cursor.execute(f'INSERT INTO {table} ({columns}) VALUES (%s)', (data,)) 
        # future improvment, use %s to counteract sql injection
        connection.commit()
        
    connection.close()
