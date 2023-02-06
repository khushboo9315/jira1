import requests
import json
url ="https://khushboo9315.atlassian.net/rest/api/2/users/search"
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
response=requests.get(url,headers=headers,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
data=response.json()
for user in data:
    print(user["displayName"])

    #if we print only user it will print all detail of the all users,, 
    # and by display name it will only display name of the users.
