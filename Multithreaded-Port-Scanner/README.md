

# 🛡️ Python Multithreaded Port Scanner

A high-performance **multithreaded TCP port scanner** built using **Python**, **socket programming**, and a **queue-based worker model**.  
Designed to efficiently scan large port ranges with proper synchronization and a clean, scalable architecture.

----------
## 📌 Features

-   ⚡ Multithreaded scanning using worker threads
    
-   🔒 Thread-safe port distribution using `queue.Queue`
    
-   🌐 TCP connect scan using `connect_ex()`
    
-   🧠 Banner grabbing for basic service identification
    
-   ⏱️ Timeout handling for faster scans
    
-   📝 Scan results saved to a log file
    
-   🧹 Clean, modular, and readable codebase
    
-   💻 Cross-platform support (Windows / Linux)
    

----------

## 🧠 How It Works (Architecture)

1.  All target ports are added to a **thread-safe queue**
    
2.  Multiple worker threads pull ports from the queue
    
3.  Each thread attempts a TCP connection to its assigned port
    
4.  If a port is open:
    
    -   The service banner is captured (if available)
        
    -   Results are printed and logged
        
5.  Threads exit gracefully when the queue becomes empty
    

This design avoids race conditions and scales efficiently.

----------

## 🚀 Usage

### Run the scanner

```bash
python port_scanner.py

```

### Example Input

```text
Enter Target IP: 127.0.0.1
Start Port: 1
End Port: 1024

```

----------

## 📂 Sample Output

```text
[+] Port 22 OPEN   | Banner: SSH-2.0-OpenSSH_8.9
[+] Port 80 OPEN   | Banner: HTTP/1.1 200 OK

```

Results are also saved to:

```text
scan_results.txt

```

----------

## 🧩 Technologies Used

-   Python 3
    
-   socket
    
-   threading
    
-   queue
    
-   TCP/IP networking
    

----------

## ⚠️ Legal Disclaimer

This tool is intended **for educational purposes only**.  
Scan only systems you own or have **explicit permission** to test.  
The author is not responsible for misuse or damage caused by this tool.


    
