class rectangle:

    def __init__(self,name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def pgrect(self):
        print("heyhey")

    def push(self, item):
        self._stack.append(item)

    def __len__(self):
        return len(self.rectangle)



rectangle1 = rectangle("input1", 390, 300, 320, 280)
rectangle.push()
rectangle2 = rectangle("input1", 390, 300, 320, 280)


print(len(rectangle))

