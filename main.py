import socket
import os
import requests

webhookURL = 'https://discord.com/api/webhooks/942477543959822366/MKgU8xRNSCMBPIy4S7lqXZZQcNwO_HV4a2VikNxMNejTokg1>'
gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()
print ("IP:", ipaddr, " GW:", gateway, " Host:", host)

data = {
    'username': 'Silent IP Bot',
    'embeds': [{
        'color': 3066993,
        'title': 'Silence is up!',
        'description': '**hostname: **' + host + '\n' + '**IP: **' + ipaddr + '\n' + '**Gateway: **' + gateway,
    }]
}


result = requests.post(webhookURL, json = data)

try:
    result.raise_for_status()
except:
    pass