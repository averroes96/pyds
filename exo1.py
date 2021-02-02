from __future__ import print_function
from pyds import MassFunction


scientist_1 = MassFunction([
    ({"P", "C"}, 0.65),
    ({"S"}, 0.24),
    ({"P","C","S"}, 0.11)
])

scientist_2 = MassFunction([
    ({"S"}, 0.48),
    ({"P","C","S"}, 0.52)
])

scientist_3 = MassFunction([
    ({"P"}, 0.33),
    ({"C"}, 0.33),
    ({"S"}, 0.33),
])

scientist_4 = MassFunction([
    ({}, 0),
    ({"P","C","S"}, 1)
])

# Beliefs

print("Belief:\n")

print('bel_1 =', scientist_1.bel())
print("=" * 48)
print('bel_2 =', scientist_2.bel())
print("=" * 48)
print('bel_3 =', scientist_3.bel())
print("=" * 48)
print('bel_4 =', scientist_4.bel())

print("\n\n")

# Plausibility

print("Plausibility:\n")
print("=" * 48)
print('pl_1 =', scientist_1.pl())
print("=" * 48)
print('pl_2 =', scientist_2.pl())
print("=" * 48)
print('pl_3 =', scientist_3.pl())
print("=" * 48)
print('pl_4 =', scientist_4.pl())

print("\n\n")

print("Conjunctive combination:\n")
print('Dempster\'s combination rule for scientist 1, scientist 2, and scientist 3 =', scientist_1 & scientist_2 & scientist_3)

