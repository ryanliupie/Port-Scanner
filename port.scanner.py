# Creator: Ryan Liu
# 03/18/2025

import socket # works with networking and protocols 
import sys # helps control and change python environment such as handling exceptions
from concurrent.futures import ThreadPoolExecutor # concurrent.futures module includes the ThreadPoolExector class which is used to manage multiple threads  

target_ip = str(input("Enter an IP Address: "))

def scan_port(port): # parameter
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET specifies that an IPV4 will be used. SOCK_STREAM specifies that a TCP connection with be used to establish communication.
        socket.setdefaulttimeout(0.5) # amount of time before moving onto the next port

        result = s.connect_ex((target_ip, port)) # attempts connection to ip address and port number
        if result == 0: # if result == 0, then the port is open
            print(f" Port {port} is open")
        s.close() # whether success or fail, important to close the network endpoint (socket(combination of an ip address and port number))

    except KeyboardInterrupt: 
        print("User stopped the program")
        sys.exit()

    except socket.error:
        print("Unresponsive host")
        sys.exit()
    

print(f" Scanning {target_ip}...")
with ThreadPoolExecutor(max_workers = 100) as executor: # this creates a thread pool of 100 threads. For example, having 100 workers scanning different ports simultaneously. The with statement makes sure the threads are properly closed after execution.
    executor.map(scan_port, range(1, 1025)) # executor.map runs the scan_port function where we can pass in an argument from 1 to 1025 ports