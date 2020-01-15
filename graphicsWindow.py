from PIL import Image

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def drawPixel(self,pixel,color):
        self.__image[pixel[0],pixel[1]] = color

    def saveImage(self,fileName):
        self.__canvas.save(fileName)