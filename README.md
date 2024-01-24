Network Traffic Analyzer
Overview

This tool is a multi-platform network traffic analyzer designed to capture and analyze network packets. It supports Windows, Linux, and macOS platforms and can capture traffic from real hardware interfaces, excluding virtual interfaces.
Author Information

    Author: **Subhankar Senapati**
    LinkedIn: linkedin.com/in/subhankar-senapati
    Creation Date: 2024-01-24

Latest Update
Version 1.0.0

    Added multi-platform support (Windows, Linux, macOS).
    Improved interface filtering to exclude virtual interfaces.
    Enhanced user experience during packet capture.

Usage

    Run the Script:
        Execute the script using Python.

    bash

    python network_analyzer.py

    Select Interface:
        Choose a real hardware interface from the list displayed.

    Enter Output File Name:
        Provide a name for the output file, including the .pcap extension.

    Capture Traffic:
        The tool will start capturing network traffic in a separate thread.

    Interrupt Capture:
        Press Enter to stop capturing.
        For a graceful exit, the tool will ask for confirmation before stopping.

    Automatic Save:
        If interrupted twice, the captured traffic will be automatically saved to the specified output file.

Notes

    The tool uses the scapy library for packet capture and analysis.
    Ensure proper permissions for network packet capture on your system.

Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.
