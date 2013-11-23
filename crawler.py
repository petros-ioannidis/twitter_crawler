import sys
import random
import tweepy


class crawler:
    
    def __init__(self,filename):
        
        try:
            f = open(filename,'r')
        except:
            print("Filename Problem")
            exit(-1)
        
        self.random = False
        self.tweets = []
        self.api = tweepy.API()
        self.database = []
        buf = f.readline()
        counter = 1
        while buf:
            buf = buf.replace("\n","")
            temp = buf.split("\t")
            temp = (temp[0],temp[1])
            try:
                self.database.append((eval(temp[0]),eval(temp[1])))
            except ValueError as e:
                print e
                print "Error in line " + str(counter) + "\n" + buf
                print "Line " + str(counter) + " will not be added in database."
            buf = f.readline()
            counter += 1
            
    def get_tweets_gathered(self):
        return self.tweets      
    
    def random_tweets(self,number):
        assert number > 0
        while(len(self.tweets) < number):
            user_id,tweet_id = random.choice(self.database)
            try:
                print "Request " + str(len(self.tweets)) + ": Receiving Tweet " + str(tweet_id) + " from User " + str(user_id)
                tweet = self.api.get_status(tweet_id)
                user = self.api.get_user(user_id)
                if (user_id,tweet_id,tweet.text,user.friends_count,user.followers_count,tweet.created_at,tweet.retweet_count) not in self.tweets:
                    self.tweets.append((user_id,tweet_id,tweet.text,user.friends_count,user.followers_count,tweet.created_at,tweet.retweet_count))
                else:
                    print "Duplicate,trying again."

            except (tweepy.error.TweepError,UnicodeEncodeError) as e:
                print str(e)
        self.random = True
    def gather_all_tweets(self): 
        count = 0
        errors = ['Rate limit exceeded. Clients may not make more than 150 requests per hour.',
                  'Failed to send request: [Errno 10053] An established connection was aborted by the software in your host machine',
                  'Failed to send request: [Errno 11004] getaddrinfo failed',
                  'Failed to send request: [Errno 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond']
        for user_id,tweet_id in self.database:
            try_flag = True
            while try_flag:
                try:
                    count += 1
                    print "Currently in the database: " + str(len(self.tweets))
                    print "Request " + str(count) + ": Receiving Tweet " + str(tweet_id) + " from User " + str(user_id)
                    tweet = self.api.get_status(tweet_id)
                    user = self.api.get_user(user_id)
                    if (user_id,tweet_id,tweet.text,user.friends_count,user.followers_count,tweet.created_at,tweet.retweet_count) not in self.tweets:
                        self.tweets.append((user_id,tweet_id,tweet.text,user.friends_count,user.followers_count,tweet.created_at,tweet.retweet_count))          
                    else:
                        print "Duplicate,ommiting current tweet."
                    try_flag = False
                except (tweepy.error.TweepError,UnicodeEncodeError) as e:
                    print str(e)
                    if str(e) in errors:
                        raw_input("waiting:")
                        print "Trying again."
                    else:
                        print "Ommiting current tweet."
                        try_flag = False
                   
    def write_tweets_to_file(self,out):
        
        output = open(out,"w")
        complete = open("complete"+out,"w")
        final = open("final"+out,"w")
        print "Saving tweets to ouput."
        for i in self.tweets:
            try:
                
                final.write(str(i[0])+"\t"+str(i[1])+"\n")
                output.write(str(i[0])+"\t"+str(i[1])+"\t"+str(i[2])+"\n")
                complete.write(str(i)+"\n")
                
            except:
                print "Problem while writing tweets in file."
                if self.random:
                    "Inserting another random tweet in the database."   
                    self.random_tweets(1)
                    
                else:
                    print "Trying next tweet." 
        print "Saving completed successfully."            

c = crawler(sys.argv[1])
#c.random_tweets(2)
c.gather_all_tweets()
c.write_tweets_to_file("tweets.txt")
        
