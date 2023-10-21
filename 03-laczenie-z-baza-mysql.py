import mysql.connector

connection = mysql.connector.connect(
    user='', password='', host='', database='python', auth_plugin='mysql_native_password')

cursor = connection.cursor()

insertQuery = "INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)"
insertData = {
    'username': 'Marian',
    'city': ' Krakow'
}
cursor.execute(insertQuery, insertData)

connection.commit()

query = 'SELECT id, username, city FROM users'


cursor.execute(query)

for (id, username, city) in cursor:
    print(f'{id} - {username} from {city}')

connection.close()
