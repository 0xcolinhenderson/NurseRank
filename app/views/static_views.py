from flask import render_template
from flask_login import login_required
from ..permissions import roles_required

navbar = {
    'Home' : '/',
    'About' : '/about',
}

admin_navbar = {
    'Home' : '/',
    'About' : '/about',
    'Manage' : '/admin'
}

def index():
    return render_template("index.html", current_page='home', navbar_pages = navbar)

def register():
    return render_template("register.html",current_page='register', navbar_pages = navbar)

def login():
    return render_template("login.html",current_page='login', navbar_pages = navbar)

def about():
    return render_template("about.html",current_page='about', navbar_pages = navbar)

@login_required
def account():
    return render_template("account.html",current_page='account', navbar_pages = navbar)

@login_required
@roles_required(["admin"])
def admin():
    return render_template("admin.html",current_page='admin', navbar_pages = admin_navbar)