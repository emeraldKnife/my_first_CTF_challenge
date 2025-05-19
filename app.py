from flask import Flask, request, render_template_string, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite DB
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'flag{2401AI17}')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
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
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    try:
        result = c.execute(query).fetchone()
        if result:
            return "<h1>Welcome Admin! flag{2401AI17}" + "</h1>"
        else:
            return "<h1>Login Failed</h1>"
    except:
        return "<h1>Error</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)