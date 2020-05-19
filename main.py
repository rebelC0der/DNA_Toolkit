# DNA Toolset/Code testing file

from bio_seq import bio_seq
from utilities import read_FASTA, readTextFile, writeTextFile

test_dna = bio_seq()
test_dna.generate_rnd_seq(40, "RNA")

print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
print(test_dna.transcription())
print(test_dna.reverse_complement())
print(test_dna.gc_content())
print(test_dna.gc_content_subsec())
print(test_dna.translate_seq())
print(test_dna.codon_usage('L'))

for rf in test_dna.gen_reading_frames():
    print(rf)


print(test_dna.all_proteins_from_orfs())
