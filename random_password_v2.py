#!/usr/bin/env python3

from secrets import choice
from random import sample

"""
    Random Password Generator v2 > cleaner code in Python3
    It uses secrets (best for CSPRNG) and random modules,
    according to the newest recommendations.
    Use secrets.choice instead of random.choice for
    cryptographically secure implementations.

    PEP8 compliant
    “Simple is better than complex.”
    — The Zen of Python
"""

char = 'abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#*%$@:;._-~+?[]()<>/|=^'

[randompassword1 := ''.join(choice(char) for _ in range(20))]
[randompassword2 := ''.join(sample(char, 20))]

print(f'Chosen password with 20 characters (secrets)>> "{randompassword1}"')
print(f'Chosen password with 20 characters (sample)>> "{randompassword2}"')
