from athena import flask_app as app
from athena import db, bcrypt
from flask import render_template, request, g, flash, redirect, url_for
from athena.forms import RegistrationForm, LoginForm, SearchForm

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/search")
def index():

    return render_template("search.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Hi {form.firstname.data}, your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@athena.com' and form.password.data == 'password123':
            flash(f'Welcome Back. Keep Writing!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check login email or password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/search_engine", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash(f'Submitted. You will receive a report in your email soon.', 'success')
        return redirect(url_for('home'))
    return render_template('search_engine.html', title='Search', form=form)