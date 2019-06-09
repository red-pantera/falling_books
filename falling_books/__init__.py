from flask import Flask
from falling_books.main.controllers import main
from falling_books.admin.controllers import admin
from falling_books.data.models import db

app = Flask(__name__)
app.config['TESTING']

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

db.init_app(app) 
