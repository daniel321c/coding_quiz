class Parent:
    def __init__(self):
        self.x = 10


class Child(Parent):
    def __init__(self):
        # Parent.__init__(self)
        super().__init__()


c = Child()

print(c.x)