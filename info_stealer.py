import os
import json
import platform
import socket
import uuid
import requests
import pyperclip
import hashlib
from base64 import b64encode, b64decode

# Global variable to store collected data
collected_data = {
    "browser_passwords": [],
    "clipboard_data": "",
    "system_info": {}
}

def simple_encryption_simulation(password, key):
    """
    Simple simulation of encryption for educational purposes
    """
    # This is not real encryption - just for demonstration
    return f"decrypted_{password}"

def extract_browser_passwords():
    """
    Simulates extracting browser passwords
    """
    print("[*] Simulating browser password extraction")
    
    # Simulated database entries
    simulated_passwords = [
    	("http://testphp.vulnweb.com/login.php","admin","admin")
        ("https://example.com", "test_user", "encrypted_password_1"),
        ("https://test-site.com", "demo_user", "encrypted_password_2")
    ]
    
    for url, username, password in simulated_passwords:
        decrypted_password = simple_encryption_simulation(password, "simulated_key")
        collected_data["browser_passwords"].append({
            "url": url,
            "username": username,
            "password": decrypted_password
        })
    
    print(f"[+] Retrieved {len(simulated_passwords)} simulated passwords")

def capture_clipboard_data():
    """
    Captures current clipboard content
    """
    print("[*] Capturing clipboard data")
    try:
        clipboard_text = pyperclip.paste()
        collected_data["clipboard_data"] = clipboard_text
        print(f"[+] Clipboard data captured: {clipboard_text[:50]}...")
    except Exception as e:
        print(f"[-] Error capturing clipboard: {e}")
        collected_data["clipboard_data"] = "Error capturing clipboard"

def gather_system_info():
    """
    Gathers system information
    """
    print("[*] Gathering system information")
    
    try:
        # Get system details
        system_info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.architecture()[0],
            "hostname": socket.gethostname(),
            "private_ip": socket.gethostbyname(socket.gethostname()),
            "mac_address": ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                                   for elements in range(0, 8*6, 8)][::-1])
        }
        
        # Get public IP (with error handling)
        try:
            public_ip = requests.get('https://api.ipify.org', timeout=5).text
            system_info["public_ip"] = public_ip
        except:
            system_info["public_ip"] = "Unable to retrieve"
        
        collected_data["system_info"] = system_info
        print("[+] System information gathered successfully")
        
    except Exception as e:
        print(f"[-] Error gathering system info: {e}")

def display_results():
    """
    Displays the collected information
    """
    print("\n" + "="*50)
    print("INFORMATION STEALER  RESULTS")
    print("="*50)
    
    print("\n1. BROWSER PASSWORDS (SIMULATED):")
    if collected_data["browser_passwords"]:
        for i, entry in enumerate(collected_data["browser_passwords"], 1):
            print(f"   {i}. URL: {entry['url']}")
            print(f"      Username: {entry['username']}")
            print(f"      Password: {entry['password']}")
    else:
        print("   No passwords retrieved")
    
    print("\n2. CLIPBOARD DATA:")
    print(f"   Content: {collected_data['clipboard_data']}")
    
    print("\n3. SYSTEM INFORMATION:")
    for key, value in collected_data["system_info"].items():
        print(f"   {key.replace('_', ' ').title()}: {value}")

def main():
    """
    Main function to run the information stealer simulation
    """
    print("Information Stealer ")
    print("="*60)
    
    # Run all collection functions
    extract_browser_passwords()
    capture_clipboard_data()
    gather_system_info()
    
    # Display results
    display_results()
    
    print("\n" + "="*60)
    print("SIMULATION COMPLETE")
    print("This demonstration shows how information stealers work.")
    print("Always practice ethical hacking with proper authorization.")
    print("="*60)

if __name__ == "__main__":
    main()
