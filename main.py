from display import *
from draw import *

screen = new_screen()
color = [ 153, 153, 255 ]

#horizontal
draw_line(0, 250, 499, 250, screen, color)
#vertical
draw_line(250, 0, 250, 499, screen, color)

#slope = 1
draw_line(0, 0, 499, 499, screen, color)
#slope = -1
draw_line(0, 499, 499, 0, screen, color)

xBeg = 0
xEnd = 499
yBeg = 0
yEnd = 0

for xBeg in range(0,499,5):
    draw_line(xBeg, 0, 499, yEnd, screen, color)
    yEnd += 10

yEnd = 0
xBeg = 499
while xBeg > 0:
    draw_line(xBeg, 0, 0, yEnd, screen, color)
    yEnd += 10
    xBeg -= 5

yEnd = 499
xBeg = 0
yBeg = 499
xEnd = 499
while yEnd > 0:
    draw_line(xBeg, yBeg, xEnd, yEnd, screen, color)
    yEnd -= 10
    xBeg += 5

yEnd = 499
xBeg = 499
yBeg = 499
xEnd = 0
while yEnd > 0:
    draw_line(xBeg, yBeg, xEnd, yEnd, screen, color)
    yEnd -= 10
    xBeg -= 5




display(screen)
save_extension(screen, 'img.png')
