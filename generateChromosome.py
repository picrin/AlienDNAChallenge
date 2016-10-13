#!/bin/env python
from __future__ import print_function
import Crypto.Random.random as srandom
import sys
geneticCode = ["A", "B", "C", "D", "E", "F"]
for _ in range(int(sys.argv[1])):
    print(srandom.choice(geneticCode), end="")
