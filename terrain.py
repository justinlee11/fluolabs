cols, rows = 0, 0
scl = 20

angle = 0
flying = 0
def setup():
    global cols, rows, terrain
    size(600, 600, P3D)
    w = 800
    h = 800
    cols = w/scl
    rows = h/scl
    terrain = [[0] * rows for i in range(cols)]

    
def draw():
    global flying
    yoff = flying
    for y in range(rows):
        xoff = 0
        for x in range(cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -100, 100)
            xoff += 0.2
        yoff += 0.2
    flying -= 0.15
            
    global angle
    background(0)
    stroke(255)
    noFill()
    
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-width/2 - 100, -height/2)
    
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()
