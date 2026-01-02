from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast("blastn", "nt", "AGTCTAGAC")
