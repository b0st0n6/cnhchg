def dvd(x, y):
    
    textSize(60)
    text('DVD', x, y, 45)
    ellipse(x + 60, y + 20, 150, 35)
    textSize(25)

    text('v i d e o', x + 15, y + 30)
    

    
def setup():
    size(1000, 800)


x = 0
y = 0
speedX = 3
speedY = 3
def draw():
    global x, y, speedX, speedY
    background(0)
    x += speedX
    y += speedY
    dvd(100 + x, 200 + y)
    
    if y > height - 250 or y < 0 - 150:
        fill(random(255), random(255), random(255))
        speedY = -speedY

    if x > width - 240 or x < 0 - 90:
        fill(random(255), random(255), random(255))
        speedX = -speedX



    

    
