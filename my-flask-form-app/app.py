from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    return render_template('submit.html', username=username, password=password, email=email)

if __name__ == '__main__':
    app.run()
