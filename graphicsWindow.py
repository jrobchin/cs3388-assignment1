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
            plot (x1, y1)
            for (i= x1 to x2 by step of 1) {
                if (i== x1 ) {
                    pi=2Δy−Δx
                }
                else {
                    if ( pi<0 ) {
                        pi= pi+2 Δ y
                    }
                    else {
                        pi= pi+2 Δ y−2Δ x
                        y1++
                    }
                    x1++
                    plot (x1, y1)
                }
            }
        end
        """
        plot = lambda x, y, c=color: self.drawPixel((x, y), c)
        sign = lambda x: x and (1, -1)[x<0]

        x1, y1 = p1
        x2, y2 = p2
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        dxSign = sign(x2 - x1)
        dySign = sign(y2 - y1)
        try:
            m = dy*dySign / dx*dxSign
        except ZeroDivisionError:
            m = None

        if dx >= dy:
            d1, y, ySign = dy*dySign, y1, dySign
            d2, x, xSign = dx*dxSign, x1, dxSign
        else:
            d1, y, ySign = dx*dxSign, x1, dxSign
            d2, x, xSign = dy*dySign, y1, dySign

        c = (255, 0, 0)
        plot(x, y, c)
        pi = 2 * d1 - d2
        for i in range(abs(d2)):
            if pi < 0:
                pi = pi + 2 * d1
            else:
                pi = pi + 2 * d1 - 2 * d2
                y += ySign
            x += xSign
            if x >= 512 or y >= 512:
                breakpoint()
                pass
            else:
                plot(x, y, c)

        # if m is not None:
        #     if x1 < x2 and y1 < y2 and 0 <= m and m <= 1: # 1st octant
        #         c = (255, 0, 0)
        #         plot(x1, y1, c)
        #         pi = 2 * dy - dx
        #         for i in range(abs(dx)):
        #             if pi < 0:
        #                 pi = pi + 2 * dy
        #             else:
        #                 pi = pi + 2 * dy - 2 * dx
        #                 y1 += 1
        #             x1 += 1
        #             plot(x1, y1, c)
        #     elif x1 < x2 and y1 < y2 and 1 < m and m < math.inf: # 2nd octant
        #         c = (0, 255, 0)
        #         plot(x1, y1, c)
        #         pi = 2 * dx - dy
        #         for i in range(abs(dy)):
        #             if pi < 0:
        #                 pi = pi + 2 * dx
        #             else:
        #                 pi = pi + 2 * dx - 2 * dy
        #                 x1 += 1
        #             y1 += 1
        #             plot(x1, y1, c)
        #     elif x1 > x2 and y1 < y2 and -1 > m and m > -math.inf: # 3rd octant
        #         c = (0, 0, 255)
        #         plot(x1, y1, c)
        #         pi = 2 * -dx - dy
        #         for i in range(abs(dy)):
        #             if pi < 0:
        #                 pi = pi + 2 * -dx
        #             else:
        #                 pi = pi + 2 * -dx - 2 * dy
        #                 x1 -= 1
        #             y1 += 1
        #             plot(x1, y1, c)
        #     elif x1 > x2 and y1 < y2 and 0 >= m and m >= -1: # 4th octant
        #         c = (255, 255, 0)
        #         plot(x1, y1, c)
        #         pi = 2 * dy - -dx
        #         for i in range(abs(dx)):
        #             if pi < 0:
        #                 pi = pi + 2 * dy
        #             else:
        #                 pi = pi + 2 * dy - 2 * -dx
        #                 y1 += 1
        #             x1 -= 1
        #             plot(x1, y1, c)
        #     elif x1 > x2 and y1 > y2 and 0 < m and m <= 1: # 5th octant
        #         c = (65, 0, 165)
        #         plot(x1, y1, c)
        #         pi = 2 * -dy - -dx
        #         for i in range(abs(dx)):
        #             if pi < 0:
        #                 pi = pi + 2 * -dy
        #             else:
        #                 pi = pi + 2 * -dy - 2 * -dx
        #                 y1 -= 1
        #             x1 -= 1
        #             plot(x1, y1, c)
        #     elif x1 > x2 and y1 > y2 and 1 < m and m < math.inf: # 6th octant
        #         # TODO: check if this is correct
        #         c = (255, 165, 255)
        #         plot(x1, y1, c)
        #         pi = 2 * -dx - -dy
        #         for i in range(abs(-dy)):
        #             if pi < 0:
        #                 pi = pi + 2 * -dx
        #             else:
        #                 pi = pi + 2 * -dx - 2 * -dy
        #                 x1 -= 1
        #             y1 -= 1
        #             plot(x1, y1, c)
        #     elif x1 < x2 and y1 > y2 and -1 > m and m > -math.inf: # 7th octant
        #         # TODO: check if this is correct
        #         c = (255, 165, 65)
        #         plot(x1, y1, c)
        #         pi = 2 * dx - -dy
        #         for i in range(abs(-dy)):
        #             if pi < 0:
        #                 pi = pi + 2 * dx
        #             else:
        #                 pi = pi + 2 * dx - 2 * -dy
        #                 x1 += 1
        #             y1 -= 1
        #             plot(x1, y1, c)
        #     elif x1 < x2 and y1 > y2 and 0 > m and m >= -1: # 8th octant
        #         c = (0, 255, 255)
        #         plot(x1, y1, c)
        #         pi = 2 * -dy - dx
        #         for i in range(abs(dx)):
        #             if pi < 0:
        #                 pi = pi + 2 * -dy
        #             else:
        #                 pi = pi + 2 * -dy - 2 * dx
        #                 y1 -= 1
        #             x1 += 1
        #             plot(x1, y1, c)
        #     else:
        #         x = min(x1, x2)
        #         for i in range(abs(dx)):
        #             plot(x+i, y1, (128, 0, 128))
        #         pass
        # elif dx == 0: # vertical line
        #     y = min(y1, y2)
        #     for i in range(abs(dy)):
        #         plot(x1, y+i, (128, 0, 128))
        # else:
        #     raise Exception(f"{p1} to {p2} not drawn")