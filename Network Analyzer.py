import scapy.all as scapy
from scapy.layers import http
from scapy.arch import windows as scapy_windows
import threading
import datetime
import platform  # Added for multi-platform support

# Author information
author_name = "Subhankar Senapati"
linkedin_profile = "linkedin.com/in/subhankar-senapati"
creation_date = datetime.datetime.now().strftime("%Y-%m-%d")

def get_interfaces():
    # Get a list of available network interfaces with names
    if platform.system() == "Windows":
        interfaces = scapy_windows.get_windows_if_list()
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # macOS
        interfaces = scapy.get_if_list()
    else:
        print("Unsupported operating system. Exiting.")
        exit()

    # Filter out virtual interfaces based on keywords
    excluded_keywords = ["VirtualBox", "Microsoft Wi-Fi Direct", "WAN Miniport"]
    real_interfaces = [(interface['name'], interface['description']) for interface in interfaces if all(keyword not in interface['description'] for keyword in excluded_keywords)]
    
    return real_interfaces

def select_interface(interfaces):
    # Display available interfaces and prompt the user to select one
    print("Available Real Hardware Interfaces:")
    for i, (name, description) in enumerate(interfaces, start=1):
        print(f"{i}. {name} - {description}")

    selection = input("Enter the number of the desired interface: ")
    try:
        selected_interface = interfaces[int(selection) - 1][0]
        return selected_interface
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        exit()

def get_output_filename():
    # Prompt the user for the desired output file name
    return input("Enter the output file name (include .pcap extension): ")

def process_packet(packet, output_file):
    # Process the packet here
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f"HTTP Request: {url}")

        login_info = get_login_info(packet)
        if login_info:
            print(f"Possible Username/Password: {login_info}")

    # Store the packet to the output file
    with open(output_file, 'ab') as file:
        scapy.wrpcap(file, packet, append=True)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load.decode('utf-8'):
                return load.decode('utf-8')

def capture_traffic(interface, output_file):
    # Use AsyncSniffer for asynchronous packet capture
    sniffer = scapy.AsyncSniffer(iface=interface, prn=lambda x: process_packet(x, output_file))
    sniffer.start()

    try:
        input("Press Enter to stop capturing...")
    except KeyboardInterrupt:
        pass
    finally:
        sniffer.stop()

if __name__ == "__main__":
    # Display author information
    print(f"Author: {author_name}")
    print(f"LinkedIn: {linkedin_profile}")
    print(f"Creation Date: {creation_date}")

    interfaces = get_interfaces()
    if not interfaces:
        print("No real hardware interfaces found. Exiting.")
        exit()

    selected_interface = select_interface(interfaces)
    output_filename = get_output_filename()

    # Use threading to capture traffic in a separate thread
    capture_thread = threading.Thread(target=capture_traffic, args=(selected_interface, output_filename))
    capture_thread.start()
    capture_thread.join()

    print("Traffic capture complete.")
