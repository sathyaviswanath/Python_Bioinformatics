# DNA Parent class & Child class

class Sequence:
        
    def __init__(self, sequence):
        self.__sequence = sequence

    def get_sequence(self):
        return self.__sequence
        
    def set_sequence(self, sequence):
        if all (base in "ATGC" for base in sequence):
            self.__sequence = sequence

        else:
            raise ValueError("Invalid DNA sequence")
    
    def length(self):
        return len(self.__sequence)
    
    def reverse(self):
        return self.__sequence[::-1]
    
    def is_valid_dna(self):
        if all(base in "ATGC" for base in self.__sequence):
            return True
        else:
            return False
        
class DNA(Sequence):

    def gc_percent(self):
        sequence = self.get_sequence()
        gc = sequence.count("G") + sequence.count("C")
        return round ((gc / len(sequence)) * 100, 2)
    
    def dna_to_rna(self):
        sequence = self.get_sequence()
        return sequence.replace("T", "U")
    
    def nucleotide_count(self):
        sequence = self.get_sequence()
        counts = {
            "A": 0,
            "T": 0,
            "G": 0,
            "C": 0
        }
        
        for base in sequence:
            counts[base] += 1

        return counts
            
    def has_start_codon(self):
        sequence = self.get_sequence()
        if sequence.startswith("ATG"):
            return "Start codon found"
        else:
            return "Start codon not found"
            
    def has_stop_codon(self):
        sequence = self.get_sequence()
        if any(stop in sequence for stop in ["TAA","TAG","TGA"]):
            return "Stop codon found"
        else:
            return "No stop codon"        
        
    def __str__(self):
        sequence = self.get_sequence()
        return(
            f"DNA Sequence: {sequence}\n"
            f"Length: {len(sequence)}\n"
            f"GC%: {self.gc_percent()}\n"
            f"RNA Sequence: {self.dna_to_rna()}"
            )
    
    def __repr__(self):
        sequence = self.get_sequence()
        return f"DNA('{sequence}')"