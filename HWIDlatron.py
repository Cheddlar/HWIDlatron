import uuid
import pyperclip
import time

def get_hwid():
    print("""
 ██╗  ██╗██╗    ██╗██╗██████╗ ██╗      █████╗ ████████╗██████╗  ██████╗ ███╗   ██╗
 ██║  ██║██║    ██║██║██╔══██╗██║     ██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
 ███████║██║ █╗ ██║██║██║  ██║██║     ███████║   ██║   ██████╔╝██║   ██║██╔██╗ ██║
 ██╔══██║██║███╗██║██║██║  ██║██║     ██╔══██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║
 ██║  ██║╚███╔███╔╝██║██████╔╝███████╗██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║
 ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    """)
    hwid = uuid.getnode()
    print(f'HWID: {hwid} - This has been automatically copied to your clipboard.')
    pyperclip.copy(str(hwid))
    print("The program will auto-close in 5 minutes.")
    time.sleep(300)
    print("Auto-closing now.")

get_hwid()
