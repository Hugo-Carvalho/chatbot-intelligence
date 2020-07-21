from flask import Flask
import os

app = Flask(__name__)

from main import main
app.register_blueprint(main)

if __name__ == '__main__':
    app.run('localhost',5000, use_reloader=True,use_debugger=True, use_evalex=True)
