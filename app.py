from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('fitness.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            weight REAL,
            height REAL,
            bmi REAL,
            category TEXT,
            workout TEXT,
            duration INTEGER,
            calories REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    workout = request.form['workout']
    duration = int(request.form['duration'])

    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    calories = duration * 5

    conn = sqlite3.connect('fitness.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, weight, height, bmi, category, workout, duration, calories)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, weight, height, bmi, category, workout, duration, calories))
    conn.commit()
    conn.close()

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('fitness.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    names = [user[1] for user in users]
    bmis = [user[4] for user in users]
    calories = [user[8] for user in users]

    return render_template(
        'dashboard.html',
        users=users,
        names=names,
        bmis=bmis,
        calories=calories
    )

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('fitness.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/dashboard')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)