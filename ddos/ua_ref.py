#############################################################
# FDos - Create Random User Agent and Referer.              #
#############################################################

import requests
import random

def user_agent() -> str:
    useragent = []
    if useragent:
        pass
    else:
        req = requests.get("https://gist.githubusercontent.com/fooster1337/d526ba3f963d8e8c9372a9e77486aa05/raw/f4782156809d4c960225fa7375b659e052d0e106/user-agent.txt").text.splitlines()
        useragent.extend(req)
    return random.choice(useragent)
    
def referer() -> str:
    referer_page = []
    if referer_page:
        pass
    else:
        req = requests.get('https://gist.githubusercontent.com/fooster1337/f9f457e2d14683a5b0e1f259b68fce20/raw/cbf2a80c76d85963a54df911153ec45ff4891652/referer.txt').text.splitlines()
        referer_page.extend(req)
    return random.choice(referer_page)