import logging
import math

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
        """
        Pseudo code:
        begin
            plot (x1, y1);
            for (i= x1 to x2 by step of 1) {
                if (i== x1 ) {
                    pi=2Δy−Δx;
                }
                else {
                    if ( pi<0 ) {
                        pi= pi+2 Δ y;
                    }
                    else {
                        pi= pi+2 Δ y−2Δ x;
                        y1++;
                    }
                    x1++;
                    plot (x1, y1);
                }
            }
        end
        """
        def plot(x, y, c=color):
            self.drawPixel((x, y), c)
        
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        try:
            m = dy / dx
        except ZeroDivisionError:
            m = None

        if m is not None:
            if x1 < x2 and y1 < y2 and 0 <= m and m <= 1: # 1st octant
                c = (255, 0, 0)
                plot(x1, y1, c)
                for i in range(x1, x2): # TODO: check that +1 is necessary
                    if i == x1:
                        pi = 2 * dy - dx
                    else:
                        if pi < 0:
                            pi = pi + 2 * dy
                        else:
                            pi= pi + 2 * dy - 2 * dx;
                            y1 += 1
                        x1 += 1
                        plot(x1, y1, c)
            elif x1 < x2 and y1 < y2 and 1 < m and m < math.inf: # 2nd octant
                c = (255, 127, 0)
                plot(x1, y1, c)
                for i in range(x1, x2): # TODO: check that +1 is necessary
                    if i == x1:
                        pi = 2 * dy - dx
                    else:
                        if pi < 0:
                            pi = pi + 2 * dy
                        else:
                            pi= pi + 2 * dy - 2 * dx;
                            x1 += 1
                        y1 += 1
                        plot(x1, y1, c)
            else:
                # print(f"line {p1} to {p2} with slope {m} not drawn")
                pass
        elif dx == 0: # vertical line
            # print(f"line {p1} to {p2} vertical line")
            pass
            for y in range(y1, y2+1):
                plot(x1, y, (128, 0, 128))
        else:
            # print(f"line {p1} to {p2} with undefined slope not drawn")
            pass