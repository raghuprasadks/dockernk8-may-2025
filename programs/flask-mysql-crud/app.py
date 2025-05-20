# filepath: d:\kaushalya\consultancy\nhce\2025\nhce\aiml\dockernkubernetes\sandbox\programs\flaskdemo\app.py
from flask import Flask, request, jsonify
import pymysql
import os
app = Flask(__name__)
"""
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='kaushalya@2017',
        db='dockerdb',
        cursorclass=pymysql.cursors.DictCursor
    )

"""
def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', '127.0.0.1'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        db=os.environ.get('DB_NAME', ''),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (data['name'], data['email'])
        )
        conn.commit()
    conn.close()
    return jsonify({'message': 'User added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)