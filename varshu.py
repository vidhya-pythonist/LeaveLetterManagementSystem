
import sqlite3
from flask import Flask, render_template, request,jsonify
app = Flask(__name__)

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT,
              email TEXT,
              password TEXT)''')
conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
#function definition 
def register():
    if request.method == 'POST':
        # Retrieve the user input from the registration form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Store the user registration information in the database
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        
        # Return a success message to the user
        return 'Registration successful!'
    elif request.method== "GET":
    # Render the registration page template for GET requests
    
        return render_template('user.html')

    return render_template('user.html')


@app.route('/users', methods=['GET'])
def get_users():
    # Retrieve all user information from the database
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")    
    rows = c.fetchall()
    conn.close()

    # convert the user information into a JSON file 
    users = []
    for row in rows:
        user = {'id': row[0], 'username': row[1], 'email': row[2], 'password': row[3]}
        users.append(user)
    return jsonify(users)

# Create the users table if it doesn't exist
conn = sqlite3.connect('temp_table.db')
c = conn.cursor()
# Create a temporary table
c.execute('''CREATE TABLE IF NOT EXISTS temp_table
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL)''')
conn.commit()
conn.close()

@app.route('/store_name', methods=['GET', 'POST'])
def name_create():
    if request.method == 'POST':
        # Retrieve the user input from the form
        username = request.form['Enter your name']

        # Store the user's name in the database
        conn = sqlite3.connect('temp.db')
        c = conn.cursor()
        c.execute("INSERT INTO temp_table (name) VALUES (?)", (username,))

        conn.commit()
        conn.close()
        
        # Return a success message to the user
        return "Name  has been added to the database!"
    
    # Render the form for GET requests
    return render_template('name.html')

@app.route('/get_names', methods=['GET'])
def get_names():
    # Retrieve all names from the database
    conn = sqlite3.connect('temp.db')
    c = conn.cursor()
    c.execute("SELECT name FROM temp_table")

    rows = c.fetchall()
    conn.close()
    
    # Convert the name information into a JSON response
    names = []
    for row in rows:
        names.append(row[0])
    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True)
