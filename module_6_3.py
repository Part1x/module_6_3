class Horse:

    def __init__(self, x_distance, sound):
        self.x_distance = int(x_distance)
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:

    def __init__(self, y_distance, sound):
        self.y_distance = int(y_distance)
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0, y_distance=0, sound = ""):
        Horse.__init__(self, x_distance, sound)
        Eagle.__init__(self, y_distance, sound)

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

