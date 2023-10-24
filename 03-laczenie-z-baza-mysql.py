import mysql.connector

connection = mysql.connector.connect(
    user='', password='', host='127.0.0.1', database='python1', auth_plugin='mysql_native_password')

cursor = connection.cursor()


checkQuery = "SELECT * FROM users WHERE username = %(username)s AND city = %(city)s"
insertData = {
    'username': 'Janko',
    'city': 'Krakow'
}
cursor.execute(checkQuery, insertData)
existing_user = cursor.fetchone()

if existing_user is None:
    insertQuery = "INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)"
    cursor.execute(insertQuery, insertData)
    connection.commit()
    print("Użytkownik dodany pomyślnie.")
else:
    print("Podany użytkownik istnieje.")

query = 'SELECT id, username, city FROM users'
cursor.execute(query)

for (id, username, city) in cursor:
    print(f'{id} - {username} from {city}')

connection.close()
