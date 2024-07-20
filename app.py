from flask import Flask, render_template, jsonify

app = Flask(__name__)

PEOPLE = [{
    'id': 1,
    'firstname': 'Jack',
    'lastname': 'Name',
    'duedate': '2020-01-01',
    'department': 'Nursing',
    'rank': '4',
}, {
    'id': 2,
    'firstname': 'Jane',
    'lastname': 'Frame',
    'duedate': '2023-01-05',
    'department': 'Dermatology',
    'rank': '1',
}, {
    'id': 3,
    'firstname': 'John',
    'lastname': 'Lame',
    'duedate': '2022-11-12',
    'department': 'PRE-OP',
    'rank': '3',
}, {
    'id': 4,
    'firstname': 'Jen',
    'lastname': 'Blame',
    'duedate': '2021-02-10',
    'department': 'Nursing',
    'rank': '2',
}]


@app.route('/')
def home():
    return render_template('base.html', allow=True)


@app.route('/sign-up')
def sign_up():
    return "signup"


@app.route('/login')
def login():
    return "login"


@app.route('/logout')
def logout():
    return "logout"


@app.route('/admin-view')
def admin_view():
    return "admin"


@app.route('/profile')
def profile():
    return "profile"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
