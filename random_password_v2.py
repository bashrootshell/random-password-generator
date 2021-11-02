#!/usr/bin/env python3

from secrets import choice
from random import sample
from bip_utils import Bip39MnemonicGenerator as bip
from bip_utils import Bip39WordsNum

"""
    Random Password Generator v2 > cleaner code in Python3
    It uses secrets (best for CSPRNG) and random modules,
    according to the newest recommendations.
    One must use secrets.choice instead of random.choice for
    cryptographically secure implementations.
    For mnemonic passphrases, it's a good idea to use a well-known mnemonic
    generator such as bip39 (used by BTC).

    PEP8 compliant
    “Simple is better than complex.”
    — The Zen of Python
"""

char = 'abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#*%$@:;._-~+?[]()<>/|=^'

[randompassword1 := ''.join(choice(char) for _ in range(20))]
[randompassword2 := ''.join(sample(char, 20))]
[mnemonic_passphrase := bip().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)]
print(f'Chosen password with 20 characters (secrets)>> "{randompassword1}"')
print(f'Chosen password with 20 characters (sample)>> "{randompassword2}"')
print(f'Chosen mnemonic passphrase with 12 words >> "{mnemonic_passphrase}"')
