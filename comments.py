import requests
import json
import io
url ="https://khushboo9315.atlassian.net/rest/api/3/issue/khus-1/comment"
headers = {

    "Accept": "application/json",
  "Content-Type": "application/json"
}

files={
    "file":("users.csv",open("users.csv","rb"))
}
response=requests.get(url,headers=headers,auth=("khushboo22@navgurukul.org","YVtytAyOp0bAsX1wlEVG9F4D"))
data=(response.json())
# it gives the count of comments
# print(data["total"])
with io.open("comments.csv","w",encoding="utf-8") as f1:
    for comments in data["comments"]:
        f1.write(comments["id"]+","+comments["body"]["content"][0]["content"][0]["text"]+"\n")
    f1.close()
