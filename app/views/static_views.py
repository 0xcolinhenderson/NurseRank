from flask import render_template
from flask_login import login_required
from ..permissions import roles_required

index_navbar = {
    'Home' : '/',
    'Log In' : '/login',
    'Register' : 'register',
    'About' : '/about',
}

def index():
    return render_template("index.html", current_page='home', navbar_pages = index_navbar)

register_navbar = {
    'Home' : '/',
    'About' : '/about',
}

def register():
    return render_template("register.html",current_page='register', navbar_pages = register_navbar)

login_navbar = {
    'Home' : '/',
    'About' : '/about',
}

def login():
    return render_template("login.html",current_page='login')

about_navbar = {
    'Home' : '/',
    'Log In' : '/login',
    'Register' : 'register',
    'About' : '/about',
}

def about():
    return render_template("about.html",current_page='about')



@login_required
def account():
    return render_template("account.html",current_page='account')


@login_required
@roles_required(["admin"])
def admin():
    return render_template("admin.html",current_page='admin')