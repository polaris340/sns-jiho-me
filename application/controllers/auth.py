#-*- coding:utf-8 -*-
from application import app, db
from flask import session, request, render_template, redirect, url_for
from application.models.user_manager import *
import re



@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/login')
def login():
    if is_login():
        return redirect(url_for('timeline'))
    else:
        return render_template('login.html')

@app.route('/login_submit', methods = ['POST'])
def login_submit():
    email = request.form['email']
    password = request.form['password']

    user = login_check(email, password)
    if user.count() == 1:
        # login success
        user = user.one()
        session['username'] = user.username
        session['user_id'] = user.id
        return '0'
    else:
        return '1'


@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('user_id')
    session.pop('wall_id')
    session.pop('wall_username')
    return redirect(url_for('login'))

@app.route('/join_submit', methods = ['POST'])
def join_submit():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username'].encode('utf8')
    mobile = request.form['mobile']


    # form validation
    if email_exists(email):
        return '1'

    emailPattern = re.compile('^[\w\d_.]+@[\w\d_.]+\.(\w+|\w+\.\w+)$')
    if not emailPattern.search(email):
        return '2'

    if not 6 <= len(password) <= 20 or (not re.search('\d+',password) or not re.search('[a-zA-Z]+',password)):
        return '3'

    if password != request.form['password-confirm']:
        return '3'

    if len(username) == 0 or not(re.search('^[a-zA-Z가-힣0-9_.]{1,10}$',username)):
        return '4'

    if not re.search('^\+?[0-9-]{10,14}$',mobile):
        return '5'

    


    add_user(request.form);
    return '0'

@app.route('/email_duplicate_check', methods = ['POST'])
def email_duplicate_check():
    if email_exists(request.form['email']):
        return '1'
    else:
        return '0'

def is_login():
    return 'username' in session and 'user_id' in session



