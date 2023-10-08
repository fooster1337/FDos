#############################################################
# FDos - Create Random User Agent and Referer.              #
#############################################################

import random

def user_agent() -> str:
    return random.choice(open('ddos/lib/ua.txt', 'r').read().splitlines())
    
def referer() -> str:
    return random.choice(open('ddos/lib/referer.txt', 'r').read().splitlines())
