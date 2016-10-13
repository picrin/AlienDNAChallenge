import random
genome = ["DDFADBDFADBFBA", "ABDBDFADFEFABDBDBEFACAEBDAB", "DCFCCAC"]

def cutChromosome(cuttingPlace, chromosome):
    result = []
    pieces = chromosome.split(cuttingPlace)
    for piece in pieces[:-1]:
        result.append(piece + cuttingPlace)
    if pieces[-1] != '':
        result.append(pieces[-1])
    random.shuffle(result)
    return result

print("genome", genome)
print("cutting first chromosome at DFAD", cutChromosome("DFAD", genome[0]))
print("cutting second chromosome at BD", cutChromosome("BD", genome[1]))
print("cutting third chromosome at C", cutChromosome("C", genome[2]))
