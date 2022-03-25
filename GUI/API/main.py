import requests
import json
import binascii
login = "6183075ec563d6081f43ccc7"
password = "0134d833880f83db9815b8b64493882a"
authentication = (login, password)
#device ID (4D76AD, 2A0D6F8)
#device = "4D76AD"
#print()
#response = requests.get("https://api.sigfox.com/v2/devices/" + device + "/messages", auth=authentication).json()
#with open("Sigfox_returned_4D76AD.json", 'w') as f:
#    json.dump(response['data'], f)

#response = response['data']
#i = 0
#a = {}
#while (1):
#    try:
#        data = response[i]['data']
#        time = response[i]['time']
#        a[time] = data
#        i += 1
#    except:
#        break

#with open("Sigfox_4D76AD_data_time.json", 'w') as f:
#    json.dump(a, f)



def two2dec(s):
    int_value = int(s, base=16)
    bin_value = bin(int_value)
    s = str(bin_value)[2:]
    if len(s) != 8:
        num = 8 - len(s)
        s = '0'*num + s
    if s[0] == '1':
        return -1 * (int(''.join('1' if x == '0' else '0' for x in s), 2) + 1)
    else:
        return int(s, 2)
device = "2A0D6F8"
print()
response = requests.get("https://api.sigfox.com/v2/devices/" + device + "/messages", auth=authentication).json()
with open("./Sigfox_2A0D6F8/Sigfox_returned_2A0D6F8.json", 'w+') as f:
    json.dump(response['data'], f)

response = response['data']
i = 0
a = {}
while (1):
    try:
        data = response[i]['data']
        if data == "ffffffffffffffffffffffff":
            break
        time = response[i]['time']
        t = {}
        t['time'] = time
        #print(t)
        t['Coordinate_x'] = data[:2]
        t['Coordinate_y'] = data[2:4]
        temp_1 = data[4:6]
        temp_2 = data[6:8]
        t['Temperature'] = int(temp_1, 16) + 0.01 * int(temp_2, 16)
        Hum_1 = data[8:10]
        Hum_2 = data[10:12]
        #print(t)
        t['Humidity'] = int(Hum_1, 16) + 0.01 * int(Hum_2, 16)
        #print(t)
        airx_1 = two2dec(data[12:14])
        airx_2 = data[14:16]
        #print(airx_1 + 0.01 * int(airx_2, 16))
        if airx_1 < 0:
            t['Airflow_X'] = str(airx_1 - 0.01 * int(airx_2, 16))
        else:
            t['Airflow_X'] = str(airx_1 + 0.01 * int(airx_2, 16))
        #print(t)
        #print(data)
        airy_1 = two2dec(data[16:18])
        #print(data[16:18])
        airy_2 = data[18:20]
        #print(airy_1)
        if airy_1 < 0:
            t['Airflow_Y'] = str(airy_1 - 0.01 * int(airy_2, 16))
        else:
            t['Airflow_Y'] = str(airy_1 + 0.01 * int(airy_2, 16))
        airz_1 = two2dec(data[20:22])
        airz_2 = data[22:24]
        if airz_1 < 0:
            t['Airflow_Z'] = str(airz_1 - 0.01 * int(airz_2, 16))
        else:
            t['Airflow_Z'] = str(airz_1 + 0.01 * int(airz_2, 16))
        print(t)
        a[i] = t
        #a[i].append(data)
        i += 1
    except:
        break

with open("./Sigfox_2A0D6F8/Sigfox_2A0D6F8_data_time.json", 'w+') as f:
    json.dump(a, f)