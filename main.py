# DNA Toolset/Code testing file
from dna_toolkit import *
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(DNA_Nucleotides)
                      for nuc in range(50)])

DNAStr = validate_seq(randDNAStr)

# print(f'\nSequence: {DNAStr}\n')
# print(f'[1] + Sequence Length: {len(DNAStr)}\n')
# print(f'[2] + Nucleotide Frequency: {nucleotide_frequency(DNAStr)}\n')

# print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')

# print(f"[4] + DNA String + Complement + Reverse Complement:\n5' {DNAStr} 3'")
# print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
# print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
# print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")

# print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
# print(
#     f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')

# print(
#     f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')

# print(
#     f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')

# print('[9] + Reading_frames:')
# for frame in gen_reading_frames(DNAStr):
#     print(frame)


test_rf_frame = ['L', 'M', 'T', 'A', 'L', 'V', 'V',
                 'L', 'L', 'R', 'R', 'G', 'S', '_', 'G', 'H']

print(proteins_from_rf(test_rf_frame))1
