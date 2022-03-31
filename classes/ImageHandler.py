import io
import numpy as np
from flask import make_response
from PIL import Image, ImageOps

class ImageHandler():
    def __get_extension(self, ext):
        if ext == 'jpg':
            return 'jpeg'
        return ext
       
    def __init__(self, image):
        self.file = Image.open(image.stream)
        
        if self.file.mode != 'RGB':
            self.file = self.file.convert('RGB')
            
        self.target_extension = self.__get_extension(image.filename.split('.')[-1])
        self.bytes_array = io.BytesIO()
        self.file.save(self.bytes_array, format=self.target_extension)
        self.encoded = self.bytes_array.getvalue()
        
    def __save(self):
        self.bytes_array = io.BytesIO()
        self.file.save(self.bytes_array, format=self.target_extension)
        self.encoded = self.bytes_array.getvalue()

    def set_ext(self, ext):
        self.target_extension = self.__get_extension(ext)
        self.__save()

    def set_filter(self, f):        
        if f == 'grayScale':
            self.file = ImageOps.grayscale(self.file)
        if f == 'invert':
            self.file = ImageOps.invert(self.file)
            
        self.__save()

    def set_dimensions(self):
        pass

    def set_compression(self, percentage):
        pass
