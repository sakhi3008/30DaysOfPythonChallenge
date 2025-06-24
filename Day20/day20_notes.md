# 🗓️ Day 20 – Sockets and HTTP Requests

Today’s challenge introduced me to the **low-level working of web communication** using Python’s `socket` module. I learned how to manually send an HTTP request and retrieve webpage content using TCP sockets — a foundational concept behind the internet!

---

## 🧠 Topics Covered

### 🔹 What are Sockets?
A **socket** is one endpoint of a two-way communication channel between two programs running on a network.

- It allows programs to communicate over the internet or local network.
- Python’s `socket` module provides access to the **BSD socket interface** for network communication.
- Two primary types:  
  - `SOCK_STREAM` (TCP): Reliable, connection-based.  
  - `SOCK_DGRAM` (UDP): Unreliable, connectionless.

💡 In this challenge, I used `SOCK_STREAM` (i.e., TCP) to create a connection between the client and the web server.

## ✅ Commonly Used socket Functions & Methods
| Function / Method           | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| `socket()`                  | Creates a new socket object.                                          |
| `connect((host, port))`     | Connects to a remote server.                                          |
| `bind((host, port))`        | Binds the socket to an address and port (used in servers).            |
| `listen()`                  | Puts the socket into server mode and waits for incoming connections.  |
| `accept()`                  | Accepts an incoming connection (used with servers).                   |
| `send(data)` or `sendall()` | Sends data through the socket. `sendall()` sends all data completely. |
| `recv(bufsize)`             | Receives data from the socket. `bufsize` is how much data to receive. |
| `close()`                   | Closes the socket connection.                                         |
| `settimeout()`              | Sets a timeout for blocking socket operations.                        |
| `gethostname()`             | Returns the current hostname.                                         |
| `gethostbyname(hostname)`   | Returns the IP address for the given hostname.                        |


---

### 🔹 What is an HTTP Request?
**HTTP (HyperText Transfer Protocol)** is the foundation of data communication on the web.

- A **GET request** is used to retrieve information from a server.
- Basic structure of an HTTP GET request:

```
GET / HTTP/1.1
Host: example.org
Connection: close
```

- The headers specify the **path**, the **HTTP version**, the **host** we're contacting, and that we want to **close the connection** after receiving the response.

---

### 🔹 Steps Performed in the Challenge

✅ Defined the **host and port** (default HTTP port is `80`)  
✅ Created a **TCP socket** using `socket.socket()`  
✅ Connected to the server using `connect()`  
✅ Constructed a **manual HTTP GET request**  
✅ Sent the request using `sendall()`  
✅ Received the raw **HTTP response**  
✅ Parsed the response to extract and print only the HTML content  
✅ Closed the socket to release resources  

---

## 🎯 Challenge – Fetch and Display a Webpage’s Content

In this challenge, I built a simple HTTP client using sockets that:

- Connected to `example.org`
- Manually sent an HTTP GET request
- Printed the raw HTML content of the homepage

---

## 💡 Key Learnings

- Sockets provide the **lowest level of network communication**.
- HTTP requests can be manually constructed and sent via sockets.
- Real-world web browsers internally use sockets to fetch and render web pages.
- Understanding socket communication helps in:
  - Building custom networking tools  
  - Learning how APIs and browsers function under the hood  
  - Preparing for real-time applications (like chat servers, multiplayer games, etc.)

---

This challenge helped me demystify how browsers and servers communicate and made me appreciate the underlying mechanics of the internet 🌐.
