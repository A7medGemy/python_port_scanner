from socket import socket, AF_INET, SOCK_STREAM


def scan_port(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))
    s.close()
    return result == 0


def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        result = scan_port(ip, port)
        if result:
            print(f"the port {port} is open")
        else:
            print(f"the port {port} is closed")


def main():
    check = input("what would you like to scan : port or ports: ").lower()
    if check == "port":
        try:
            ip = input("Enter your ip address: ")
            port = int(input("Enter the port you want to scan: "))
            if 0 <= port <= 65535:
                if scan_port(ip, port):
                    print(f"the port {port} is opened")
                else:
                    print(f"the port {port} is closed")
            else:
                print("The port must be between 0 and 65535")
        except ValueError:
            print("Enter a port number")



    elif check == "ports":
        ip = input("Enter your ip address: ")

        try:
            start = int(input("Enter the start port: "))
            end = int(input("Enter the end port: "))
            if 0 < start < end < 65535:

                scan_ports(ip, start, end)

            else:
                print("The scope of ports is (0, 65535) and the start port must be lower than the end one")
        except ValueError:
            print("Enter a valid num port")
    else:
        print("there is something went wrong!")


if __name__ == "__main__":
    main()
# ip = input("Enter IP Address: ")
# startPort = int(input("Enter your start port: "))
# endPort = int(input("Enter your end port: "))
#
# for port in range(startPort, endPort + 1):
#     s = socket(AF_INET, SOCK_STREAM)
#     result = s.connect_ex((ip, port))
#     if result == 0:
#         print("port " + str(port) + " is open")
#     else:
#         print("port " + str(port) + " is closed")
#     s.close()
