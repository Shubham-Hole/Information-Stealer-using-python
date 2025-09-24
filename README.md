# Information-Stealer-using-python
A safe Python demo showing how info-stealing attacks work conceptually, using synthetic data for system info, clipboard, and browser data in a controlled lab.
# Overview
Project Overview:
This Python script performs the following malicious tasks:

1. Extracts Saved Browser Passwords:
 Retrieves stored credentials from Google Chrome.
 Decrypts saved passwords using system encryption keys.

2. Captures Clipboard Data:
 Reads and stores the latest copied text.
 Can include sensitive data like passwords and credit card numbers.

3. Steals System Information:
 Gathers OS details, IP address, MAC address, hostname, and processor information.
 Retrieves public IP using an external API.
