import sys
import socket  #socket provide low level network communication functionality
from datetime import datetime

#define our target

if len(sys.argv) == 2 :
    
    Target = socket.gethostbyname(sys.argv[1]) # converting hostname to Ipv4

else:
    
    print("INVALID amount of arguments, ")
    print("Syntax: python3 scanner.py <ip>")

#ADD a pretty banner

print("_" * 50)

print("Scanning target: "+Target)

print("Time started: "+str(datetime.now()))

print("_" * 50)

try:
     for port in range(1,65536):
         s = socket.soccket(socket.AF_INET, socket.SOCK_STREAM)
         result = s.connect_ex((Target,port))
         if result == 0:
           print(f"Port {port} is open")
         s.close()
           
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit(1)

except socket.gaiierror:
    print("Hostname could not be") 
    sys.exit(1)

except socket.error:
    print("could not connect to server.")
    sys.exit(1)
    
   