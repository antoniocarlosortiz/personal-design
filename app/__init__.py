from flask import Flask

# Create app
app = Flask(__name__, static_url_path='')

from app.frontend import frontend
app.register_blueprint(frontend, url_prefix='')