# IP-Hook

## What is IP-Hook
IP-Hook is a small service written in python to send your IP-Adress on boot to a Discord webhook
(Maybe even more webhooks?), I made this little service for a raspberry pi without a display, Since I needed the IP-Adress on boot for SSHing into it. Now this should work on any Debian based system like Raspbian.

## Setting up IP-Hook

Step 1: Cloning the Git Repository:
  ````bash
git clone https://github.com/ScrimGit/IPhook
````
<br/>

Step 2: Configuring The Webhook URL,
Navigate to the directory you installed IPHook in and use a text editor like NANO to edit the iphook,py file located like this /*Your Path*/IPhook/iphook.py

<br/>

Step 3: Create the IP-Hook Service
````bash
sudo systemctl --force --full edit IPhook.service
````
<br/>

This wil open the editor where you have to paste these contents with your own paths
Here are the Default contents to paste in and edit with your own paths
```bash
[Unit]
Description=IPhook **Hooked, matey!
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/IPhook/iphook.py

[Install]
WantedBy=multi-user.target
```
<br/>

Step 3: Enable and check the Service:
   ````bash
sudo systemctl enable IPhook.service
sudo systemctl status IPhook.service
````
<br/>

Notes: 
1. Remember to change the webhook url in iphook.py to your own webhook URL!
2. Remember to change the path to the iphook.py file in the iphook service!
3. Tested with a Discord webhook maybe different webhooks work like Slack, telegram etc.
