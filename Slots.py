class NormalClass:
    classvar = "foo"

    def __init__(self):
        self.x = 1
        self.y = 2

n = NormalClass()

print(n.__dict__)

n.z = 100

print(n.__dict__)


class SlottedClass:
    classvar = "foo"
    __slots__ = ("x", "y")

    def __init__(self):
        self.x = 1
        self.y = 2

n = SlottedClass()

n.x = 20

n.z = 100 # Tu wypluje błąd bo są sloty

