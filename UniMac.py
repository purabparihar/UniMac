import subprocess   
import optparse     #importing parser for CLI options
import re    #importing regular expressions
from termcolor import colored   #terminal color

banner = ("""                        *


                                                                                        
 ____   ____  _____   ______    ____      ______  _______          ____         _____   
|    | |    ||\    \ |\     \  |    |    |      \/       \    ____|\   \    ___|\    \  
|    | |    | \\    \| \     \ |    |   /          /\     \  /    /\    \  /    /\    \ 
|    | |    |  \|    \  \     ||    |  /     /\   / /\     ||    |  |    ||    |  |    |
|    | |    |   |     \  |    ||    | /     /\ \_/ / /    /||    |__|    ||    |  |____|
|    | |    |   |      \ |    ||    ||     |  \|_|/ /    / ||    .--.    ||    |   ____ 
|    | |    |   |    |\ \|    ||    ||     |       |    |  ||    |  |    ||    |  |    |
|\___\_|____|   |____||\_____/||____||\____\       |____|  /|____|  |____||\ ___\/    /|
| |    |    |   |    |/ \|   |||    || |    |      |    | / |    |  |    || |   /____/ |
 \|____|____|   |____|   |___|/|____| \|____|      |____|/  |____|  |____| \|___|    | /
    \(   )/       \(       )/    \(      \(          )/       \(      )/     \( |____|/ 
     '   '         '       '      '       '          '         '      '       '   )/    
                                                                                  '     
Version 1.0
Developer: Purab Parihar
Linkedin: https://www.linkedin.com/in/purab-parihar-b28618188
Instagram: https://www.instagram.com/purabparihar
 """)
print(colored(banner, 'cyan'))


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="newmac", help="New Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please Specify the Interface, You can use --help for more info.")
    if not options.newmac:
        parser.error("[+] Please Specify the Interface, You can use --help for more info")
    return options


# Changing MAC address
def change_mac(interface, newmac):
    print("[+] Changing MAC Address for", interface, "to", newmac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
    subprocess.call(["ifconfig", interface, "up"])

    
# Fetching current MAC address
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_verified = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_verified:
        return(mac_verified.group(0))
    else:
        print("[-] Could not Read MAC Address from Interface")

options = get_arguments()
current_mac=get_current_mac(options.interface)
print("Current Mac =",current_mac)

change_mac(options.interface,options.newmac)

current_mac=get_current_mac(options.interface)
if current_mac== options.newmac:
    print("[+] MAC Address is succusfully changed to >> ",current_mac)
