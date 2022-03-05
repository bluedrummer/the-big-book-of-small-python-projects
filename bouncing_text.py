import bext
import random
import time

bext.clear()
text = "Adam"
WIDTH = bext.size().columns
HEIGHT = bext.size().lines
x = 0
y = 0
ratio = WIDTH/HEIGHT
while True:
    #    bext.goto(random.randint(0, WIDTH-2), random.randint(0, HEIGHT-2))
    if x >= WIDTH and y >= HEIGHT:
        x = 0
        y = 0
    bext.goto(x,y)
    bext.fg(bext.ALL_COLORS[random.randint(0,7)])
    print(text)
    time.sleep(0.5)
    bext.clear()
    x += ratio
    y += 1

bext.clear()
