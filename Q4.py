import nltk
from nltk import FreqDist
import pandas as pd

fname = "Test_TextFile.txt"
myFile = open(fname)
p = myFile.read()

words = nltk.tokenize.word_tokenize(p)
tagged_sent = nltk.pos_tag(words)
nouns = []
for word, pos in tagged_sent:
    if pos in ['NN', "NNP", "NNS", "NNPS"] and word.isalpha():
        nouns.append(word)
nouns.sort()
fDist = FreqDist(nouns)
df = pd.DataFrame(fDist, index=[0])
print(df)
myFile.close()
