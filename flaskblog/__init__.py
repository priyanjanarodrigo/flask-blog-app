from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''
    # Generate a secret easily (IDLE can be used)
    import secrets
    secrets.token_hex(16) 
'''
app.config['SECRET_KEY'] = '30e8a8f03e6df34c9f76837290d89e1b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
