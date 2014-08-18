from application.models.schema import User
from application import db
from file_manager import *
import os

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

def edit_user_data(id, data, profileImageFile):
    user = get_user(id)
    user.email = data['email']
    user.username = data['username']
    user.gender = data['gender']
    if data['password']:
        user.password = db.func.md5(data['password'])
    user.mobile = data['mobile']
    user.birthday = data['birthday']

    if profileImageFile and is_valid_image_file(profileImageFile.filename):
        filename = str(id)+'.'+get_extension(profileImageFile.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'profile',filename) 
        save_file(profileImageFile, filepath)

        user.profile_image = filename


    try:
        db.session.commit()
        return '0'
    except:
        return '1'
