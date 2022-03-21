import tkinter as tk
import tkinter.messagebox
import pickle
import main_interface

def main():
#window
    window=tk.Tk()
    window.title('FloBotics')
    window.geometry('450x300')
    #photo
    canvas=tk.Canvas(window,height=300,width=500)
    imagefile=tk.PhotoImage(file='qm.png')
    image=canvas.create_image(130,0,anchor='nw',image=imagefile)
    canvas.pack(side='top')
    #label for user and password
    tk.Label(window,text='Username:').place(x=90,y=150)
    tk.Label(window,text='Password:').place(x=90,y=190)
    #username input
    var_usr_name=tk.StringVar()
    entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
    entry_usr_name.place(x=160,y=150)
    #passwrd input
    var_usr_pwd=tk.StringVar()
    entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
    entry_usr_pwd.place(x=160,y=190)
        
    #login
    def usr_log_in():
        #get username and password
        usr_name=var_usr_name.get()
        usr_pwd=var_usr_pwd.get()
        #find info from dict
        try:
            with open('usr_info.pickle','rb') as usr_file:
                usrs_info=pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle','wb') as usr_file:
                usrs_info={'admin':'admin'}
                pickle.dump(usrs_info,usr_file)
        #username and pass equal
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                window.destroy()
                top=tk.Tk()
                myapp = main_interface.App(top)
                myapp.mainloop()
            else:
                tk.messagebox.showerror(message='Wrong password')
        #username and password can't empty
        elif usr_name=='' or usr_pwd=='' :
            tk.messagebox.showerror(message='Empty username or password')
        #unfind user pop register
        else:
            is_signup=tk.messagebox.askyesno('Welcome','Invaild user please sign up')
            if is_signup:
                usr_sign_up()
    #register
    def usr_sign_up():
        def signtowcg():
            #get info
            nn=new_name.get()
            np=new_pwd.get()
            npf=new_pwd_confirm.get()
    
            #load local dict data
            try:
                with open('usr_info.pickle','rb') as usr_file:
                    exist_usr_info=pickle.load(usr_file)
            except FileNotFoundError:
                exist_usr_info={}           
                
            #data check
            if nn in exist_usr_info:
                tk.messagebox.showerror('Error','Exist username')
            elif np =='' or nn=='':
                tk.messagebox.showerror('Error','Empty username or password')
            elif np !=npf:
                tk.messagebox.showerror('Error','Password different')
            #input to dict
            else:
                exist_usr_info[nn]=np
                with open('usr_info.pickle','wb') as usr_file:
                    pickle.dump(exist_usr_info,usr_file)
                tk.messagebox.showinfo('Welcome','Success')
                #exit
                window_sign_up.destroy()
        #registor box
        window_sign_up=tk.Toplevel(window)
        window_sign_up.geometry('350x200')
        window_sign_up.title('Sign up')
        #user input
        new_name=tk.StringVar()
        tk.Label(window_sign_up,text='Username：').place(x=10,y=10)
        tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
        #password input
        new_pwd=tk.StringVar()
        tk.Label(window_sign_up,text='Password：').place(x=10,y=50)
        tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
        #2 password input
        new_pwd_confirm=tk.StringVar()
        tk.Label(window_sign_up,text='Password：').place(x=10,y=90)
        tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
        #confirm
        bt_confirm_sign_up=tk.Button(window_sign_up,text='Confirm',
                                    command=signtowcg)
        bt_confirm_sign_up.place(x=150,y=130)
    #exit
    def usr_sign_quit():
        window.destroy()
    #login and register button
    bt_login=tk.Button(window,text='Sign In',command=usr_log_in)
    bt_login.place(x=140,y=230)
    bt_logup=tk.Button(window,text='Sign Up',command=usr_sign_up)
    bt_logup.place(x=210,y=230)
    bt_logquit=tk.Button(window,text='Quit',command=usr_sign_quit)
    bt_logquit.place(x=280,y=230)
    #main loop
    window.mainloop()