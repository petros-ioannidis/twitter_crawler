

class word_emotion_marker:
    
    def __init__(self,text,feeling):
        
        textfile = open(text,"r")
        feelingfile = open(feeling,"r")
        punctuation = ['.',',','!','?','"','-',':',')','(',']','[','}','{','<','>','\\','/','*','&','^','%','$','+','-','=','|'] 
        self.textfeel_dict = dict()
        feelings = dict()
        f = feelingfile.readline()
        while f:
            feel = f.split("\t")
            feel1 = int(feel[-1])
            feelings[feel[0]] = feel1
            f = feelingfile.readline()
        t = textfile.readline()
        while t:

            word_list1 = t.split("\t")
            word_list = word_list1[-1]
            print word_list
            for i in punctuation:
                word_list = word_list.replace(i,' ')
            print word_list
            word_list = word_list.split()
            word_list = set(word_list)
            print word_list
            
            for word in word_list:
                if word[0] != '@':
                    if not self.textfeel_dict.has_key(word.lower()):
                        self.textfeel_dict[word.lower()] = 0
                    self.textfeel_dict[word.lower()] += feelings[word_list1[0]]
            
            print self.textfeel_dict
            t = textfile.readline()
            f = feelingfile.readline()
    def get_word_feeling(self,word):
        return self.textfeel_dict[word]
    
    def write_to_file(self,filename):
        f = open(filename,"w")
        for i in sorted(self.textfeel_dict.keys()):
            f.write(str(i) + " " + str(self.textfeel_dict[i])+"\n")


anal = word_emotion_marker('annotatedtweets.txt','annotated.txt')
anal.write_to_file('feelings.txt')

        