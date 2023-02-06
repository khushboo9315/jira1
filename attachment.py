import requests
import json
import io
url ="https://khushboo9315.atlassian.net/rest/api/3/issue/khus-1/attachments"
headers = {
     "X-Atlassian-Token": "no-check"

}

files={
    "file":("users.csv",open("users.csv","rb"))
}
response=requests.post(url,headers=headers,files=files,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
print(response.text)


# we can attach attachment using this in our issues