class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.mid_position = width + height - 2
        self.dir = 0
        self.pos = 0
        self.direction = {0: "East", 1: "North", 2: "West", 3: "South"}

    def step(self, num: int) -> None:
        self.pos += num
        self.pos %= (self.mid_position * 2)
        if self.pos > self.mid_position + self.width:
            self.dir = 3
        elif self.pos > self.mid_position:
            self.dir = 2
        elif self.pos > self.width:
            self.dir = 1
        elif not self.pos:
            self.dir = 3
        else:
            self.dir = 0

    def getPos(self) -> List[int]: 
        if self.pos > self.mid_position + self.width:
            return [0, self.height - (self.pos - self.width - self.mid_position)]
        elif self.pos > self.mid_position:
            return [self.width - (self.pos - self.mid_position), self.height]
        elif self.pos > self.width:
            return [self.width, self.pos - self.width]
        else:
            return [self.pos, 0]

    def getDir(self) -> str: 
        return self.direction[self.dir]