import nltk
#from pprint import pprint
from nltk import FreqDist
import pandas as pd

fname = "Test_TextFile.txt"
myFile = open(fname)
p = myFile.read()
words = nltk.tokenize.word_tokenize(p)
fDist = FreqDist(words)
#pprint(fDist)
df = pd.DataFrame(fDist, index=[0])
print(df)
