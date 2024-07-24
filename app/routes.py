# routes.py

from flask import Blueprint
from app import db_manager
from app import login_manager
from .models import User
from .views import (
    static_views,
    account,
    error_views
)

bp = Blueprint('routes', __name__)

db = db_manager.session

@bp.before_app_request
def before_request():
    db()

@bp.teardown_app_request
def shutdown_session(response_or_exc):
    db.remove()

@login_manager.user_loader
def load_user(user_id):
    if user_id and user_id != "None":
        return User.query.filter_by(user_id=user_id).first()
    return None  # Ensure that the function always returns a value

# Error views
bp.register_error_handler(404, error_views.not_found_error)
bp.register_error_handler(500, error_views.internal_error)

# Public views
bp.add_url_rule("/", view_func=static_views.index)
bp.add_url_rule("/register", view_func=static_views.register)
bp.add_url_rule("/login", view_func=static_views.login)
bp.add_url_rule("/about", view_func=static_views.about)

# Login required views
bp.add_url_rule("/account", view_func=static_views.account)
bp.add_url_rule("/edit", view_func=static_views.edit_account)

# Public API
bp.add_url_rule("/api/login", view_func=account.login_account, methods=["POST"])
bp.add_url_rule("/logout", view_func=account.logout_account)
bp.add_url_rule("/api/register", view_func=account.register_account, methods=["POST"])

# Login Required API
bp.add_url_rule("/api/user", view_func=account.user)
bp.add_url_rule("/api/email", view_func=account.email, methods=["POST"])

# Admin required
bp.add_url_rule("/admin", view_func=static_views.admin)
