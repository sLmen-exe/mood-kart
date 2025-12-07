from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mooddb"
)
cursor = db.cursor(dictionary=True)

@app.route("/")
def index():
    cursor.execute("SELECT * FROM moods ORDER BY created DESC")
    logs = cursor.fetchall()
    return render_template("index.html", logs=logs)

@app.route("/add", methods=["POST"])
def add():
    mood = request.form["mood"]
    note = request.form["note"]
    cursor.execute("INSERT INTO moods (mood, note) VALUES (%s, %s)", (mood, note))
    db.commit()
    return redirect("/")

app.run(host="0.0.0.0", port=5000)
