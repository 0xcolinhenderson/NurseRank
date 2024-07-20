from functools import wraps
from flask_login import current_user
from .utils.error_utils import get_business_requirement_error_response
from .utils.errors import PermissionsDeniedError


def roles_required(roles):
    def decorated_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if set(roles).issubset({r.name for r in current_user.roles}):
                return f(*args, **kwargs)
            else:
                return get_business_requirement_error_response(
                    PermissionsDeniedError, 403
                )

        return wrapper

    return decorated_function