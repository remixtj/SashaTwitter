'''
Created on 29/dic/2011

@author: remix_tj
'''

import markov_class
import random
import re
import twitter
import ConfigParser

class Handlemsg():
    CONSUMER_KEY=''
    CONSUMER_SECRET=''
    ACCESS_TOKEN_KEY=''
    ACCESS_TOKEN_SECRET=''
    nickname = ""
    chattiness = 0.05
    chain_length = 3
    max_words = 1000
    lastid = 0
    api = twitter.Api()
    mrk = markov_class.MarkovClass

    def __init__(self):
        '''
        Constructor
        '''
        Config = ConfigParser.ConfigParser()
        Config.read('config.ini')
        self.CONSUMER_KEY= Config.get('config','CONSUMER_KEY')
        self.CONSUMER_SECRET=Config.get('config','CONSUMER_SECRET')
        self.ACCESS_TOKEN_KEY=Config.get('config','ACCESS_TOKEN_KEY')
        self.ACCESS_TOKEN_SECRET=Config.get('config','ACCESS_TOKEN_SECRET')
        self.nickname = Config.get('config','nickname')
        
        self.api = twitter.Api(consumer_key=self.CONSUMER_KEY, consumer_secret=self.CONSUMER_SECRET, access_token_key=self.ACCESS_TOKEN_KEY, access_token_secret=self.ACCESS_TOKEN_SECRET)
        try:
            filen = open("lastid.txt")
            while 1:
                fline = filen.readline()
                if not fline:
                    break
                else:
                    self.lastid = int(fline)
                pass
        except:
            pass
         
        self.mrk = markov_class.MarkovClass(self.chain_length)
    
    def newmsg(self, msg, user,id):
        if self.nickname in msg:
            #print msg
            msg = re.compile("@"+self.nickname + " ", re.I).sub('', msg)
            prefix = "@%s " % (user, )
        else:
            prefix = ''
        
        self.mrk.add_to_brain(msg, self.chain_length, write_to_file=True)
        if prefix or random.random() <= self.chattiness:
            sentence = self.mrk.generate_sentence(msg, self.chain_length, self.max_words)
            if sentence:
                if prefix:
                    self.tweetmsg(prefix + sentence,statusid=id)
                else:
                    self.tweetmsg(prefix + sentence) 
                
                
    def tweetmsg(self,msg,statusid=-1):
        if statusid == -1:
            status = self.api.PostUpdate(msg)
        else:
            status = self.api.PostUpdate(msg,in_reply_to_status_id=id)
        self.lastid = status.id
    
    def parseFriendsMsg(self):
        statuses = self.api.GetFriendsTimeline(user=self.nickname,since_id=(self.lastid+1))
        #print "Last ID was "+self.lastid.__str__()
        
        for s in statuses:
            #print "Parsing msg with id "+ s.id.__str__() +" from "+s.user.screen_name
            # if s.id > self.lastid and s.user.screen_name != "Sashagrigio":
            if s.user.screen_name != self.nickname:
                try:
                    self.newmsg(s.text, s.user.screen_name,id)
                except:
                    pass
                print "Terminated parsing msg with id "+ s.id.__str__() +" from "+s.user.screen_name
                if s.id > self.lastid:
                    filen = open("lastid.txt", 'w')
                    filen.write(s.id.__str__())
                    filen.close()
                    self.lastid = s.id
                    
    def learnFrom(self, user):
        statuses = self.api.GetUserTimeline(user,count=150)
        
        for s in statuses:
            if s.user.screen_name != self.nickname:
                try:
                    msg = s.text
                    if self.nickname in msg:
                        msg = re.compile("@"+self.nickname + " ", re.I).sub('', msg)
                        
                    self.mrk.add_to_brain(msg, self.chain_length, write_to_file=True)
                except:
                    pass
                print "Terminated parsing msg with id "+ s.id.__str__() +" from "+s.user.screen_name
        
        