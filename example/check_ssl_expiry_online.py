import ssl
import socket
from datetime import datetime


'''
1. Establish SSL/TLS connection to specified hostname
2. Retrieves the SSL certificate.
3. Extracts and parses the expiration date from the certificate
4. Returns the expiration date as 'datetime' object.
'''
def get_ssl_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssl_info = ssock.getpeercert()
            print("ssl_info", ssl_info)
            expiry_date_str = ssl_info['notAfter']
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

