'''
Created on 27/dic/2011

@author: remix_tj
'''

from collections import defaultdict
import random,os
from pprint import pprint

class MarkovClass():
    '''
    classdocs
    '''
    markov = defaultdict(list)
    STOP_WORD = "\n"
    training_text = 'training_text.txt'
    
    def __init__(self,chain_lenght):
        if os.path.exists(self.training_text):
            ttf = open(self.training_text, 'r')
            for line in ttf:
                self.add_to_brain(line, chain_lenght)
            print 'Brain Reloaded'
            ttf.close()
    
    def add_to_brain(self,msg, chain_length, write_to_file=False):
        if write_to_file:
            f = open(self.training_text, 'a')
            f.write(msg + '\n')
            f.close()
        buf = [self.STOP_WORD] * chain_length
        for word in msg.split():
            self.markov[tuple(buf)].append(word)
            del buf[0]
            buf.append(word)
            self.markov[tuple(buf)].append(self.STOP_WORD)
            
    def generate_sentence(self,msg, chain_length, max_words=10000):
        buf = msg.split()[:chain_length]
        if len(msg.split()) > chain_length:
            message = buf[:]
        else:
            message = []
            for i in xrange(chain_length):
                message.append(random.choice(self.markov[random.choice(self.markov.keys())]))
        for i in xrange(max_words):
            try:
                next_word = random.choice(self.markov[tuple(buf)])
            except IndexError:
                continue
            if next_word == self.STOP_WORD:
                break
            message.append(next_word)
            del buf[0]
            buf.append(next_word)
        return ' '.join(message)
            
    
    

        