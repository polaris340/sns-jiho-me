#-*- coding:utf-8 -*-
from application import app
from flask import render_template, redirect, url_for, session, request
from application.models.post_manager import *
from application.models import comment_manager
from auth import is_login
from bs4 import BeautifulSoup as BS


@app.route('/read/<int:post_id>')
def read(post_id) :
    if not is_login():
        return redirect(url_for('login'))

    post = get_post(post_id)
    context = {
        'post':post,
        'is_author':post.user_id == session['user_id']
    }
    return render_template('read.html', context = context)


@app.route('/write')
def write():
    if not is_login():
        return redirect(url_for('login'))

    return render_template('write.html')

@app.route('/post_submit', methods = ['POST'])
def post_submit():
    if not is_login():
        return redirect(url_for('login'))
    
    postData = {
        'user_id' : session['user_id'],
        'wall_id' : session['wall_id'],
        'is_secret' : '1' if 'is_secret' in request.form else '0',
        'body' : request.form['body']
    }
    add_post(postData)


    return redirect(url_for('timeline',wall_id = session['wall_id']))

@app.route('/edit',methods=['POST'])
def edit():
    targetPost = get_post(request.form['post_id'])
    if targetPost.user_id != session['user_id']:
        return '1'

    edit_post(request.form)
    return '0'


@app.route('/delete/<int:post_id>')
def delete(post_id):
    targetPost = get_post(post_id)
    if targetPost.user_id != session['user_id']:
        return "error",403
    else:
        delete_post(post_id)
        return redirect(url_for('timeline'))

@app.route('/add_comment', methods = ['POST'])
def add_comment():
    data = {
        'user_id':session['user_id'],
        'post_id':request.form['post_id'],
        'body':request.form['body']

    }

    comment_manager.add_comment(data)

    return redirect(url_for('read',post_id=request.form['post_id']))
    
@app.route('/get_posts', methods=['POST'])
def get_posts():
    posts = get_wall_posts(session['wall_id'],request.form['start_id'])

    if posts.count() == 0:
        return ''

    context = {
        'posts':posts,
        'BS':BS
    }



    return render_template('post_list.html',context = context)





