import requests
import json
login = "6183075ec563d6081f43ccc7"
password = "0134d833880f83db9815b8b64493882a"
authentication = (login, password)
#device ID (4D76AD, 2A0D6F8)
device = "4D76AD"
print()
response = requests.get("https://api.sigfox.com/v2/devices/" + device + "/messages", auth=authentication).json()
with open("Sigfox_returned_4D76AD.json", 'w') as f:
    json.dump(response['data'], f)

response = response['data']
i = 0
a = {}
while (1):
    try:
        data = response[i]['data']
        time = response[i]['time']
        a[time] = data
        i += 1
    except:
        break

with open("Sigfox_4D76AD_data_time.json", 'w') as f:
    json.dump(a, f)

device = "2A0D6F8"
print()
response = requests.get("https://api.sigfox.com/v2/devices/" + device + "/messages", auth=authentication).json()
with open("Sigfox_returned_2A0D6F8.json", 'w') as f:
    json.dump(response['data'], f)

response = response['data']
i = 0
a = {}
while (1):
    try:
        data = response[i]['data']
        time = response[i]['time']
        a[time] = data
        i += 1
    except:
        break

with open("Sigfox_2A0D6F8_data_time.json", 'w') as f:
    json.dump(a, f)
# The variable response contains the response from the server