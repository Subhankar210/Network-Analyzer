# Network Traffic Analyzer

This Python script uses Scapy to capture and analyze network traffic. It can extract information from HTTP packets, including requested URLs and potential username/password information.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)

## Usage

1. Run the script by executing the following command:

   ```bash
   python network_traffic_analyzer.py
    Select a network interface from the displayed list.
    Enter the desired output file name when prompted.

The script will capture network traffic, analyze HTTP requests, and store the captured packets in a PCAP file.
Features

    Dynamically select a network interface.
    Prompt user for the output file name.
    Analyze HTTP requests and extract URLs.
    Identify potential username/password information in HTTP packets.
    Store captured packets in a PCAP file for further analysis.

Important Notes

    Ensure you have Python 3.x installed.
    Install the required Scapy library using pip install scapy.
    Use this tool responsibly and comply with legal and ethical considerations.

Disclaimer

This script is for educational purposes only. Use it responsibly and ensure compliance with applicable laws and policies.
Author

Subhankar Senapati
License

This project is licensed under the MIT License - see the LICENSE.md file for details
