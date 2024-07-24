import bcrypt
from app import db_manager as db
from ..models import User, Account
from ..utils import errors
from ..utils.validators import AccountValidator, EmailValidator

def get_user_profile_from_user_model(user_model):
    user_model_dict = user_model.__dict__

    allowlisted_keys = ["username", "email"]

    for key in list(user_model_dict.keys()):
        if key not in allowlisted_keys:
            user_model_dict.pop(key)

    return user_model_dict

def create_account(sanitized_firstname, sanitized_lastname, sanitized_email, unhashed_password):
    print(sanitized_firstname)
    print(sanitized_lastname)
    print(sanitized_email)
    print(unhashed_password)
    AccountValidator(
        firstname=sanitized_firstname,
        lastname=sanitized_lastname,
        email=sanitized_email,
        password=unhashed_password
    )
    print('a')
    if (
        db.session.query(User.email).filter_by(email=sanitized_email).first()
        is not None
    ):
        print('a2')
        raise errors.EmailAddressAlreadyExistsError()
    print('b')

    hash = bcrypt.hashpw(unhashed_password.encode(), bcrypt.gensalt())
    password_hash = hash.decode()
    print('c')

    account_model = Account()
    db.session.add(account_model)
    db.session.flush()
    print('d')

    user_model = User(
        firstname=sanitized_firstname,
        lastname=sanitized_lastname,
        password_hash=password_hash,
        email=sanitized_email,
        account_id=account_model.account_id,
    )
    print('e')


    print(f"user created @:{user_model.firstname} | ID #{user_model.account_id}")

    db.session.add(user_model)
    db.session.commit()
    print('e')

    return user_model


def verify_login(sanitized_email, password):
    EmailValidator(email=sanitized_email)

    user_model = db.session.query(User).filter_by(email=sanitized_email).first()

    if not user_model:
        raise errors.CouldNotVerifyLogin()

    if not bcrypt.checkpw(password.encode(), user_model.password_hash.encode()):
        raise errors.CouldNotVerifyLogin()

    return user_model