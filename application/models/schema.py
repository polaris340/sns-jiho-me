from application import db



class User(db.Model):
    id          = db.Column(db.Integer, primary_key = True) # When creating tables, SQLAlchemy will automatically set AUTO_INCREMENT on the first Integer primary key column which is not marked as a foreign key
    email       = db.Column(db.String(60))
    username    = db.Column(db.String(45))
    gender      = db.Column(db.Enum('F','M'))
    password    = db.Column(db.String(100))
    mobile      = db.Column(db.String(15))
    birthday    = db.Column(db.Date)


class Post(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    user        = db.relationship('User',foreign_keys = [user_id]
       #,backref  = db.backref('posts', cascade = 'all, delete-orphan', lazy = 'dynamic')
       )
    wall_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    wall        = db.relationship('User',foreign_keys = [wall_id],
        backref = db.backref('wall_posts', cascade = 'all, delete-orphan', lazy = 'dynamic'))
    body        = db.Column(db.Text())
    edited_time = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())
    created_time = db.Column(db.DateTime, default = db.func.now())
    is_edited   = db.Column(db.Boolean, default = '0')
    is_secret   = db.Column(db.Boolean, default = '0')


class Comment(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    post_id     = db.Column(db.Integer, db.ForeignKey('post.id'))
    post        = db.relationship('Post'
        ,backref = db.backref('comments', cascade = 'all, delete-orphan', lazy = 'dynamic')
        )
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User'
    #    ,backref = db.backref('comments', cascade = 'all, delete-orphan', lazy = 'dynamic')
    )
    body        = db.Column(db.Text())
    created_time = db.Column(db.DateTime, default = db.func.now())


