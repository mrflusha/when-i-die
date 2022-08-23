import pymysql.cursors,pymysql.err
import sys


db_table = 'post_text'

db_text = 'text'

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='mrf*',
                             database='VK',
                             cursorclass=pymysql.cursors.SSCursor)
def get_from_db():

	with connection.cursor() as cursor:
		connection.autocommit(True)
		result = list()
		sql = f'SELECT {db_text} FROM {db_table}'
		print(sql)
		cursor.execute(sql)
		for row in cursor:
			result.append(row)

		return result
	


def add_to_table(text):

	with connection.cursor() as cursor:
		sql = f"INSERT INTO {db_table} ({db_text}) VALUES (%s)"
		cursor.execute(sql, text)
	connection.commit()

		


#add_to_table("test 23567")
#posts = get_from_db()

#print(a)