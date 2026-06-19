from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = "journal_app"

mysql = MySQL(app)

@app.route("/entries", methods=["GET"])
def get_entries():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM entries")
    rows = cursor.fetchall()
    cursor.close()

    entries = []
    for row in rows:
        entries.append({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "date": row[3]
        })
    return jsonify(entries)

@app.route("/entries", methods=["POST"])
def add_entry():
    data = request.get_json()
    title = data["title"]
    content = data["content"]
    date = data["date"]

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO entries (title, content, date) VALUES (%s, %s, %s)", (title, content, date))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Entry added"}), 201

@app.route("/entries/<int:id>", methods=["DELETE"])
def delete_entry(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM entries WHERE id=%s", (id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)