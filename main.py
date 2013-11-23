from attr_analyser import analyzer
from converter import convert
import datetime

a = analyzer("positive_words.txt","negative_words.txt","training_dataset.txt")

f = open("completemyfinal.txt","r")

f = f.read()
f = f.split("\n")

out = []
for i in f:
    i = eval(i)
    i = list(i)
    i[5] = str(i[5])
    i[5] = "\"" + i[5] + "\""
    out.append(tuple(i))

for i in out:
    a.read_tweet_input(i)
    a.basic_test()
print a.analysis_list_out()
convert(a.analysis_list_out())
