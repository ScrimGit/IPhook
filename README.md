# IP Hook

IP Hook is a simple Python script that sends your device's IP address and hostname to a specified Discord webhook URL on boot. This can be useful for keeping track of the IP addresses of remote devices, or for quickly checking the IP address of a device on your local network.

## Getting Started

These instructions will help you run the script on your local machine and set up the webhook URL.

### Prerequisites

- Python 3.6 or later
- Requests library (can be installed with pip)

### Installation

1. Clone this repository to your local machine.
2. Open the `iphook.py(iphook2.py)` file in your favorite text editor.
3. Replace `your-discord-webhook` on line 4 with the URL of the Discord webhook you want to send the IP address to.
4. Save the file.

### Usage

To use Captain IP Hook, simply run the script in a terminal or command prompt:

sudo python3 iphook.py (iphook2.py)

The script will send the device's IP address, hostname, and gateway address to the specified Discord webhook.

### Discord Webhook Setup

To set up a Discord webhook for Captain IP Hook, follow these steps:

1. In Discord, right-click on the server you want to add the webhook to and select **Server Settings**.
2. Click on **Integrations** in the sidebar.
3. Click on **Webhooks** and then **Create Webhook**.
4. Enter a name for the webhook and select the channel you want the messages to appear in.
5. Copy the webhook URL and paste it into the `webhookURL` variable in the `captain_ip_hook.py` file.

### Contributing

If you find any issues with the script or have suggestions for improvement, please feel free to open an issue or submit a pull request.

#### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
