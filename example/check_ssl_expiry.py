import ssl
import socket
from datetime import datetime

def get_ssl_expiry_date(hostname):
    """Get the SSL certificate's expiry date for the given hostname."""
    # Define the port for SSL
    port = 443

    # Create a default SSL context
    context = ssl.create_default_context()

    # Create a socket and wrap it with SSL
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # Get the certificate
            cert = ssock.getpeercert()

    # Extract the expiry date from the certificate
    expiry_date_str = cert['notAfter']
    expiry_date = datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')

    return expiry_date

def check_ssl_expiry(hostname):
    """Check if the SSL certificate for the given hostname is expired or near expiry."""
    expiry_date = get_ssl_expiry_date(hostname)
    current_date = datetime.utcnow()

    # Calculate the difference in days
    days_to_expiry = (expiry_date - current_date).days

    print(f"Hostname: {hostname}")
    print(f"SSL Certificate Expiry Date: {expiry_date}")
    print(f"Days until expiry: {days_to_expiry}")

    if days_to_expiry < 0:
        print("The SSL certificate has expired.")
    elif days_to_expiry < 30:
        print("The SSL certificate will expire soon (within 30 days).")
    else:
        print("The SSL certificate is valid.")

if __name__ == "__main__":
    # Example usage
    hostname = input("Enter the hostname (e.g., www.google.com): ")
    check_ssl_expiry(hostname)

