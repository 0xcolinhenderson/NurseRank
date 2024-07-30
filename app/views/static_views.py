from flask import render_template
from flask_login import login_required, current_user
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

def get_user_roles():
    if current_user.is_authenticated:
        user_roles = current_user.get_user_roles()
        return [role[0] for role in user_roles]
    return []

def index():
    roles = get_user_roles()
    return render_template("index.html", current_page='home', navbar_pages = navbar, user = current_user, roles=roles)

def register():
    roles = get_user_roles()
    return render_template("register.html",current_page='register', navbar_pages = navbar, user = current_user,roles=roles)

def login():
    roles = get_user_roles()
    return render_template("login.html",current_page='login', navbar_pages = navbar, user = current_user,roles=roles)

def about():
    roles = get_user_roles()
    return render_template("about.html",current_page='about', navbar_pages = navbar, user = current_user,roles=roles)

@login_required
def account():
    roles = get_user_roles()
    return render_template("account.html",current_page='account', navbar_pages = navbar, user = current_user,roles=roles)

@login_required
def edit_account():
    roles = get_user_roles()
    return render_template("edit_account.html",current_page='edit_account', navbar_pages = navbar, user = current_user,roles=roles)

@login_required
@roles_required(["admin"])
def admin():
    roles = get_user_roles()
    return render_template("admin.html",current_page='admin', navbar_pages = admin_navbar, user = current_user,roles=roles)

