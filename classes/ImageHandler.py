import io
import numpy as np
from flask import make_response
from PIL import Image, ImageOps, ImageFilter

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
        if f == 'solarize':
            self.file = ImageOps.solarize(self.file)
        if f == '4bit':
            self.file = ImageOps.posterize(self.file, 4)
        if f == '8bit':
            self.file = ImageOps.posterize(self.file, 8)
        if f == 'mirror':
            self.file = ImageOps.mirror(self.file)
        if f == 'boxBlur':
            self.file = self.file.filter(ImageFilter.BoxBlur(3))
        if f == 'gaussianBlur':
            self.file = self.file.filter(ImageFilter.GaussianBlur(4))
        if f == 'unsharpMask':
            self.file = self.file.filter(ImageFilter.UnsharpMask(4, 4, 1))
        if f == 'sharpen':
            self.file = self.file.filter(ImageFilter.SHARPEN)
        if f == 'contour':
            self.file = self.file.filter(ImageFilter.CONTOUR)
        if f == 'detail':
            self.file = self.file.filter(ImageFilter.DETAIL)
        if f == 'edgeEnhance':
            self.file = self.file.filter(ImageFilter.EDGE_ENHANCE)
        if f == 'edgeEnhanceMore':
            self.file = self.file.filter(ImageFilter.EDGE_ENHANCE_MORE)
        if f == 'emboss':
            self.file = self.file.filter(ImageFilter.EMBOSS)
        if f == 'findEdges':
            self.file = self.file.filter(ImageFilter.FIND_EDGES)
        if f == 'smooth':
            self.file = self.file.filter(ImageFilter.SMOOTH)
        if f == 'smoothMore':
            self.file = self.file.filter(ImageFilter.SMOOTH_MORE)
        
            
        self.__save()

    def set_dimensions(self):
        pass

    def set_compression(self, percentage):
        pass
