# Import specific modules regarding nmap
# Please download python-nmap
import nmap 

# Identify the scan target
target_address = input("Input your IP address: ")

# Ports to scan
port_start = 1
port_end = 1000

# Create scanner object
scanner = nmap.PortScanner()

print("Scanning {0}".format(target_address))

# Loop through start and end
for port in range(port_start, port_end + 1):
    try:
        result = scanner.scan(target_address, str(port))
        port_status = result['scan'][target_address]['tcp'][port]['state']
        print("\t Port: {0} is {1}".format(port, port_status))
    except KeyError as e:
        print(f"Error accessing data for port {port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
