from utils.constants import ALLOWED_EXTENSIONS


def allowed_file(filename):
    """
    Function that checks if the file is allowed
    """
    extension = filename.rsplit('.', 1)[1].lower()
    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False