# Author: Kelvin Gooding
# Created: 2023-05-26
# Updated: 2024-03-07
# Version: 1.1

# Ansible

if dpkg -s ansible &> /dev/null; then
        echo
        echo "-----| Ansible |-----"
        ansible --version | head -1
else
        echo "-----| Ansible |-----"
        echo "Ansible is not installed"
fi

# Python3

if dpkg -s python3 &> /dev/null; then
        echo
        echo "-----| Python3 |-----"
        python3 --version
else
        echo
        echo "-----| Python3 |-----"
        echo "Python3 is not installed"
fi

# Docker

if dpkg -s docker &> /dev/null; then
        echo
        echo "-----| Docker |-----"
        docker --version
else
        echo
        echo "-----| Docker |-----"
        echo "Docker is not installed"
fi

# MariaDB

if dpkg -s mariadb &> /dev/null; then
        echo
        echo "-----| MariaDB |-----"
        mariadb --version
else
        echo
        echo "-----| MariaDB |-----"
        echo "MariaDB is not installed"
fi

# Git

if dpkg -s git &> /dev/null; then
        echo
        echo "-----| Git |-----"
        git --version
else
        echo
        echo "-----| Git |-----"
        echo "Git is not installed"
fi

# PIP

if dpkg -s pip &> /dev/null; then
        echo
        echo "-----| PIP |-----"
        pip --version
else
        echo
        echo "-----| PIP |-----"
        echo "PIP is not installed"
fi

echo
