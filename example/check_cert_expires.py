from datetime import datetime
from OpenSSL import crypto as c

with open('/home/nguyenbuitk/Downloads/www.example.org', 'r') as cert_file:
    cert_data = cert_file.read()



cert = c.load_certificate(c.FILETYPE_PEM, cert_data)
expiry_date = cert.get_notAfter().decode('ascii')

expiry_datetime = datetime.strptime(expiry_date,"%Y%m%d%H%M%SZ")
print("Certificate Expiry Date: ", expiry_datetime)
