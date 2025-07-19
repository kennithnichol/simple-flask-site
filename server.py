from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def blog_index():
    return 'These are my blog entries'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')
