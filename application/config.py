from application import app


app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///snsdb?instance=jiho-me-blog:jiho-me-blog-db',
    migration_directory = 'migrations'
))

