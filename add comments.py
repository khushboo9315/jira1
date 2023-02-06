import requests
import json
import io
url ="https://khushboo9315.atlassian.net/rest/api/3/issue/khus-2/comment"
headers = {

    "Accept": "application/json",
  "Content-Type": "application/json"
}

data=json.dumps({
  
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "text": "hi this is comment 1 by code",
            "type": "text"
          }
        ]
      }
    ]
  }
})

response=requests.post(url,headers=headers,data=data,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
print(response.text)
