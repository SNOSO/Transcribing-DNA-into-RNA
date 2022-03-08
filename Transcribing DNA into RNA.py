# open file and set as variable
data = open('rosalind_rna.txt')

# set variabe to read file
RNA = data.read()

#print replaced elements of file
print(RNA.replace('T','U'))