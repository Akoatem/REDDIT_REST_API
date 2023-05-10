
import requests
from credential import USERNAME, PASSWORD
# create two variables

CLIENT_ID = 'o0GTU4ezjUkDh4UHddhVWA'
CLIENT_SECRET = 'd9CL2KkU-Rv9cOIUmxOu4HmA2vvMHQ'

# to get temproary token from reddit authorization
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

# login
with open('pw.txt', 'r') as f:
    pw = f.read
# create a dictionary
data = {
    'grant type': 'password',
    'username' : 'Akoatem',
    'password' : pw
}

# create the cersion
headers = {'User.Agent': 'MyAPI/0.0.1'}

# send a request for our token

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers= headers)
TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

print(headers)


