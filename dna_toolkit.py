# DNA Toolkit file
from structures import *
# from collections import Counter


def validate_seq(seq):
    """Check the sequence to make sure it is a valid DNA string"""

    tmpseq = seq.upper()
    for nuc in tmpseq:
        if nuc not in DNA_Nucleotides:
            return False
    return tmpseq


def nucleotide_frequency(seq):
    """Count nucleotides in a given sequence. Return a dictionary"""

    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

    # More Pythonic, using Counter
    # return dict(Counter(seq))


def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")


def reverse_complement(seq):
    """
    Swapping adenine with thymine and guanine with cytosine.
    Reversing newly generated string
    """
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

    # More Pythonic solution. A little bit faster solution.
    # mapping = str.maketrans('ATCG', 'TAGC')
    # return seq.translate(mapping)[::-1]
