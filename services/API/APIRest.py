
import requests
from requests.auth import HTTPBasicAuth

class APIRest :

    def __init__(self):
        return

    def BasicAuthentication(self, url, method , credentials):
        
        response = requests.post(f"{url}/{method}", auth=(credentials['user'], credentials['pass']))

        return response