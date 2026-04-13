from flask import Flask, request, jsonify
import mysql.connector
import time

app = Flask(__name__)

# retry DB connection
while True:
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root123",
            database="userdb"
        )
        break
    except:
        print("Waiting for DB...")
        time.sleep(3)

cursor = db.cursor()

# create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
)
""")
db.commit()

@app.route('/')
def home():
    return "App Running"

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    return jsonify(cursor.fetchall())

@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (data['name'],))
    db.commit()
    return "User Added"

@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    cursor.execute("UPDATE users SET name=%s WHERE id=%s", (data['name'], id))
    db.commit()
    return "Updated"

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    return "Deleted"

app.run(host='0.0.0.0', port=5000)
