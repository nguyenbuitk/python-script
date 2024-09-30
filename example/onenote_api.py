import msal
import webbrowser
from msal import PublicClientApplication

# Azure app registration details
client_id = 'c4d878fb-6535-407f-a277-427473665be4'
tenant_id = 'f8cdef31-a31e-4b4a-93e4-5f571e91255a'

# The OAuth 2.0 endpoint for your tenant
authority = f"https://login.microsoftonline.com/{tenant_id}"
authority_url = "https://login.microsoftonline.com/consumers"
base_url = 'https://graph.microsoftonlinne.com/v1.0'
# The Microsoft Graph API scope
scope = ["https://graph.microsoft.com/.default"]

endpoint = base_url + 'me'

client_instance = msal.ConfidentialClientApplication(
    
)