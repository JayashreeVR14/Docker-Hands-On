from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Step 1: connect to MySQL
        conn = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="mydb"
        )

        # Step 2: create cursor (to run SQL commands)
        cursor = conn.cursor()

        # Step 3: create table
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")

        # Step 4: insert data
        cursor.execute("INSERT INTO users (name) VALUES ('Jayashree')")

        # Step 5: fetch data
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        return str(data)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
