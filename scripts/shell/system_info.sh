# Author: Kelv Gooding
# Created: 2023-04-11
# Updated: 2024-03-07
# Version: 1.5

echo "-----| $(hostname) - System Info |-----"
echo
echo -n "Hostname:              "; hostname
echo -n "System Boot:           "; uptime -s
echo -n "System Uptime:         "; uptime -p
echo -n "OS Version:            "; uname -s
echo -n "OS Distribution:       "; lsb_release -d | cut -c 14-
echo -n "OS Kernel Version:     "; uname -r
echo -n "OS Shell:              $SHELL"
echo
