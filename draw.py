from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 > x1:
        xtemp = x0
        x0 = x1
        x1 = xtemp
        ytemp = y0
        y0 = y1
        y1 = ytemp

    #vertical
    if x0 == x1:
        if y0 < y1:
            Ystart = y0
            Yend = y1
            while Ystart <= Yend:
                plot(screen, color, x0, Ystart)
                Ystart+=1
        else:
            Ystart = y1
            Yend = y0
            while Ystart >= Yend:
                plot(screen, color, x0, Ystart)
                Ystart-=1

    #horizontal
    elif y0 == y1:
        Xstart = x0
        Xend = x1
        while Xstart < Xend:
            plot(screen, color, Xstart, y0)
            Xstart+=1

    else:
        x = x0
        y = y0
        A = y1 - y0
        B = (x1-x0) * -1
        #check octants
        slope = A/(B * -1)
        # + slope
        if slope >= 0 and slope <=1: #slope < 1 --> octant 1 & 5
            d = 2*A + B
            while x <= x1:
                plot(screen, color, x, y)
                if d >= 0:
                    y+=1
                    d += 2*B
                x+=1
                d += 2*A
        elif slope > 1:  #octant 2 & 6
            d = A + 2*B
            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+=1
                    d += 2*A
                y+=1
                d += 2*B
        # - slope
        elif slope <= -1: #octant 7 & 3
            d = 2*B - A
            while y >= y1:
                plot(screen, color, x, y)
                if d <= 0:
                    x+=1
                    d -= 2*A
                y-=1
                d += 2*B
        elif slope < 0 and slope > -1:  #octant 8 & 4
            d = B - 2*A
            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y-=1
                    d += 2*B
                x+=1
                d -= 2*A
