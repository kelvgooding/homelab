> NOTE: Ensure that Java is installed on the nodes.

## General

By default, Jenkins stores all of its data in this directory on the file system /var/jenkins_home

## Manage Jenkins - Users

Navigate to Manage Jenkins - Create User

Complete the form

- Username
- Password
- Confirm password
- Full name
- E-mail address

Click Create User once the details have been entered.

## Manage Jenkins - System

Navigate to Manage Jenkins > System

Under Jenkins location, fill in the following input boxes:

- Update System Admin e-mail address

Click Save once the details have been entered.

## Manage Jenkins - Nodes

Navigate to Manage Jenkins > Nodes

** Form 1 **

Complete the form with the below details:

- Node name

Under Type, enable Permanet Agent

Click Create one these details have been entered.

** Form 2 **

Complete the form with the below details:

- Description
- Number of executors: 1
- Remote root directory: /home/kgooding/homelab/jenkins
- Usage: Use this node as much as possible
- Launch method: Launch agents via SSH

- Enter IP address
- Credentials: Add Jenkins

> Note: the Remote root directory will generate folders and directories

** Form 3 **

Complete the form with the below details:

- Domain: Global Credneitlas (Unrestricted)
- Kind: Username with passwowrd
- Scopre: Global (Jenkins, nodes, items all child items, etc)
- Username: 
- Password: 
- ID: hostname

Once back on Form 2, select the newly created user credentials in the credentials dropdown.

