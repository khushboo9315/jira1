import requests
import json
import io
url ="https://khushboo9315.atlassian.net/rest/api/3/search"
headers = {

    "Accept": "application/json",
    "Content-Type": "application/json"
}

query = {
  'jql': 'project = KHUS'
}
response=requests.get(url,headers=headers,params=query,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
data =response.json()
issues=data["issues"]
for issue in issues:
    issue_key=issue["key"]
    url1="https://khushboo9315.atlassian.net/rest/api/3/issue/"+issue_key
    response=requests.get(url1,headers=headers,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
    data=response.json
    print('issue id is {issue_key}and status is{data["feilds"]["status"]["name"]}')

