

#===============================================================================
# def LenError():
#    len(tweet)<=17 
#===============================================================================
def convert(his_list):
    f=open('myfinal.arff','w')
    f.write("@RELATION tweety\n\n\
             @ATTRIBUTE tweet_id NUMERIC\n\
             @ATTRIBUTE user_id NUMERIC\n\
             @ATTRIBUTE followers NUMERIC\n\
             @ATTRIBUTE following NUMERIC\n\
             @ATTRIBUTE timestamp DATE \"yyyy-MM-dd HH:mm:ss\"\n\
             @ATTRIBUTE references NUMERIC\n\
             @ATTRIBUTE hyperlinks NUMERIC\n\
             @ATTRIBUTE positive_words NUMERIC\n\
             @ATTRIBUTE negative_words NUMERIC\n\
             @ATTRIBUTE number_of_negations NUMERIC\n\
             @ATTRIBUTE number_of_exclamations NUMERIC\n\
             @ATTRIBUTE number_of_quotes NUMERIC\n\
             @ATTRIBUTE retweeting NUMERIC\n\
             @ATTRIBUTE number_of_upper_case  NUMERIC\n\
             @ATTRIBUTE number_of_lower_case NUMERIC\n\
             @ATTRIBUTE number_of_positive_emoticons NUMERIC\n\
             @ATTRIBUTE number_of_negative_emoticons NUMERIC\n\
             @ATTRIBUTE class {Negative,Neutral,Positive}\n\n")
    
    sentiment = { -1:"Negative", 0:"Neutral", 1:"Positive" }
    
    f.write("@DATA\n")
    for tweet in his_list:
    
        for attr in tweet[:-1]:
            f.write(str(attr)+',')
        try:
            if(tweet[-1] in sentiment.keys()):
                f.write(sentiment[tweet[-1]]+'\n')
            else:
                raise ValueError
        
        except ValueError:
            print 'Value not in sentiment dictionary'
            exit(-1)
        
        #=======================================================================
        # try:
        #    LenError()
        #    print 'Attribute missing'
        #    exit(-1)
        #=======================================================================




    

    





