import pyperclip
import time
import subprocess
import sys

def get_hwid():
    print("""
 ██╗  ██╗██╗    ██╗██╗██████╗ ██╗      █████╗ ████████╗██████╗  ██████╗ ███╗   ██╗
 ██║  ██║██║    ██║██║██╔══██╗██║     ██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
 ███████║██║ █╗ ██║██║██║  ██║██║     ███████║   ██║   ██████╔╝██║   ██║██╔██╗ ██║
 ██╔══██║██║███╗██║██║██║  ██║██║     ██╔══██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║
 ██║  ██║╚███╔███╔╝██║██████╔╝███████╗██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║
 ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    """)
    try:
        hwid_raw = subprocess.check_output("wmic csproduct get uuid", shell=True).decode('utf-8')
        hwid = hwid_raw.strip().split('\r\r\n')[1]
    except subprocess.CalledProcessError as e:
        print("Failed to get the machine's HWID.")
        time.sleep(10)
        sys.exit(1)
    print(f'HWID: {hwid} - This has been automatically copied to your clipboard.')
    pyperclip.copy(str(hwid))
    print("The program will auto-close in 5 minutes.")
    time.sleep(300)
    print("Auto-closing now.")

get_hwid()
