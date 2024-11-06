#
# Copyright (c) 2024  Cenk Sasmaztin <cenk@oxoonetworks.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
# PURPOSE of this SCRIPT

# This code connects to a network device and retrieves the current working configuration.
#Then detects the changes made, creates a report with the change lines,
#and also backs up the new version of the configuration.
#
#
# This script requires the following variables to be defined:
# 
#

#Command examples
#python3 backup_report.py -i 192.168.1.250 -u admin -p 1qaz2wsx -c "show running-config"


#Examples
#For HP Comware Switch:
#Command: display current-configuration
#Copy code
#python backup_report.py -i 192.168.1.251 -u admin -p password123 -c "display current-configuration"

#For Cisco Switch:
#Command: show running-config
#Copy code
#python backup_report.py -i 192.168.1.252 -u admin -p password123 -c "show running-config"

#Aruba CX Switch:
#Command: show running-configuration

#Copy code
#python backup_report.py -i 192.168.1.253 -u admin -p password123 -c "show running-configuration"

# importing necessary modules

#import paramiko
#import time
#import os
#import argparse
#from datetime import datetime
#import difflib
#import re

he backup_report.py file includes the following Python libraries:

	1.	paramiko - for SSH connections.
	2.	argparse - for command-line argument parsing.
	3.	datetime - for handling date and time.
	4.	difflib - for comparing configurations.
	5.	re - for regular expressions.

The command to install the necessary libraries on a Linux environment without a virtual environment is:
sudo apt install python3-paramiko
The other libraries (argparse, datetime, difflib, re) are part of the Python standard library and do not require additional installation. Make sure Python 3 is installed for compatibility. ￼

