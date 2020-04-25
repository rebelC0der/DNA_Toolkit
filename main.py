# DNA Toolset/Code testing file

from bio_seq import bio_seq

test_dna = bio_seq()
test_dna.generate_rnd_seq(40, "DNA")

print(test_dna.get_seq_info())
