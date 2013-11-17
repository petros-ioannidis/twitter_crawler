f = open("positive_words.txt",'r')

s = set()

temp = f.readline()

while(temp):
    temp = temp.replace("\n","")
    temp = temp.split("\t")
    for i in temp:
        s.add(i.rstrip().lower())
    temp = f.readline()
    
f = open("positive_words.txt",'w')
for i in sorted(s):
    f.write(i+"\n")