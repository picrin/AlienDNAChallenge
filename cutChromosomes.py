#!/bin/env python
from __future__ import print_function
import Crypto.Random.random as random
import sys
import json
import os, os.path

with open(sys.argv[1]) as f:
    chromosome = f.readlines()[0].rstrip()

def cutChromosome(cuttingPlace, chromosome):
    result = []
    pieces = chromosome.split(cuttingPlace)
    for piece in pieces[:-1]:
        result.append(piece + cuttingPlace)
    if pieces[-1]:
        result.append(pieces[-1])
    random.shuffle(result)
    return result

def digest(restrictionSite):
    path = os.path.join("genomePieces", os.path.split(sys.argv[1])[-1] + "_digest_" + restrictionSite)
    with open(path, "w") as f:
        result = cutChromosome(restrictionSite, chromosome)
        json.dump(result, f)
        print(len(result),file=sys.stderr)

digest("BC")
digest("DFAD")
digest("EDA")
digest("DE")
