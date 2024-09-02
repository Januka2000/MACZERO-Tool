#!/usr/bin/python3

import subprocess
import optparse
import re
import sys
import os

# Welcome screen banner
welcome_screen = r"""
 __  __    _____  ______ _____  ______  _____  
|  \/  |  / ____|/      / ____||  ____|/  __  \ 
| \  / | | |__  |  (| | |__  |  |___ | |__) |  
| |\/| |  \__ \ |  | |  \__ \|   __|  |   _/    
| |  | |  |___) |  |_| |  __) |  |    |  |   
|_|  |_| |_____/ \___  \_____/|  |    |  |   
"""

print(welcome_screen)

# Function to change the MAC address of an interface
def change_mac_address(interface, new_mac):
    try:
        # Bring down the network interface
        subprocess.run(["ifconfig", interface, "down"], check=True)
        # Set the new MAC address
        subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], check=True)
        # Bring the interface back up
        subprocess.run(["ifconfig", interface, "up"], check=True)
        print(f"[+] Successfully changed MAC Address of {interface} to {new_mac}")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error changing MAC address: {e}")
        sys.exit(1)

# Function to parse command-line arguments
def get_arguments():
    parser = optparse.OptionParser()
    # Add options for interface and new MAC address
    parser.add_option("-i", "--interface", dest="interface", help="Network interface to change the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Desired new MAC address")
    options, _ = parser.parse_args()

    # Check if the necessary arguments are provided
    if not options.interface:
        parser.error("[-] Interface not specified. Use --help for instructions.")
    if not options.new_mac:
        parser.error("[-] New MAC address not specified. Use --help for instructions.")

    return options

# Function to get the current MAC address of an interface
def get_current_mac(interface):
    try:
        # Retrieve interface configuration
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        # Use regex to extract the MAC address
        current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))

        if current_mac:
            return current_mac.group(0)
        else:
            print("[-] Could not retrieve MAC address.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[-] Error retrieving MAC address for {interface}: {e}")
        sys.exit(1)

# Function to validate the MAC address format
def validate_mac(mac):
    return bool(re.match(r"^(\w\w:){5}\w\w$", mac))

# Function to check if the script is run as root
def check_root():
    if os.geteuid() != 0:
        print("[-] Root privileges are required. Please run the script as root.")
        sys.exit(1)

# Function to check if the specified interface exists
def check_interface(interface):
    try:
        subprocess.check_output(["ifconfig", interface])
    except subprocess.CalledProcessError:
        print(f"[-] The interface {interface} does not exist.")
        sys.exit(1)

# Main program flow
if __name__ == "__main__":
    # Ensure the script is run as root
    check_root()

    # Get the user-provided arguments
    options = get_arguments()

    # Validate the MAC address format
    if not validate_mac(options.new_mac):
        print("[-] Invalid MAC address format. Example: 00:11:22:33:44:55")
        sys.exit(1)

    # Check if the specified network interface exists
    check_interface(options.interface)

    # Retrieve and display the current MAC address
    current_mac = get_current_mac(options.interface)
    print(f"Current MAC: {current_mac}")

    # Change the MAC address
    change_mac_address(options.interface, options.new_mac)

    # Retrieve and display the MAC address after the change
    final_mac = get_current_mac(options.interface)

    # Verify if the MAC address was successfully changed
    if final_mac == options.new_mac:
        print(f"[+] MAC address successfully changed to {final_mac}")
    else:
        print("[-] MAC address change failed. Please verify the MAC address format.")
