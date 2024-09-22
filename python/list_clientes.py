import pymysql
import dotenv
import os
import json
import datetime 
import pymysql.cursors
dotenv.load_dotenv()

## Connection pymysql
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Define a custom function to serialize datetime objects 
def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    # raise TypeError("Type not serializable") 


TABLE_NAME = 'users'
id = 101
with connection:
    with connection.cursor() as cursor:
        querySql = (
            f'SELECT * FROM {TABLE_NAME} LIMIT 10'
        )
        cursor.execute(
            querySql
        )

        for user in cursor.fetchall():
            print(json.dumps(user, default=serialize_datetime))
