# NurseRank
A website to help make my mom's life a little easier. 

Using: Python, JS, HTML + CSS, Flask, Supabase w/ Postgres

To run:
create .env folder w/ DB_URI set to your uri string
run "pip install -r require.txt"
run "python3 app.py"

Contents:

app.py - main executable python file

> app
    __init__.py - handle startup (db creation/handling, flask app, blueprints)
    database_manager.py - custom class for handling database creation, queries, sessions
    models.py - define database models (nurse, account, users, notes, files, etc)
    permissions.py - create decorator for functions that require specific permissions
    routes.py - creates blueprints + routing information

> app\views
    account.py - defines registration, login, logout, edit account functions
    error_views.py - defines views for 404 or 500 errors
    static_views.py - routing for main webpages

> app\utils
    cleaner.py - handling text sanitiztion functions
    error_utils.py - handle responses for error handling
    errors.py - definition of common errors w/ descriptions
    validators - handling of text validation for user inputs

> app\templates
    all html templates

> app\static\
    \css\styles.css - main css file
    \images\ - static image folder (stuff like the logo)
    \js\ - javascript folders for handling form input (registration, login, updating, getting profile)

> app\services
    account_management_services.py - main file for handing account creation / updating to database
