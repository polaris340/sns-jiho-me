#-*- coding:utf-8 -*-
from application import app, db
from flask import session, request, render_template, redirect, url_for
from application.models.user_manager import *
import os
from application.controllers.auth import *


@app.route('/profile')
def profile():
    if not is_login():
        return redirect(url_for('login'))

    userData = get_user(session['user_id'])
    return render_template('profile.html',userData = userData)

@app.route('/edit_profile', methods = ['POST'])
def edit_profile():
    
    profileImageFile = request.files['input-profile-image']

    edit_user_data(session['user_id'], request.form, profileImageFile)
    return redirect(url_for('profile'))

@app.route('/image/profile/<filename>')
def profile_image(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],'profile',filename)
    return read_file(filepath)