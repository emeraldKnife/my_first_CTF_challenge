from flask import Flask, request, render_template_string, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


CORRECT_PASSWORD = "299792458"


def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'flag{2401AI17}')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return '''
    <h1>Restricted Portal</h1>
    <p>33355588 -> ilu</p>
    <form action="/check_password" method="POST">
        <input type="password" name="password" placeholder="Password">
        <button>Submit</button>
    </form>
    '''

@app.route('/check_password', methods=['POST'])
def check_password():
    user_password = request.form.get('password', '')
    if user_password == CORRECT_PASSWORD:
        session['authenticated'] = True
        return redirect('/portal')
    else:
        return "<h1>Wrong password!</h1>"

@app.route('/portal')
def portal():
    if not session.get('authenticated'):
        return redirect('/')
    return '''
    <h1>Secure Admin Portal</h1>
    <form action="/login" method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <button>Login</button>
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    if not session.get('authenticated'):
        return redirect('/')
    
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    try:
        result = c.execute(query).fetchone()
        if result:
            return "<h1>Welcome Admin! flag{2401AI17}</h1>"
        else:
            return "<h1>Login Failed</h1>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
