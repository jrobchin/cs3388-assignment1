"""
CS3388 Assignment 1

by Jason Chin
250920898
"""

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
        # function for getting the sign of a number
        sign = lambda x: x and (1, -1)[x<0]
        
        # decompose x and y from points
        x1, y1, x2, y2 = *p1, *p2
        # calculate deltas and signs
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        sX, sY = sign(x2 - x1), sign(y2 - y1)

        # each case dictates by which axis you increment
        if dx >= dy:
            # if the absolute slope is between 0 and 1
            # plot as if in octant 1 where the sign of dx and dy determine
            # if we are incrementing or decrementing
            plot = lambda x, y, c=color: self.drawPixel((x, y), c)
            x, xi, y, yi, d1, d2 = x1, sX, y1, sY, dy, dx
        elif dy > dx:
            # if the absolute slope is between 1 and infinity
            # plot as if in octant 2 where the sign of dx and dy determine
            # if we are incrementing or decrementing
            x, xi, y, yi, d1, d2 = y1, sY, x1, sX, dx, dy
            plot = lambda x, y, c=color: self.drawPixel((y, x), c)
        
        # general plotting algorithm that plots depending on
        # how the parameters are set
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
