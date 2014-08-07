#-*- coding:utf-8 -*-
from schema import Post
from application import db


def add_post(data):
    post = Post(
        wall_id = data['wall_id'],
        user_id = data['user_id'],
        body = data['body'],
        is_secret = data['is_secret']
    )

    db.session.add(post)
    db.session.commit()

    return post

def get_post(id):
    return Post.query.get(id)

def get_all_posts():
    return Post.query.all().order_by(desc(Post.edited_time))


def get_wall_posts(wall_id,start_id = 0, 
    post_count = 5):
    start_id = int(start_id)

    if start_id == 0:
        return Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).limit(post_count)
    else:
        return Post.query.filter(Post.wall_id == wall_id, Post.id < start_id).order_by(db.desc(Post.edited_time)).limit(post_count)


def delete_post(id):
    db.session.delete(get_post(id))
    db.session.commit()

def edit_post(data):
    targetPost = get_post(data['post_id'])
    targetPost.body = data['body']

    db.session.commit()
