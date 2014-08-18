from application import app
from google.appengine.api import files


def is_valid_image_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1] in app.config['IMAGE_EXTENSIONS']

def get_extension(filename):
    return filename.split('.')[-1]

def save_file(file, filename):
    writableFileName = files.gs.create(filename, mime_type = file.content_type, acl = 'public-read')
    with files.open(writableFileName,'ab') as f:
        f.write(file.read())
    files.finalize(writableFileName)

def read_file(filename):
    with files.open(filename, 'r') as f:
        return f.read()