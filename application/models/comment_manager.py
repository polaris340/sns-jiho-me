from schema import Comment
from application import db


def add_comment(data):
    comment = Comment(
        user_id = data['user_id'],
        post_id = data['post_id'],
        body = data['body']
    )

    db.session.add(comment)
    db.session.commit()

    return comment

def get_comment(id):
    return Comment.query.get(id)

def get_post_comments(post_id):
    return Comment.query.filter(Comment.post_id == post_id)


def delete_comment(id):
    db.session.delete(get_comment(id))
    db.session.commit()