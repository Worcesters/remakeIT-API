from utils.constants import ALLOWED_EXTENSIONS
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

def allowed_file(filename):
    """
    Function that checks if the file is allowed
    """
    extension = filename.rsplit('.', 1)[1].lower()
    if extension in ALLOWED_EXTENSIONS:
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