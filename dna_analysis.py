# DNA Analysis Main program file

from dna_class import DNA

with open(r"C:\Users\sathy\OneDrive\Desktop\DNA Sequence Analysis\DNA_Sequences.txt") as infile, \
    open(r"C:\Users\sathy\OneDrive\Desktop\DNA Sequence Analysis\Reports\DNA_Analysis_report.txt", "w") as report:

    report.write("DNA SEQUENCES ANALYSIS REPORT\n")
    report.write("===============================\n\n")

    # Summary variables
    total_sequences = 0
    valid_sequences = 0
    invalid_sequences = 0

    gc_values = []
    gc_list = []

    count = 1
    for seq in infile:
        seq = seq.strip()

        if seq == "":
            continue

        total_sequences += 1

        dna = DNA(seq)
        
        if dna.is_valid_dna():

            valid_sequences += 1

            gc = dna.gc_percent()

            gc_values.append(gc)
            gc_list.append((dna.get_sequence(), gc))

            report.write(f"Sequence: {count}: {dna.get_sequence()}\n")
            report.write(f"Length: {dna.length()}\n")
            report.write(f"Reverse seq: {dna.reverse()}\n")
            report.write(f"GC%: {gc}\n")
            report.write(f"RNA Sequence: {dna.dna_to_rna()}\n")
            report.write(f"Nucleotide counts: {dna.nucleotide_count()}\n")
            report.write(f"Start codon: {dna.has_start_codon()}\n")
            report.write(f"Stop codon: {dna.has_stop_codon()}\n")
            report.write("-------------------------------------------------\n")
            
            count += 1 

        else:

            invalid_sequences += 1

            report.write(f"Sequence {count}: {seq}\n")
            report.write("Status: INVALID DNA SEQUENCE\n")
            report.write("-----------------------------------------\n")

            count += 1

 # ---------- Summary ----------

    if gc_values:

        highest_gc = max(gc_values)
        lowest_gc = min(gc_values)
        average_gc = round(sum(gc_values) / len(gc_values), 2)

    else:

        highest_gc = 0
        lowest_gc = 0
        average_gc = 0

    report.write("\n")
    report.write("=====================================\n")
    report.write("FINAL SUMMARY\n")
    report.write("=====================================\n")

    report.write(f"Total Sequences : {total_sequences}\n")
    report.write(f"Valid Sequences : {valid_sequences}\n")
    report.write(f"Invalid Sequences : {invalid_sequences}\n")
    report.write(f"Highest GC% : {highest_gc}\n")
    report.write(f"Lowest GC% : {lowest_gc}\n")
    report.write(f"Average GC% : {average_gc}\n")


    


