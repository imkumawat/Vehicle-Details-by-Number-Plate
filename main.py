import requests
from html.parser import HTMLParser
from Token import getToken
from SessionID import getSessionID


session = requests.session()

vahan_url = "https://vahaninfos.com/vehicle-details-by-number-plate/"

headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}

data = {"number": "RJ01WS0647"}

try:

    remote_response = session.get(vahan_url, headers=headers, verify=False)
    if remote_response.status_code == 200:
        print("Remote Server is up and running! :)")
        print()
        print("1. Enter Bike Number\n2. Continue with defualt\n?")
        if(int(input())==1):
            print("Please Enter Bike Number")
            data["number"] = input()

except Exception as e:
    
    print("Remote Server Down! :(")
    print()
    print(e.__class__)
    exit(0)


remote_server_content  = str(remote_response.content)
token = getToken.get_token(remote_server_content)

header = remote_response.headers

session_id = getSessionID.get_SessionID(header)


vahan_url = "https://vahaninfos.com:443/getdetails.php"

headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest", "Num": token, "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://vahaninfos.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://vahaninfos.com/vehicle-details-by-number-plate", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}


try:

    info = requests.post(vahan_url, headers=headers, cookies=session_id, data=data, verify=False)

except Exception as e:
    
    print("Remote Server Down! :(")
    print()
    print(e.__class__)
    exit(0)


getdata=[]
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        getdata.append(data)

parser = MyHTMLParser()
parser.feed(str(info.content))

rm=["b'","\\r\\n        ",":","Financer","Fitness/Regn Upto",
    "Engine Capacity","Color","Ownership Type","Vehicle Age","Vehicle Type",
    "Vehicle Category","'"]
getdata1=[]
for x in getdata:
    getdata1.append(x)
for ele in getdata1:
    if rm.count(ele):
        getdata.remove(ele)

for i in range(0,20,2):
    print(getdata[i]," ---> ",getdata[i+1])