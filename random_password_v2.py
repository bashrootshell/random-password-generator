#!/usr/bin/env python3

from secrets import choice

"""
    Random Password Generator v2 > cleaner code in Python3
    It now uses secrets in preference to random,
    according to the newest recommendations...
    (although the SystemRandom class is implemented
    by simply importing this module from random.)
    Use secrets.choice instead of random.choice for
    cryptographically secure implementations.

    PEP8 compliant
    “Simple is better than complex.”
    — The Zen of Python
"""

char = 'abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#*%$@:;._-~+?[]()<>/|=^'

[randompassword := ''.join(choice(char) for _ in range(20))]

print(f'Chosen password with 20 characters >> "{randompassword}"')
