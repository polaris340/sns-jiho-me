from application import app


app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///wtfdb?instance=affable-tribute-629:dbaffable-tribute-629',
    migration_directory = 'migrations',
    UPLOAD_FOLDER = '/gs/sns_storage',
    IMAGE_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif']),

))

