import logging
import math
import random

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
    
    def drawLine(self,p1,p2,color):
        sign = lambda x: x and (1, -1)[x<0]
        
        x1, y1, x2, y2 = *p1, *p2
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        sX, sY = sign(x2 - x1), sign(y2 - y1)

        if dx >= dy:
            x, xi, y, yi, d1, d2 = x1, sX, y1, sY, dy, dx
            plot = lambda x, y, c=color: self.drawPixel((x, y), c)
        elif dy > dx:
            x, xi, y, yi, d1, d2 = y1, sY, x1, sX, dx, dy
            plot = lambda x, y, c=color: self.drawPixel((y, x), c)
        else:
            raise Exception(f"{p1} to {p2} is not drawn")
        
        plot(x, y)
        pi = 2 * d1 - d2
        for i in range(d2):
            if pi < 0:
                pi = pi + 2 * d1
            else:
                pi = pi + 2 * d1 - 2 * d2
                y += yi
            x += xi
            plot(x, y)