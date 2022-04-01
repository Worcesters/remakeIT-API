import io
from PIL import Image, ImageOps, ImageFilter

class ImageHandler():

    def __init__(self, image):
        self.file = Image.open(image.stream)
        self.file = self.file.convert('RGB')
        self.target_extension = self.__get_extension(image.filename.split('.')[-1])
        self.quality = 100
        self.__save()

    def __get_extension(self, ext):
        if ext == 'jpg':
            return 'jpeg'
        return ext

    def __save(self):
        self.bytes_array = io.BytesIO()
        self.file.save(self.bytes_array, format=self.target_extension, quality=self.quality)
        self.encoded = self.bytes_array.getvalue()

    def set_ext(self, ext):
        self.target_extension = self.__get_extension(ext)
        self.__save()

    def set_filter(self, f):        
        if f == 'grayScale':
            self.file = ImageOps.grayscale(self.file)            
        elif f == 'invert':
            self.file = ImageOps.invert(self.file)
        elif f == 'solarize':
            self.file = ImageOps.solarize(self.file)
        elif f == '4bit':
            self.file = ImageOps.posterize(self.file, 4)
        elif f == '8bit':
            self.file = ImageOps.posterize(self.file, 8)
        elif f == 'mirror':
            self.file = ImageOps.mirror(self.file)
        elif f == 'boxBlur':
            self.file = self.file.filter(ImageFilter.BoxBlur(30))
        elif f == 'gaussianBlur':
            self.file = self.file.filter(ImageFilter.GaussianBlur(30))
        elif f == 'unsharpMask':
            self.file = self.file.filter(ImageFilter.UnsharpMask(4, 4, 1))
        elif f == 'sharpen':
            self.file = self.file.filter(ImageFilter.SHARPEN)
        elif f == 'contour':
            self.file = self.file.filter(ImageFilter.CONTOUR)
        elif f == 'detail':
            self.file = self.file.filter(ImageFilter.DETAIL)
        elif f == 'edgeEnhance':
            self.file = self.file.filter(ImageFilter.EDGE_ENHANCE)
        elif f == 'edgeEnhanceMore':
            self.file = self.file.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif f == 'emboss':
            self.file = self.file.filter(ImageFilter.EMBOSS)
        elif f == 'findEdges':
            self.file = self.file.filter(ImageFilter.FIND_EDGES)
        elif f == 'smooth':
            self.file = self.file.filter(ImageFilter.SMOOTH)
        elif f == 'smoothMore':
            self.file = self.file.filter(ImageFilter.SMOOTH_MORE)
        elif f == 'sepia':
            new_img = self.file
            width, height = new_img.size
            img_map = new_img.load()
            print(img_map[4,4])
            # work on pixels
            for py in range(height):
                for px in range(width):
                    # 1) get rgb values
                    r, g, b = img_map[px, py]
                    # 2) transform to grayscale
                    gray = int(r * 0.298912 + g * 0.586611 + b * 0.114478)
                    # 3) change to sepia
                    sr = int(gray * 0.8 + 2)
                    sg = int(gray * 0.6 + 2)
                    sb = int(gray * 0.4 + 2)
                    # 4) set new value to picture
                    img_map[px, py] = sr, sg, sb
            # 5) save sepia filter
            self.file = new_img

        self.__save()

    def set_dimensions_and_compression(self, h, w, c):
        h = h if h else self.file.height
        w = w if w else self.file.width
        c = c if c else 100
        self.quality = c
        self.file = self.file.resize((w, h), Image.ANTIALIAS)
        self.bytes_array = io.BytesIO()
        self.file.save(self.bytes_array, format='jpeg', quality=c)
        self.encoded = self.bytes_array.getvalue()
