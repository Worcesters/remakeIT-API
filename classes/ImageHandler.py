import cv2
import numpy as np
from flask import make_response


class ImageHandler():

    def __init__(self, image):
        # Je transforme l'image en numpy array depuis le buffer de l'image, puis je la décode avec cv2
        self.file = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        self.target_extension = image.filename.rsplit('.', 1)[1].lower()
        # J'encode l'image en bytes dans le format souhaité (par defaut, base_extension)
        _, img_encoded = cv2.imencode(f'.{self.target_extension}', self.file)
        self.encoded = img_encoded.tobytes()
        
    def __encode_to_bytes(self, file):
        _, img_encoded = cv2.imencode(f'.{self.target_extension}', file)
        return img_encoded.tobytes()

    def set_ext(self, ext):
        self.target_extension = ext
        self.encoded = self.__encode_to_bytes(self.file)

    def set_filter(self, f):
        filters = {'grayScale': cv2.COLOR_BGR2GRAY, 'hsv': cv2.COLOR_BGR2HSV, 'rgb': cv2.COLOR_BGR2RGB}
        
        if f in filters:
            file = cv2.cvtColor(self.file, filters[f])
            self.encoded = self.__encode_to_bytes(file)
        elif f == 'anaglyph':
            pass

    def set_dimensions(self):
        pass

    def set_compression(self):
        pass
