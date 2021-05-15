import subprocess as sb
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i" ,"--interface" ,dest="interface" ,help="Your device")
    parse_object.add_option("-m" ,"--mac" ,dest="mac_address" ,help="New mac address")

    return parse_object.parse_args()

def change_mac_address(user_interface ,user_mac_address):
    sb.call(["ifconfig" ,user_interface ,"down"])
    sb.call(["ifconfig" ,user_interface ,"hw" ,"ether" ,user_mac_address])
    sb.call(["ifconfig" ,user_interface ,"up"])

def new_mac_address(user_interface):
    ifconfig = sb.check_output(["ifconfig" ,user_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" ,str(ifconfig))
    
    if new_mac:
        return new_mac.group(0)

print("MaCChanger started!")

(user_inputs ,arguments) = get_user_input()
change_mac_address(user_inputs.interface,user_inputs.mac_address)

finallized_mac = new_mac_address(str(user_inputs.interface))

if finallized_mac == user_inputs.mac_address:
    print("Success!")
else:
    print("Error!")