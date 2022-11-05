def countingValleys(steps, path):
    new=list(path)
    position,value = 0,0
    for i in new:
        if i == 'U' and position == -1:
            value += 1
            position += 1
        elif i == 'U' and position != -1:
            position += 1
        elif i == 'D':
            position -= 1
    return (value)
