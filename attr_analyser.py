class analyzer:
    
    def __init__(self,pos_words_file,neg_words_file,sentiment,tweet = None):
        """
        The analyzer is an object that performs
        analysis to a tweet string extracting
        useful information and stores that information 
        in a list of tuples in the following form:
        (tweet id, user id, number of followers, number of following),
        (timestamp),(number of references to other users),(number of hyperlinks),
        (number of positive words),(number of negative words),(number of negations),
        (number of exclamation marks),(number of question marks),(number of quotes),
        (number of retweets),(number of uppercase letters),(number of lowcase letters),
        (number of positive emoticons),(number of negative emoticons))
        """
        print "Initializing attribute analyser."
        feelingfile = open(sentiment,"r")
        f = feelingfile.readline()
        self.feelings = dict()
        while f:
            feel = f.split("\t")
            feel1 = int(feel[-1])
            print feel[1]
            self.feelings[feel[1]] = feel1
            f = feelingfile.readline()
        print self.feelings
        self.tup_tweet = ()
        self.tweet = tweet
        self.analysis_list = [] 
        self.positive_emoticon_list = [':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', 
                                       '8)', '=)', ':}', ':^)', ':-D', ':D', '8-D', '8D', 
                                       'x-D', 'xD', 'X-D', 'XD', '=-D', '=D', '=-3', '=3',
                                       'B^D', ':-))', ':\'-)', ':\')', ':*', ':^*',
                                       '( \'}{\' )', ';-)', ';)', '*-)', '*)', ';-]',
                                       ';]', ';D', ';^)', ':-,', '>:P', ':-P', ':P', 
                                       'X-P', 'x-p', 'xp', 'XP', ':-p', ':p', '=p', 
                                       ':-b', ':b', 'O:-)', '0:-3', '0:3', '0:-)', '0:)', 
                                       '0;^)', 'o/\o', '^5', '>_>^', '^<_<', '|;-)',
                                       '#-)', '%-)', '%)', '*\0/*', '@}-;-\'---', '@>-->--',
                                       '<3', '(\';\')', '^_^', '(^_^)/', '(^O^)/', 
                                       '(^o^)/', '(^^)/', '>^_^<', '<^!^>', '^/^', '(*^_^*)', 
                                       '(^<^)', '(^.^)', '(^_^.)', '(^_^)', '(^^)', '(^J^)', 
                                       '(*^.^*)', '^_^', '(\#^.^\#)', '(^-^)', '(*^^)v', '(^^)v', 
                                       '(^_^)v', '( ^)o(^ )', '(^O^)', '(^o^)', ')^o^(']
        
        self.negative_emoticon_list = ['>:[', ':-(', ':(',  ':-c', ':c', ':-<', ':<', ':-[', 
                                       ':[',' :{\'', ':-||', ':@', ':\'-(', ':\'(\'', 'D:<', 
                                       'D:', 'D8' ,'D;', 'D=', 'DX', 'v.v', 'D-\':', '>:\\', 
                                       '>:/', ':-/', ':-.', ':/', ':\\', '=/', '=\\', ':S', 
                                       '>.<\'', '>:)', '>;)', '>:-)', '}:-)', '}:)', '3:-)', 
                                       '3:)', ':-\#\#\#..', ':\#\#\#..', '</3', '(^_^;)',
                                       '(-_-;)', '(~_~;)', '((+_+))', '(+o+)','(-"-)', 'STO', 
                                       'OTZ', 'OTL', 'orz']
        self.negation_test = ['can\'t','don\'t',' not ',' cannot ','didn\'t','haven\'t','hadn\'t','won\'t','shouldn\'t']
        self.hyperlink_test = ['http://']
        self.quotes_test = ['\"']
        self.exclamation_test = ['!']
        self.question_test = ['?']
        self.reference_test = ['@a','@b','@c','@d','@e','@f','@g','@h','@i','@j','@k','@l','@m','@n','@o','@p','@q','@r','@s','@t','@u','@v','@w','@x','@y','@z',
                               '@A','@B','@C','@F','@E','@F','@G','@H','@I','@J','@K','@L','@M','@N','@O','@P','@Q','@R','@S','@T','@U','@V','@W','@X','@Y','@Z']
        self.positive_test = open(pos_words_file,"r")
        self.positive_test = self.positive_test.read()
        self.positive_test = self.positive_test.split("\n")
        print self.positive_test
        self.negative_test = open(neg_words_file,"r")
        self.negative_test = self.negative_test.read()
        self.negative_test = self.negative_test.split("\n")
        print "Attribute analyser ready."
    
    def analysis_list_out(self):
        return self.analysis_list
    
    def tweet_input(self):
        return self.tweet
    
    def has_input(self):
        if self.tweet:
            return True
        return False
    
    def read_tweet_input(self,tweet):
        """
        Sets the current twitter for analysis.
        """
        self.tup_tweet = tweet
        self.tweet = tweet[2]
    
    def num_of_symbols(self,symbol_list):
        
        if not self.has_input():
            print "No tweet input is given to the attribute analyzer."
            return None
        
        n = 0
        for symbol in symbol_list:
            if symbol in self.tweet:
                n += self.tweet.count(symbol)
        
        return n
    
    def num_of_words(self,word_list):
        
        if not self.has_input():
            print "No tweet input is given to the attribute analyzer."
            return None
        
        n = 0
        for word in word_list:
            if " "+word+" " in self.tweet.lower() or self.tweet.lower().startswith(word+" ") or self.tweet.lower().endswith(" " + word):
                n += self.tweet.count(" "+word+" ")
                if self.tweet.lower().startswith(word+" "):
                    n+=1
                if self.tweet.lower().endswith(" " + word):
                    n+=1
                    
        return n
     
    
    def num_of_upper(self):
        
        if not self.has_input():
            print "No tweet input is given to the attribute analyzer."
            return None
        
        n = 0
        for i in self.tweet:
            if i.isupper():
                n += 1
        return n
        
    def num_of_lower(self):
        
        if not self.has_input():
            print "No tweet input is given to the attribute analyzer."
            return None
        
        n = 0
        for i in self.tweet:
            if i.islower():
                n += 1
        return n        
    def basic_test(self):
        
        if not self.has_input():
            print "No tweet input is given to the attribute analyzer."
            return None
        try:
            print "Tweet: "
            print self.tweet
            print "Calculating number of positive emoticons."
            positive_emoticons = self.num_of_symbols(self.positive_emoticon_list)
            print "Calculated number of positive emoticons: " + str(positive_emoticons)
            
            print "Calculating number of negative emoticons."
            negative_emoticons = self.num_of_symbols(self.negative_emoticon_list)
            print "Calculated number of negative emoticons: " + str(negative_emoticons)
            
            print "Calculating number of hyperlinks."
            hyperlinks = self.num_of_symbols(self.hyperlink_test)
            print "Calculated number of hyperlinks: " + str(hyperlinks)
            
            print "Calculating number of quotes."
            quotes = self.num_of_symbols(self.quotes_test)
            print "Calculated number of quotes: " + str(quotes)
           
            print "Calculating number of exclamation marks."
            excl_marks = self.num_of_symbols(self.exclamation_test)
            print "Calculated number of exclamation marks: " + str(excl_marks)
            
            print "Calculating number of question marks."
            question_marks = self.num_of_symbols(self.question_test)
            print "Calculated number of question marks: " + str(question_marks)
            
            print "Calculating number of references."
            ref = self.num_of_symbols(self.reference_test)
            print "Calculated number of references: " + str(ref)
            
            print "Calculating number of negations."
            negations = self.num_of_symbols(self.negation_test)
            print "Calculated number of references: " + str(negations)
        
            print "Calculating number of lowercase letters."
            low = self.num_of_lower()
            print "Calculated number of lowercase letters: " + str(low)

            print "Calculating number of uppercase letters."
            upp = self.num_of_upper()
            print "Calculated number of uppercase letters: " + str(upp)
            
            print "Calculating number of positive words."
            pos = self.num_of_words(self.positive_test)
            print "Calculated number of positive words: " + str(pos)
            
            print "Calculating number of negative words."
            neg = self.num_of_words(self.negative_test)
            print "Calculated number of negative words: " + str(neg)
        except:
            print "Problem in test,tweet requires manual testing"
            return None
        self.analysis_list.append((self.tup_tweet[1],self.tup_tweet[0],self.tup_tweet[4],self.tup_tweet[3],
                                  self.tup_tweet[5],ref,hyperlinks,pos,neg,negations,excl_marks,quotes,self.tup_tweet[6],
                                  upp,low,positive_emoticons,negative_emoticons,self.feelings[str(self.tup_tweet[1])]))    
        return (positive_emoticons,negative_emoticons,hyperlinks,quotes,excl_marks,question_marks,ref,negations,low,upp,pos,neg)
            