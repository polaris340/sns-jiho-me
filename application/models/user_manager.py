from application.models.schema import User
from application import db


def get_user(id):
    return User.query.get(id)

def add_user(data):
    user = User(
        email = data['email'],
        username = data['username'],
        gender = data['gender'],
        password = db.func.md5(data['password']),
        mobile = data['mobile'],
        birthday = data['birthday']
    )

    db.session.add(user)
    db.session.commit()

    return user

def get_user(id):
    return User.query.get(id)

def login_check(email, password):
    return User.query.filter(User.email == email, User.password == db.func.md5(password))

def email_exists(email):
    return User.query.filter(User.email == email).count() != 0

def get_users():
    return User.query.all()


def delete_user(id):
    db.session.delete(get_user(id))
    db.session.commit()