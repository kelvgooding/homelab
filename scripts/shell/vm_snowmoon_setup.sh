# Author: Kelvin Gooding
# Created: 2024-03-27
# Updated: 2024-03-27
# Version: 1.0

clear
echo "#######################################################"
echo "########## Step 1: Public / Private Keypairs ##########"
echo "#######################################################"
echo
echo "1.1 - Creating authorized_keys file within .ssh directory.."
mkdir /home/`whoami`/.ssh
cd /home/`whoami`/.ssh
touch authorized_keys
echo
echo "1.2 - Enter the homelab_public ssh key below:"
echo
read choice
echo "$choice" >> /home/`whoami`/.ssh/authorized_keys
echo
echo "- homelab_public ssh key has been added to /home/`whoami`/.ssh/authorized_keys sucessfully."
echo
echo "##################################"
echo "########## Step 2: Apps ##########"
echo "##################################"
echo
cd ~/apps
git clone git@github.com:kelvgooding/8ball-leaderboard.git
pip install -r ~/apps/8ball-leaderboard/requirements.txt
cd ..
git clone git@github.com:kelvgooding/contacts.git
pip install -r ~/apps/contacts/requirements.txt
cd ~
echo
echo "##############################"
echo "########## Complete ##########"
echo "##############################"
echo