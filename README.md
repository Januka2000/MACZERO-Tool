# MACZERO - MAC Address Changer

MACZERO is a Python script that allows you to change the MAC address of a network interface on a Linux system. This can be useful for enhancing privacy, security, and testing various network configurations.

## Features

- Easily change the MAC address of any network interface.
- Validate the MAC address format before applying the change.
- Ensure the script is executed with root privileges.
- Display the current MAC address before and after the change.

## Requirements

- Python 3.x
- Linux operating system (Tested on Kali Linux)

## Installation

1. **Clone the Repository**: First, clone this repository or download the script directly.

   ```bash
   git clone https://github.com/yourusername/maczero.git
   cd maczero
#Install Required Modules: Verify Python 3 is installed and update your system.
```bash
# Check the Python 3 version
python3 --version

# Update the package list
sudo apt-get update

# Install Python 3 if not already installed
sudo apt-get install python3
```

#Usage
To change the MAC address of a network interface, use the following command:
```bash
sudo python3 maczero.py -i <interface> -m <new_mac_address>
```
Example
```bash
sudo python3 maczero.py -i eth0 -m 00:11:22:33:44:55
```
#Options
-i, --interface: Specify the network interface whose MAC address you want to change.
-m, --mac: Provide the new MAC address you want to assign.
Help
To see a brief overview of the available options, run:

```bash
python3 maczero.py --help
```

#Example Output
```bash
 __  __    _____  ______ _____  ______  _____  
|  \/  |  / ____|/      / ____||  ____|/  __  \ 
| \  / | | |__  |  (| | |__  |  |___ | |__) |  
| |\/| |  \__ \ |  | |  \__ \|   __|  |   _/    
| |  | |  |___) |  |_| |  __) |  |    |  |   
|_|  |_| |_____/ \___  \_____/|  |    |  |   

Current MAC: 00:1A:2B:3C:4D:5E
[+] Successfully changed MAC Address of eth0 to 00:11:22:33:44:55

```
