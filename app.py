from flask import Flask, request, render_template_string
import webbrowser
import threading

app = Flask(__name__)

# SQL Injection Challenge
@app.route('/')
def home():
    return '''
    <h1>Admin Login</h1>
    <form action="/login" method="GET">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <button>Login</button>
    </form>
    '''

@app.route('/login')
def login():
    username = request.args.get('username', '')
    password = request.args.get('password', '')

    if username == "' OR 1=1 --" and password == "":
        return "<h1>Login Successful! Flag: flag{sqli_success_123}</h1>"
    else:
        return "<h1>Login Failed</h1>"

def open_browser():
    webbrowser.open_new('http://localhost:5000')

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()  # Auto-open browser
    app.run(host='0.0.0.0', port=5000)
