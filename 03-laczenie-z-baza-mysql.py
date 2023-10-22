import mysql.connector

connection = mysql.connector.connect(
    user='karol', password='!Sqlkarol', host='127.0.0.1', database='python', auth_plugin='mysql_native_password')

cursor = connection.cursor()


checkQuery = "SELECT * FROM users WHERE username = %(username)s AND city = %(city)s"
insertData = {
    'username': 'Karol',
    'city': 'Warszawa'
}
cursor.execute(checkQuery, insertData)
existing_user = cursor.fetchone()

if existing_user is None:
    insertQuery = "INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)"
    cursor.execute(insertQuery, insertData)
    connection.commit()
    print("Użytkownik dodany pomyślnie.")
else:
    print("Podany użytkownik już istnieje.")

query = 'SELECT id, username, city FROM users'
cursor.execute(query)

for (id, username, city) in cursor:
    print(f'{id} - {username} from {city}')

connection.close()
