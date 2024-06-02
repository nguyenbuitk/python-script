import ssl
import socket
from datetime import datetime

def get_ssl_expiry_date(hostname):
    """Get the SSL certificate's expiry date for the given hostname."""
    port = 443
    context = ssl.create_default_context()

    try:
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
    except Exception as e:
        print(f"Could not connect to {hostname}: {e}")
        return None

    expiry_date_str = cert['notAfter']
    expiry_date = datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')

    return expiry_date

def check_ssl_expiry(hostname):
    """Check if the SSL certificate for the given hostname is expired or near expiry."""
    expiry_date = get_ssl_expiry_date(hostname)
    if not expiry_date:
        return

    current_date = datetime.utcnow()
    days_to_expiry = (expiry_date - current_date).days

    print(f"\nHostname: {hostname}")
    print(f"SSL Certificate Expiry Date: {expiry_date}")
    print(f"Days until expiry: {days_to_expiry}")

    if days_to_expiry < 0:
        print("The SSL certificate has expired.")
    elif days_to_expiry < 30:
        print("The SSL certificate will expire soon (within 30 days).")
    else:
        print("The SSL certificate is valid.")

def main():
    # List of domains to check
    domains = [
        'www.google.com',
        'www.example.com',
        'www.github.com',
        'www.nonexistentdomain.tld'  # This will demonstrate error handling
    ]

    for domain in domains:
        check_ssl_expiry(domain)

if __name__ == "__main__":
    main()

