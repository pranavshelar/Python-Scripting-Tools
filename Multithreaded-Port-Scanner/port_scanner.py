import socket
import threading
import queue
import sys
from datetime import datetime


NUM_THREADS = 100
TIMEOUT = 1
LOG_FILE = "scan_results.txt"


port_queue = queue.Queue()
open_ports = []

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return None


def scan_port(ip):
    while not port_queue.empty():
        port = port_queue.get()

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)

            result = sock.connect_ex((ip, port))
            if result == 0:
                banner = grab_banner(ip, port)
                open_ports.append((port, banner))
                print(f"[+] Port {port} OPEN", end="")
                if banner:
                    print(f"   | Banner: {banner[:50]}")
                else:
                    print("N/A")

            sock.close()

        except Exception as e:
            pass

        finally:
            port_queue.task_done()


def start_scan(ip, start_port, end_port):
    print(f"\n Starting Scan on {ip}")
    print(f"Scanning ports {start_port} to {end_port} using {NUM_THREADS} threads...")
    print("-" * 50)

    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=scan_port, args=(ip,))
        thread.daemon = True
        thread.start()

    port_queue.join()

    print("\n Scan Complete!")
    print("-" * 50)

    if open_ports:
        print(" Open Ports Found:")
        for port, banner in open_ports:
            print(f"Port {port} | Banner: {banner}")
    else:
        print("No open ports detected.")

    save_results(ip)


def save_results(ip):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n\nScan Report for {ip} | {datetime.now()}\n")
        f.write("-" * 50 + "\n")

        if open_ports:
            for port, banner in open_ports:
                f.write(f"Port {port} OPEN | Banner: {banner}\n")
        else:
            f.write("No open ports found.\n")

    print(f"\nResults saved to {LOG_FILE}")




target = input("\nEnter Target IP: ").strip()
start = int(input("Start Port: "))
end = int(input("End Port: "))

try:
    target=socket.gethostbyname(target)
except:
    print("No Hostname Found")
    sys.exit()


start_scan(target, start, end)

