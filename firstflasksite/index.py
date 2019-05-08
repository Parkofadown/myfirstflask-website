from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
# Basic Routing
@app.route('/')  # 127.0.0.1:5000
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


if __name__ == '__main__':
    app.run(debug=True)
