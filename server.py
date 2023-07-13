import csv

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        name = data.get('name')
        write_to_csv(data)
        return render_template('thankyou.html', section='contact', name=name)
    else:
        return 'something went wrong !! '

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

def write_to_file(data):
    with open('database.txt', mode='a') as databse:
        name = data['name']
        email = data['email']
        message = data['message']
        file = databse.write(f'\n{name },{email },{message }')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as databse2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(databse2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

@app.route('/works')
def works():
    return render_template("mywork.html")

# @app.route('/gallery')
# def gallery():
#     return "Here's the pictures of our association."
