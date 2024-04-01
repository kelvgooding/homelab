# Kelvin Gooding
# 27/03/2024
# 1.0

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
echo "#############################################"
echo "########## Step 2: Files & Scripts ##########"
echo "#############################################"
echo
echo "2.1 - The following directories and files need to be added to /home/`whoami`. This can be done via WinSCP."
echo
echo "- config.ini"
echo "- scripts/python"
echo "- scripts/shell"
echo
while true; do
    echo -n "- Have the directories and files been added to the server (y / n): "
    read choice

    if [ "$choice" = "y" ]; then
        break
    else
        echo "Invalid input. Please press y once this has been done"
    fi
done
echo
echo "####################################"
echo "########## Step 3: GitHub ##########"
echo "####################################"
echo
echo -n "3.1 - "
ssh-keygen -t rsa -b 4096
echo
echo "- Key has been generated:"
echo
cat ~/.ssh/id_rsa.pub
echo
while true; do
    echo -n "3.2 - This key needs to be added to GitHub. Has this been done? (y / n): "
    read choice

    if [ "$choice" = "y" ]; then
        break
    else
        echo "Invalid input. Please press y once this has been done"
    fi
done
echo
echo -n "3.3 - Enter your full name: "
read full_name
git config --global user.name "$full_name"
echo -n "3.4 - Enter your Email Address: "
read email_address

echo
echo "##################################"
echo "########## Step 4: Apps ##########"
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
