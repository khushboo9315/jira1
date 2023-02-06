import requests
import json
import io

url ="https://khushboo9315.atlassian.net/rest/api/2/user"
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

with io.open("users.csv","r",encoding="utf-8")as f1:
  user_data=f1.read()
  f1.close()
  user_data=user_data.split("\n")[1:]
  for users in user_data:
    display_name=users.split(",")[0]
    pwd=users.split(",")[1]
    email=users.split(",")[2]
    name=users.split(",")[2]


    payload=json.dumps(
    {
      "Password":"jira@123",
      "emailAdress":"test1@atlassian.com",
      "displayName":"test1",
      "name":"test1user1"
    }
    )
    response=requests.post(url,headers=headers,data=payload,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
    print(response.text)

# this will be create a issue'''