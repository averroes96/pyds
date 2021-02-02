from __future__ import print_function
from pyds import MassFunction


a = MassFunction([
    ({"B"}, 0.1),
    ({"J"}, 0.2),
    ({"S"}, 0.1),
    ({"B","J"}, 0.1),
    ({"B","S"}, 0.1),
    ({"J","S"}, 0.3),
    ({"B","J","S"}, 0.1)
])

print("Belief:\n")

for key,val in a.bel().items():
    print(f"{key} => {val}")

print("=" * 96)

print("Plausibility:\n")

for key,val in a.pl().items():
    print(f"{key} => {val}")

print("=" * 96)

print("Disbelieve:\n")

print(a.dis())