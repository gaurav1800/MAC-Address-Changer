#!/usr/bin/env python

# allows execution of system commands
import subprocess

# allows input arguments from user and parse them to be used in code
import optparse

# allows the use of regular expressions
import re

def get_arguments():
    # Create an instance that can handle user input using arguments
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address of")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    argument_values, arguments = parser.parse_args()
    if not argument_values.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not argument_values.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
    return argument_values


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for: " + interface + " into " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


argument_values = get_arguments()
# change_mac(argument_values.interface, argument_values.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", argument_values.interface])
print(ifconfig_result)

mac_address_search_result = re.search(rb"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
print(mac_address_search_result.group(0))


# To run in terminal, execute the following:
# python3 mac_changer.py --interface <interface> --mac <new MAC address>

