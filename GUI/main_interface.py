from doctest import master
import tkinter as tk
import tkinter.messagebox
import pickle
import requests
import json
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns
import binascii

 


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.master.geometry("1025x750")
        self.master.title("FloBotics Graphic User Interface")
        self.new()

    def new(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Load",command=self.load)
        filemenu.add_command(label="Save",command=self.close)
        filemenu.add_command(label="Back",command=self.new)
        menubar.add_cascade(label="Menu",menu=filemenu)
        self.master.config(menu=menubar)
        self.bt_login=tk.Button(self.master,text='  Airflow  ',command=self.AF_load)
        self.bt_login.place(x=590,y=700)
        self.bt_logup=tk.Button(self.master,text='Temperature',command=self.Temp_load)
        self.bt_logup.place(x=390,y=700)
        self.bt_login=tk.Button(self.master,text='  Humidity ',command=self.Humid_load)
        self.bt_login.place(x=500,y=700)

    def load(self):
        login = "6183075ec563d6081f43ccc7"
        password = "0134d833880f83db9815b8b64493882a"
        authentication = (login, password)
        #device ID (4D76AD, 2A0D6F8)
        #device = "4D76AD"
        #print()
        #response = requests.get("https://api.sigfox.com/v2/devices/" + device + "/messages", auth=authentication).json()
        #with open("./Sigfox_4D76AD/Sigfox_returned_4D76AD.json", 'w+') as f:
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

        #with open("./Sigfox_4D76AD/Sigfox_4D76AD_data_time.json", 'w+') as f:
        #    json.dump(a, f)
        def two2dec(s):
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
                print(t)
                t['Coordinate_x'] = data[:2]
                t['Coordinate_y'] = data[2:4]
                temp_1 = data[4:6]
                temp_2 = data[6:8]
                t['Temperature'] = int(temp_1, 16) + 0.01 * int(temp_2, 16)
                Hum_1 = data[8:10]
                Hum_2 = data[10:12]
                print(t)
                t['Humidity'] = int(Hum_1, 16) + 0.01 * int(Hum_2, 16)
                airx_1 = two2dec(binascii.unhexlify(data[12:14]))
                airx_2 = data[14:16]
                t['Airflow_X'] = airx_1 + 0.01 * int(airx_2, 16)
                airy_1 = two2dec(binascii.unhexlify(data[16:18]))
                airy_2 = data[18:20]
                t['Airflow_Y'] = airy_1 + 0.01 * int(airy_2, 16)
                airz_1 = two2dec(binascii.unhexlify(data[20:22]))
                airz_2 = data[22:24]
                t['Airflow_Z'] = airz_1 + 0.01 * int(airz_2, 16)
                print(t)
                a[i] = t
                #a[i].append(data)
                i += 1
            except:
                break

        with open("./Sigfox_2A0D6F8/Sigfox_2A0D6F8_data_time.json", 'w+') as f:
            json.dump(a, f)


    def AF_load(self):
        print('1')
        self.bt_login=tk.Button(self.master,text='  Airflow  ',command=self.AF_load)
        self.bt_login.place(x=590,y=700)
        self.bt_logup=tk.Button(self.master,text='Temperature',command=self.Temp_load)
        self.bt_logup.place(x=390,y=700)
        self.bt_login=tk.Button(self.master,text='  Humidity ',command=self.Humid_load)
        self.bt_login.place(x=500,y=700)
        localtime = time.time()
        print ("Local Time :", localtime)

        #plt.xlabel('Coordinate_X')
        #plt.ylabel('Coordinate_Y')
        
        X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
        U, V = np.cos(X), np.sin(Y)
        fig, ax = plt.subplots()

        Q = ax.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3], units='inches', pivot='mid')
        #qk = ax.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E', coordinates='figure')
        #ax.scatter(X[::3, ::3], Y[::3, ::3], color='r', s=5)
        plt.xlabel('Coordinate_X')
        plt.ylabel('Coordinate_Y')
        plt.savefig('./Airflow/'+ str(localtime) + '.jpg')
        plt.show()
        self.mainloop()

    def Temp_load(self):
        uniform_data = [[5,10,15,20,25,30],[35,40,45,50,55,60],[65,70,75,80,85,90],[95,100,105,110,115,120],[125,130,135,140,145,150],[155,160,165,170,175,180]]
        ax = sns.heatmap(uniform_data,annot=True)
        plt.xlabel('Coordinate_X')
        plt.ylabel('Coordinate_Y')
        plt.show()
        self.bt_login=tk.Button(self.master,text='  Airflow  ',command=self.AF_load)
        self.bt_login.place(x=590,y=700)
        self.bt_logup=tk.Button(self.master,text='Temperature',command=self.Temp_load)
        self.bt_logup.place(x=390,y=700)
        self.bt_login=tk.Button(self.master,text='  Humidity ',command=self.Humid_load)
        self.bt_login.place(x=500,y=700)
        self.mainloop()

    def Humid_load(self):
        uniform_data = [[5,10,15,20,25,30],[35,40,45,50,55,60],[65,70,75,80,85,90],[95,100,105,110,115,120],[125,130,135,140,145,150],[155,160,165,170,175,180]]
        ax = sns.heatmap(uniform_data,cmap='YlGnBu',annot=True)
        plt.xlabel('Coordinate_X')
        plt.ylabel('Coordinate_Y')
        plt.show()
        self.bt_login=tk.Button(self.master,text='  Airflow  ',command=self.AF_load)
        self.bt_login.place(x=590,y=700)
        self.bt_logup=tk.Button(self.master,text='Temperature',command=self.Temp_load)
        self.bt_logup.place(x=390,y=700)
        self.bt_login=tk.Button(self.master,text='  Humidity ',command=self.Humid_load)
        self.bt_login.place(x=500,y=700)
        self.mainloop()
# The variable response contains the response from the server

    def close(self):
        self.master.destroy()