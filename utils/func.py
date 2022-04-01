from utils.constants import ALLOWED_EXTENSIONS, ALLOWED_FILTERS
from PIL import Image, ImageOps, ImageFilter, ImageEnhance


def allowed_extension(extension):
    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


def allowed_file(filename):
    """
    Function that checks if the file is allowed
    """
    extension = filename.rsplit('.', 1)[1].lower()
    return allowed_extension(extension)


def allowed_filter(filter):
    if filter in ALLOWED_FILTERS:
        return True
    else:
        return False


def c_is_valid(c):
    if c > 0 and c <= 100:
        return True
    else:
        return False


def make_anaglyph(img):
    assert isinstance(img, Image.Image)
    MIN_SIZE = min(img.size)

    img_copy = img.copy()
    R_resized, L_resized = img_copy.resize((MIN_SIZE, MIN_SIZE))

    print(R_resized.size, L_resized.size)

    return R_resized, L_resized
