> NOTE: Ensure that Java is installed on the nodes.

## General

By default, Jenkins stores all of its data in this directory on the file system /var/jenkins_home

## Security: Users

Navigate to Manage Jenkins

Under Security, click Users

Click + Create User

Complete the form with the following details:

- Username
- Password
- Confirm password
- Full name
- E-mail address

Click Create User once the details have been entered.

## System Configuration: System

Navigate to Manage Jenkins

Under System Configuration, Click System

Under Jenkins location, fill in the following input boxes:

Complete the form with the following details:

- System Admin e-mail address

Untick "Help make Jenkins better by sending annoymous usage statistics and crash reports to the Jenkins project.

Click Save once the details have been entered.

## System Configuration: Nodes

Navigate to Manage Jenkins

Under System Configuration, Click Nodes

Click + New Node

### Form 1 - New Node

Complete the form with the below details:

- Node name

Select Type: Permanent Agent

Click Create one these details have been entered.

### Form 2

Complete the form with the below details:

- Name: Server Name
- Description: Server Name | OS
- Number of executors: 1
- Remote root directory: /home/kgooding/homelab/jenkins
- Usage: Use this node as much as possible
- Launch method: Launch agents via SSH
- Enter IP address
- Credentials: Add Jenkins

> Note: the Remote root directory will generate folders and directories

### Form 3

Complete the form with the below details:

- Domain: Global Credneitlas (Unrestricted)
- Kind: Username with passwowrd
- Scopre: Global (Jenkins, nodes, items all child items, etc)
- Username: 
- Password: 
- ID: hostname

Once back on Form 2, select the newly created user credentials in the credentials dropdown.

