import requests

# We get the ranking of only one user
url = "http://codeforces.com/api/user.info?handles=gdisastery"
response = requests.get(url)
data = response.json()
print(data['result'][0]['rating'])

# Of all users
# http://codeforces.com/api/help/objects#User
url2 = "http://codeforces.com/api/user.ratedList?activeOnly=true"
data = requests.get(url2).json()
for user in data['result']:
    print(user['handle'])