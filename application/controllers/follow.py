#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, redirect, url_for, request
from application.models.user_manager import *
from auth import is_login
from application.models.follow_manager import *


@app.route('/follow')
def follow():
    if not is_login():
        return redirect(url_for('login'))
    user = get_user(session['user_id'])
    return render_template('follow.html', user = user)


@app.route('/find_user', methods = ['POST'])
def find_user():
    users = find_user_by_keyword(request.form['keyword'])
    return render_template('user_list.html',users = users)



@app.route('/add_following', methods = ['POST'])
def add_following():
    followingId = request.form['following_id']

    return add_follow(session['user_id'],followingId)