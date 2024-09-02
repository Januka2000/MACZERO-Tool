# MACZERO - MAC Address Changer

MACZERO is a Python script that allows you to change the MAC address of a network interface on a Linux system. This can be useful for various privacy, security, and testing purposes.

## Features

- Change the MAC address of any network interface.
- Validate the format of the MAC address before applying the change.
- Check if the script is run with root privileges.
- Display the current MAC address before and after the change.

## Requirements

- Python 3.x
- Linux operating system (Tested on Kali Linux)

## Installation

1. **Clone the Repository**: First, clone this repository or download the script directly.

   ```bash
   git clone https://github.com/yourusername/maczero.git
   cd maczero


#Install Required Modules

python3 --version

sudo apt-get update
sudo apt-get install python3

#Usage

sudo python3 maczero.py -i <interface> -m <new_mac_address>

Example:
sudo python3 maczero.py -i eth0 -m 00:11:22:33:44:55

Options:

-i, --interface: Specify the network interface whose MAC address you want to change.
-m, --mac: Provide the new MAC address you want to assign.

Help: You can get a brief overview of the available options by running:
python3 maczero.py --help


#Example
$ sudo python3 maczero.py -i eth0 -m 00:11:22:33:44:55


output
 __  __    _____  ______ _____  ______  _____  
|  \/  |  / ____|/      / ____||  ____|/  __  \ 
| \  / | | |__  |  (| | |__  |  |___ | |__) |  
| |\/| |  \__ \ |  | |  \__ \|   __|  |   _/    
| |  | |  |___) |  |_| |  __) |  |    |  |   
|_|  |_| |_____/ \___  \_____/|  |    |  |   

Current MAC: 00:1A:2B:3C:4D:5E
[+] Successfully changed MAC Address of eth0 to 00:11:22:33:44:55

