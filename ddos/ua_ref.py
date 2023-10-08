#############################################################
# FDos - Create Random User Agent and Referer.              #
#############################################################

import random

def user_agent() -> str:
    return random.choice(open('lib/ua.txt', 'r').read().splitlines())
    
def referer() -> str:
    return random.choice(open('lib/referer.txt', 'r').read().splitlines())
