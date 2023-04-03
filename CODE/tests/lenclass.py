class Stack:
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        self._stack.pop()

    def __len__(self):
        return len(self._stack)





print(len(Stack))
