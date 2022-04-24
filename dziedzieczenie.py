class Vehicle:
    def __init__(self, name: str, year: int, energy: int):
        self.name = name
        self.year = year
        self.doors = 4
        self._energy = energy

    def __repr__(self):
        return f"{self.name} ({self.year} {self.year})"

    @property #atrybut dynamiczny
    def age(self):
        return datetime.now().year - self.year

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if value >= 0:
            self._energy = value
        else:
            raise ValueError("Enegia nie może być mniejsza niż 0")

    def __gt__(self, other):
        return self.energy > other.energy

    def __ne__(self, other):
        return self.energy != other.energy

    def __eq__(self, other):
        return self.energy == other.energy



class Car(Vehicle):

    def __init__(self, name, year, energy, color):
        super().__init__(name, year, energy)
        self.color = color

    def __repr__(self):
        return f"Car: {self.name, self.color}"


c = Car("Ford", 1980, 200, "green")

print(c)


class A:

    def foo(self):
        print("Foo z A")

    def a(self): pass


class B:

    def foo(self):
        print("Foo z B")

    def b(self): pass


class C:

    def foo(self):
        print("Foo z D")

    def c(self): pass


class D(A, B, C):
    pass


d = D()

d.foo()

print(D.mro()) # Kolejność dziedzieczenia (tu dla D)