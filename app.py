from flask import Flask, request, render_template, redirect, session
import mysql.connector
from sentiments import sentiments_bp
import os

app = Flask(__name__)

# Initialize user cookies
app.secret_key = os.urandom(24)

# Blueprint to call sentiments python file
app.register_blueprint(sentiments_bp)

# Establish database connection
try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="Enter you mysql password here", 
        database="user_db")
    cursor = conn.cursor()
except:
    print("An exception occurred")

# Call login template
@app.route('/')
def login():
    return render_template('login.html')

# Call register template
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')

# Route to verify user credentials
@app.route('/login_validation', methods=['POST'])
def login_validation():
    global conn
    email = request.form.get('email')
    password = request.form.get('password')

    cursor = conn.cursor()

    cursor.execute(
        """SELECT * 
        FROM 'users' 
        WHERE 'email' LIKE '{}' AND 'password' LIKE '{}'""".format(email, password))
    users = cursor.fetchall()

    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect('/home')
    else:
        return redirect('/login')
    
# Route to add new user to database
@app.route('/add_user', methods=['POST'])
def add_user():
    global conn

    name = request.form.get('uname')
    password = request.form.get('upassword')
    email = request.form.get('uemail')

    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO 'users' ('name', 'email', 'password')
        VALUES ('{}', '{}', '{}')""".format(name, email, password))
    conn.commit()
    cursor.execute(
        """SELECT *
        FROM 'users'
        WHERE 'email' LIKE '{}'""".format(email))
    myuser = cursor.fetchall()
    session['user_id'] = myuser[0][0]
    return redirect('/home')

# Route to logout and clear session
@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
    
