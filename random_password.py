#!/usr/bin/env python
""" PEP8 compliant """

import string
import random

__author__ = "bashrootshell"
__license__ = "BSD New"
__version__ = "1.0"
__status__ = "Production"


def main():
    """ Random Password Generator """

    char = string.ascii_letters + string.punctuation + string.hexdigits
    rd = random.SystemRandom(None)
    randompassword = ''.join(rd.choice(char) for values in xrange(20))
    print '\n'*2
    print "RANDOM Password:", randompassword
    print '\n'*2


if __name__ == "__main__":

    main()
