from adafruit_circuitplayground import cp
while True:
    x, y, z = cp.acceleration
    if x > 5:
        cp.pixel[8] = ((0, 255, 0))
        cp.pixel[7] = ((0, 255, 0))
        cp.pixel[6] = ((0, 255, 0))
    
    elif x < -5:
        cp.pixel[1] = ((0, 255, 0))
        cp.pixel[2] = ((0, 255, 0))
        cp.pixel[3] = ((0, 255, 0))