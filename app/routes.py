from flask import render_template, url_for

from . import app  # Assuming your Flask app instance is named 'app'

@app.route('/')
def index():
    return render_template('index.html')

# Define other routes as needed
