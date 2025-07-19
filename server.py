from flask import Flask, render_template, send_from_directory, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou')
    else:
        return 'Something went wrong. Try again'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')
