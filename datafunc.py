import pymysql
import os
from dotenv import load_dotenv

username = os.getenv('MYSQL_USERNAME', None)
password = os.getenv('MYSQL_PASSWORD', None)


def get_students():
    connection = pymysql.connect(
        host='localhost', user=username, password=password, db='universityx'
    )

    students = []

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM student')
        students.append(cursor.fetchall())

    connection.close()

    return students


    