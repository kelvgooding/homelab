# Author: Kelvin Gooding
# Created: 2023-10-15
# Updated: 2024-03-07
# Version: 1.2

echo "-----| $(hostname) - Network Info |-----"
echo
echo IP Address: $(hostname -I | cut -d ' ' -f 1)
echo Subnet Mask: $(ifconfig | grep -A 1 "$(route | grep '^default' | grep -o '[^ ]*$')" | grep -o 'netmask [^ ]*' | cut -c 9-25)
echo MAC Address: $(hostname -I | cut -d ' ' -f 3)
echo Network Gateway: $(hostname -I | cut -d ' ' -f 2)
echo DNS: $(grep '^nameserver' /etc/resolv.conf | cut -c 12-25)
echo