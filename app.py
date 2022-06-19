from lib2to3.pgen2 import token
from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e6798433ad54edea56a148c156ce5e9'

def token_required(func):
    @wraps(func)
    def decorated(*arg, kargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert': 'Token is missing!'})
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alert': 'Invalid token!'})
    return decorated

# Home
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Logged in currently!'

# Authenticated
@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard!'

# Login
@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] =True
        token = jwt.encode({
            'user': request.form['username'],
            'exp': str(datetime.utcnow() + timedelta(seconds=120))
        },
        app.config['SECRET_KEY'])
        return jsonify({'token': token})
    else:
        return make_response('Unable to verify', 403, {'Authentication Failed!'})

if __name__ == "__main__":
    app.run(debug=True)





