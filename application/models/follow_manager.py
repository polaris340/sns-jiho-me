#-*- coding:utf-8 -*-
from schema import Follow
from application import db


def add_follow(followerId, followingId):

    if Follow.query.filter(Follow.follower_id == followerId, Follow.following_id == followingId).count() != 0:
        return '1'

    follow = Follow(
        follower_id = followerId,
        following_id = followingId
    )

    db.session.add(follow)
    db.session.commit()

    return '0'