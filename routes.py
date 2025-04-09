from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group='Group 2')

@app.route('/about')
def about():
    message = 'Our names are Aiman, Sami, Serena, Jhaap, and Khrisha. Welcome to our flower shop'
    return render_template('about.html', title='About us', msg=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Example validation logic (you can replace this with your real authentication logic)
        if username == "admin" and password == "password":
            return redirect(url_for('home'))  # Redirect to home if credentials are correct
        else:
            return "Login failed. Please check your credentials."

    return render_template('login.html')  # Render the login form on GET request

