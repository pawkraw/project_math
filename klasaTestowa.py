from datetime import datetime
from functools import total_ordering
import math




class Integer:
    def __init__(self, int1: int):
        self.int1 = int1

    def __repr__(self):
        return f"{self.int1}"

    def __add__(self, other):
        return self.__class__(self.int1 + other.int1)

    def __mul__(self, other):
        return self.__class__(self.int1 * other.int1)

    def __mod__(self, other):
        return self.__class__(self.int1 % other.int1)

    def __truediv__(self, other):
        return self.__class__(math.ceil(self.int1 / other.int1))

    def __floordiv__(self, other):
        if isinstance(other,self.__class__):
            return self.__class__(self.int1 // other.int1)
        elif isinstance(other, int):
            return self.__class__(self.int1 // other)
        else:
            return NotImplemented



a = Integer(8)
b = Integer(3)

print(a)
print(b)
print(a+b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)



class Foo:
    count: int = 0
    living: int = 0

    def __init__(self):
        self.__class__.count += 1
        self.__class__.living += 1

    def __del__(self):
        self.__class__.living -= 1

v1 = Foo()
v1 = Foo()

print(Foo.count)
print(Foo.living)


@total_ordering
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


v = Vehicle("Ford", 1968, 200)

print(v.year, v.age, v.energy)

v.energy = 10
print(v.energy)


v1 = Vehicle("Ford", 1968, 200)

v2 = Vehicle("BMW", 1998, 120)

print(v1 > v2)



class Employee:
    def __init__(self, name: str, rate_per_hour: float):
        self.name = name
        self.rate_per_hour = rate_per_hour
        self.worked_hours = 0

    def register_time(self, t):
        self.worked_hours = t

    def pay_salary(self):
        return self.worked_hours * self.rate_per_hour




e = Employee("Stefan", 100.0)

salary = e.pay_salary()

print(salary)

