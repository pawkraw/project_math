class D:

    name = "wqr"

    @classmethod
    def class_name(cls):
        return cls.__name__

    @classmethod
    def change_name(cls, value):
        cls.name = value

D.change_name("xzy")

d = D()

print(d.name)
print(D.name)
