'''
Created on 29/dic/2011

@author: remix_tj
'''

import time 
import sys
from HandleMsg import Handlemsg
if __name__ == "__main__":
        hm = Handlemsg()
        if len(sys.argv)>2 and sys.argv[1]=="learnfrom":
            hm.learnFrom(sys.argv[2])
        else:    
            while True:
                time.sleep(15)
                hm.parseFriendsMsg()
    
    
