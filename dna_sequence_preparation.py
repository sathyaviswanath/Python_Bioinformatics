# Preparing DNA SEQUENCES files for DNA Sequence analysis project

with open(r"C:\Users\sathy\OneDrive\Desktop\DNA Sequence Analysis\DNA_Sequences.txt", "w") as file:
    file.write(
        "ATGCGATCGATCG\n"
        "ATGCGCGCGCGC\n"
        "TTTTAAAAGGGG\n"
        "ATGCATGCATGC\n"
        "ATGXCGATCG\n"
        "ATGATGATGA\n"
        "CCCCGGGGTTAA"
        )

with open(r"C:\Users\sathy\OneDrive\Desktop\DNA Sequence Analysis\DNA_Sequences.txt") as file:
    contents = file.read()
print(contents)
