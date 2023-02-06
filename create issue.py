import requests
import json
url ="https://khushboo9315.atlassian.net/rest/api/2/issue"
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload=json.dumps(
    {
    "fields": {
       "project":
       {
          "key": "KHUS"
       },
       "summary": "my first jira issue",
       "description": "created for my practice",
       "issuetype": {
          "name": "Task"
       }
   }
}
)
response=requests.post(url,headers=headers,data=payload,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
print(response.text)

# this will be create a issue