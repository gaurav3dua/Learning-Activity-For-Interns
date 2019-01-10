fname = "Test_TextFile.txt"

num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print(num_words)
