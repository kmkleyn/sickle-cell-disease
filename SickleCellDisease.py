# The purpose of this program is to translate a given DNA sequence into an amino acid sequence.
# It will also divide DNA sequences in a given text file into 2 seperate files: normal and mutated DNA.
# Finally, it will take DNA sequences in a given text file and and translate them into amino acid sequences.

# This function will translate a given DNA sequence into an amino acid sequence.
def translate(DNA_string): # The function takes an argument that is in the form of a string.

	# First, a dictionary containing the SLC for each DNA codon is created.
	codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I',
					'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'TTA':'L','TTG':'L',
					'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
					'TTT':'F', 'TTC':'F',
					'ATG':'M',
					'TGT':'C','TGC':'C',
					'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
					'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
					'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
					'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
					'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
					'TAT':'Y', 'TAC':'Y',
					'TGG':'W',
					'CAA':'Q', 'CAG':'Q',
					'AAT':'N', 'AAC':'N',
					'CAT':'H', 'CAC':'H',
					'GAA':'E', 'GAG':'E',
					'GAT':'D', 'GAC':'D',
					'AAA':'K', 'AAG':'K',
					'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
					'TAA':'_', 'TAG':'_', 'TGA':'_',
					'A':'X',
					'T':'X'
	}

	# The 'SLC' variable will store the SLC of the DNA sequence provided.
	SLC = ""
	for char in range(0, len(DNA_string), 3): # This divides each DNA sequence into groups of 3 characters.
		codon = DNA_string[char:char+3]
		SLC += codon_table[codon] # This gets the SLC code for each codon from the dictionary and adds it to the overall SLC code.
	return SLC # The final SLC is returned.

# This method changes the 'a' appearing in a DNA sequence to 'A' for normal DNA and 'T' for mutated DNA.
def mutate(read_filename, write_filename1, write_filename2): # The function takes 3 file names as an argument. The file names should appear in ' '.
	with open(read_filename, 'r') as DNA_file, open(write_filename1, 'w') as norm_file, open(write_filename2,'w') as mutate_file:
		for line in DNA_file:
			if 'a' in line:
				norm_file.write(line.replace('a','A'))
				mutate_file.write(line.replace('a','T'))

# This function makes the previous translate function able to process a file.
def txtTranslate(txt_file): # The function takes the name of a file (appearing in ' ') as an argument.
		f = open(txt_file, 'r') 
		DNA_sequence = f.read() # Each line in the given file becomes a DNA sequence.
		DNA_sequence = DNA_sequence.strip('\n') # Unnecessary characters are removed from the sequence so they don't cause an error.
		return translate(DNA_sequence) # Now that each line in the file is a string, the original translate function can be called.
	
# This code does the following using the functions created above:
# The normal DNA and the mutated DNA are written to the appropriate files.
# The DNA sequences of each file are translated to SLC and printed to the user.
mutate('DNA.txt', 'normalDNA.txt', 'mutatedDNA.txt')
print(txtTranslate('normalDNA.txt'))
print(txtTranslate('mutatedDNA.txt'))