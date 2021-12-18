import subprocess
def monitermode_mac(interface,new_mac):
    print("changing mac "+interface+" new_mac "+new_mac)
    subprocess.call(f"ifconfig {interface} down",shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}",shell=True)
    subprocess.call(f"ifconfig {interface} up",shell=True)
    subprocess.call(f"ifconfig {interface}",shell=True)

def netmac(interface):
    print("changing mac ",interface )
    subprocess.call(f"ifconfig {interface} down",shell=True)
    subprocess.call(f"ifconfig {interface} hw ether 30:46:9a:74:50:27",shell=True)
    subprocess.call(f"ifconfig {interface} up",shell=True)
    subprocess.call(f"ifconfig {interface}",shell=True)
    #print("[*] checking networking")
    #subprocess.call(f"ifconfig ping google.com -c 5",shell=True)

def trying():
    print("eth0///wlan0")
    interface=str(input("input your interface:: "))
    print("\n[*]x for moniter mode\n[*]y for internet useage::")
    operations = input("select your operations:: ")
    results=0
    if operations == "x":
        new_mac=input("new_mac for monitermode__mac::")
        result = monitermode_mac(interface,new_mac)
    elif operations == "y":
        result = netmac(interface)
    else:
        exit()

neo=trying()
