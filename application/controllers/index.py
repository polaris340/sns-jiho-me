#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, redirect, url_for
from application.models.post_manager import *
from application.models.user_manager import *
from auth import is_login
from bs4 import BeautifulSoup as BS

@app.route('/', defaults={'wall_id':0})
@app.route('/timeline/<int:wall_id>')
def timeline(wall_id) :
    if not is_login():
        return redirect(url_for('login'))
    if wall_id == 0:
        wall_id = session['user_id']

    session['wall_id'] = wall_id
    session['wall_username'] = get_user(wall_id).username

    context = {
        'posts':get_wall_posts(wall_id,0),
        'BS':BS
    }
    postList = render_template('post_list.html',context=context)
    context = {
        'post_list':postList
    }
    return render_template('timeline.html', context=context)

@app.route('/user_list')
def user_list():
    users = get_users()
    context = {'users':users}
    return render_template('all_user_list.html',context=context)