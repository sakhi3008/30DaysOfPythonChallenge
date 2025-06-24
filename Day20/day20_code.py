# Fetch and display a webpage’s content
import socket

# Define the host and port
host = "example.org"
port = 80  # Default HTTP port

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))
print(f" Connected to {host} on port {port}")

# Prepare the HTTP GET request
request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

# Send the request
client_socket.sendall(request.encode())
# Receive and display the response
response = b""
while True:
    data = client_socket.recv(4096)
    if not data:
        break
    response += data

# Close the connection
client_socket.close()

# Decode and print only the HTML content (omit headers)
html_start = response.find(b"\r\n\r\n") + 4  # skip HTTP headers
html_content = response[html_start:].decode(errors='ignore')

print("📄 Webpage Content:\n")
print(html_content)


