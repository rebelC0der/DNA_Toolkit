# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)
print(countNucFrequency(DNAStr))
