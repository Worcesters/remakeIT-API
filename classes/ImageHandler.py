import cv2
import numpy as np
from flask import make_response

class ImageHandler():

    def __init__(self, img):
        self.img = img
        self.ext = img.filename.rsplit('.', 1)[1].lower()

    def set_ext(self, ext):

        image = cv2.imdecode(np.frombuffer(self.img.read(), np.uint8), cv2.IMREAD_COLOR)
        _, img_encoded = cv2.imencode(f'.{ext}', image)
        response = make_response(img_encoded.tobytes())
        response.headers['Content-Type'] = f'image/{ext}'
        return response

    def set_filter(self, filter):
        pass

    def set_dimensions(self):
        pass

    def set_compression(self):
        pass

