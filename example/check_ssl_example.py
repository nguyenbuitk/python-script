import ssl
import socket
import pprint

hostname = 'www.example.com'
port = 443

# Create a standard socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
"""
SSL Context is collection of ciphers, protocol version, trusted certs, TLS optoins, ...
Since it is very common to have multiple connections with the same setting, they are
put together in a context an the relevant SSL connections are then create based on this context.
And to create a new connection, you need only refer to the context which thus saves time and memory
compare to the case you would have to re-create all of these settings
"""
context = ssl.create_default_context()

print("SSL Context Details: ")
print("======================")
print(f"ProtocoL: {context.protocol}")
print(f"Load verify location: {context.load_verify_locations}")
# print(f"Options: {context.options}")
# print(f"Verify Mode: {context.verify_mode}")
# print(f"Check Hostname: {context.check_hostname}")
# print(f"CA Certificates: {context.get_ca_certs()}")
# print(f"Cipher suites: {context.get_ciphers()}")


ssl_sock = context.wrap_socket(sock, server_hostname=hostname)

ssl_sock.connect((hostname, port))



print(f"Connected to {hostname} on port {port}")
print("SSL/TLS version: ", ssl_sock.version())
print("Cipher used: ", ssl_sock.cipher())
print("Server certificate: ")
pprint.pprint(ssl_sock.getpeercert())



ssl_sock.close()
