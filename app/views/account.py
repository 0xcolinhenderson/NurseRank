from flask import request, redirect, url_for
from flask_login import login_user, logout_user, login_required,  current_user
from pydantic import ValidationError
from  ..utils import cleaner, errors
from ..services import account_management_services
from ..utils.error_utils import (
    get_business_requirement_error_response,
    get_validation_error_response,
    get_db_error_response,
)

def register_account():
    firstname = request.json.get('firstname')
    lastname = request.json.get('lastname')
    email = request.json.get('email')
    password = request.json.get('password')
    password2 = request.json.get('password2')
    rn_status = request.json.get('rn_status')

    cleaned_firstname = cleaner.clean_text(firstname)
    cleaned_lastname = cleaner.clean_text(lastname)
    cleaned_email  = cleaner.clean_text(email)

    try:
        user_model = account_management_services.create_account(
            cleaned_firstname, cleaned_lastname, cleaned_email, password
        )
    except ValidationError as e:
        return get_validation_error_response(validation_error=e, http_status_code=422)
    except errors.EmailAddressAlreadyExistsError as e:
        return get_business_requirement_error_response(
            business_logic_error=e, http_status_code=409
        )
    except errors.InternalDbError as e:
        return get_db_error_response(db_error=e, http_status_code=500)

    login_user(user_model, remember=True)

    return {"message": "success"}, 201

def login_account():
    unsafe_email = request.json.get("email")
    password = request.json.get("password")

    sanitized_email = cleaner.clean_text(unsafe_email)

    try:
        user_model = account_management_services.verify_login(sanitized_email, password)
    except ValidationError as e:
        return get_validation_error_response(validation_error=e, http_status_code=422)
    except errors.CouldNotVerifyLogin as e:
        return get_business_requirement_error_response(
            business_logic_error=e, http_status_code=401
        )

    login_user(user_model, remember=True)

    return {"message": "success"}


def logout_account():
    logout_user()
    return redirect(url_for("index"))


@login_required
def user():
    user_profile_dict = account_management_services.get_user_profile_from_user_model(
        current_user
    )
    return {"data": user_profile_dict}


@login_required
def email():
    unsafe_email = request.json.get("email")

    sanitized_email = cleaner.clean_text(unsafe_email)

    try:
        account_management_services.update_email(current_user, sanitized_email)
    except ValidationError as e:
        return get_validation_error_response(validation_error=e, http_status_code=422)
    except errors.EmailAddressAlreadyExistsError as e:
        return get_business_requirement_error_response(
            business_logic_error=e, http_status_code=409
        )
    except errors.InternalDbError as e:
        return get_db_error_response(db_error=e, http_status_code=500)

    return {"message": "success"}, 201