# DNA Toolset/Code testing file
from dna_toolkit import *
from utilities import colored
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(DNA_Nucleotides)
                      for nuc in range(60)])

DNAStr = validate_seq(randDNAStr)

print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {nucleotide_frequency(DNAStr)}\n')

print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')

print(f"[4] + DNA String + Complement + Reverse Complement:\n5' {DNAStr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement ]\n")
