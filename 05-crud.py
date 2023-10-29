import mysql.connector
from flask import Flask, jsonify, request, Response
import jsonpickle
from config import DATABASE_CONFIG


def get_connection_to_database():
    try:
        connection = mysql.connector.connect(**DATABASE_CONFIG)
        return connection
    except mysql.connector.Error as err:
        return jsonify(details="Error connecting to the database: " + str(err)), 500


class User:
    def __init__(self, user_id, username, city):
        self.user_id = user_id
        self.username = username
        self.city = city


app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    users = []
    with get_connection_to_database() as connection:
        with connection.cursor(dictionary=True) as cursor:
            query = 'SELECT id, username, city FROM users'
            cursor.execute(query)
            for row in cursor:
                users.append(User(row['id'], row['username'], row['city']))
    response = Response(jsonpickle.encode(
        users, unpicklable=False), mimetype='application/json')
    response.headers['Title'] = 'CRUD_app'
    return response


@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    try:
        connection = get_connection_to_database()
        cursor = connection.cursor()
        query = 'INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()
    return jsonify(request_data), 201


@app.route('/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    request_data = request.get_json()
    request_data['user_id'] = user_id
    try:
        connection = get_connection_to_database()
        cursor = connection.cursor()
        query = 'UPDATE users SET username=%(username)s, city=%(city)s WHERE id=%(user_id)s'
        cursor.execute(query, request_data)
        if cursor.rowcount == 0:
            return jsonify(details="User with the provided ID not found."), 404

        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()
    return jsonify(request_data)


@app.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    request_data = {}
    request_data['user_id'] = user_id
    try:
        connection = get_connection_to_database()
        cursor = connection.cursor()
        query = 'DELETE from users WHERE id=%(user_id)s'
        cursor.execute(query, request_data)

        if cursor.rowcount == 0:
            return jsonify(message="User not found"), 404

        connection.commit()
        return jsonify(message="User deleted")
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()


if __name__ == '__main__':
    app.run()
