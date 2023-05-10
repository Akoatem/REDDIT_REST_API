import requests
import response
import requests.auth
from credential import USERNAME, PASSWORD
from rich import print


# create two variables

CLIENT_ID = 'sG5Z60C0f7WXIfX4PKg4BQ'
CLIENT_SECRET = 'I7iqIhpjlqdBATChzXIwRVLZKrc3Mg'


# Step 1 getting authentication info for reddit App
# to get temproary token from reddit authorization app
client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

# create a dictionary
post_data = {
    'grant_type': 'password',
    'username' : USERNAME,
    'password' : PASSWORD
}

headers = {
    'User-Agent': 'A Red automation script 1.1 by Ako'
    }

# Step 2 getting token access ID

TOKEN_ACCESS_POINT = 'https://www.reddit.com/api/v1/access_token'
response = requests.post(TOKEN_ACCESS_POINT, data=post_data, headers=headers, auth=client_auth)

#ad = response.json()
#print(response.reason)
if response.status_code == 200:
    token_id = response.json()['access_token']

# step 3 use reddit's  REST API to perform operation
OAUTH_ENDPOINT = 'https://oauth.reddit.com'
after_key = 0

get_params = {
    'limit': 100,
    'after': after_key
}
headers_get ={
    'User-Agent': 'A Red automation script 1.1 by Ako',
    'Authorization': 'Bearer ' + token_id
}
response2 = requests.get(OAUTH_ENDPOINT + '/r/Python/new/', headers=headers_get, params=get_params)
print(response2)
# save it as data
#print(response2.json())
data = response2.json()
get_key = data['data'].keys()
# print(get_key)
# the children returns the posts

posts = data['data']['children']
after_key =  data['data']['after']
#print(after_key)

before_key =  data['data']['before']
#print(before_key)

#print(len(posts))

get_params = {
    'limit': 5,
    'after': after_key
}
headers_get ={
    'User-Agent': 'A Red automation script 1.1 by Ako',
    'Authorization': 'Bearer ' + token_id
}
response3 = requests.get(OAUTH_ENDPOINT + '/r/Python/new/', headers=headers_get, params=get_params)
data = response3.json()
#get_key = data['data'].keys()
posts = data['data']['children']
after_key =  data['data']['after']
before_key =  data['data']['before']

print(before_key)
print(after_key)
print(len(posts))


requests.get(OAUTH_ENDPOINT + '/r/Python/top/')
requests.get(OAUTH_ENDPOINT + '/r/Python/best/')


