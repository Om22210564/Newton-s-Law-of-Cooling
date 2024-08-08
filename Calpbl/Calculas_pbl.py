from tkinter import*
from tkinter import ttk
import math as mt
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image,ImageTk       
root=Tk()
root.title("Calculas PBL")
root.geometry("1100x500+0+0")

L_T1=Label(root,text="NEWTON'S LAW OF COOLING",font=("fantasy",28,"bold"),bg='black',fg='gold',bd=6,relief=SUNKEN)
L_T1.place(x=0,y=10,width=1550,height=50)
F2=Frame(root,bd=4,bg='peachpuff',relief=RIDGE)
F2.place(x=0,y=65,width=295,height=430) 
F3=Frame(root,bd=4,background="light grey",relief=RIDGE)
F3.place(x=300,y=65,width=1228,height=720) 

#Entry Box and labels
var_temp_surrond=StringVar()
var_temp_initial=StringVar()
var_time_initial=StringVar()
var_time_unit=StringVar()
var_temp_unit=StringVar()
var_temp_semi=StringVar()
var_time_semi=StringVar()
var_temp_at_t=StringVar()

def submit():
    temp_initial=var_temp_initial.get()
    temp_unit=var_temp_unit.get()
    temp_surrond=var_temp_surrond.get()
    temp_semi=var_temp_semi.get()
    time_initial=var_time_initial.get()
    time_unit=var_time_unit.get()
    time_semi=var_time_semi.get()
    # temp_unit=var_temp_unit.get()

    if temp_initial=="" or temp_surrond=="" or temp_semi=="" or time_initial=="" or time_semi=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        constant=float(temp_initial)-float(temp_surrond)
        K=-(mt.log((float(temp_semi)-float(temp_surrond))/constant))/float(time_initial)
        Temp_at_t=(mt.exp(-K*float(time_semi)))*constant + float(temp_surrond)
        var_temp_at_t.set(str(Temp_at_t)+" "+temp_unit)
        F_time=Label(F3,text=f"Temp of body after {time_semi}({time_unit}) is:",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
        F_time.grid(row=6,column=0,sticky=W)
        E_time=ttk.Entry(F3,textvariable=var_temp_at_t,font=("times new roman",16,"bold"),width=29,state="readonly")
        E_time.grid(row=6,column=1)



#Initial Temperature of the body 
F_init_temp=Label(F3,text="Initial Temp",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
F_init_temp.grid(row=0,column=0,sticky=W)
E_init_temp=ttk.Entry(F3,textvariable=var_temp_initial,font=("times new roman",16,"bold"),width=29)
E_init_temp.grid(row=0,column=1)
#Temperature Unit
F_time_unit1=Label(F3,text="   Temperature Unit",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
F_time_unit1.grid(row=1,column=2,sticky=W)
Com_time_unit1=ttk.Combobox(F3,textvariable=var_temp_unit,font=("times new roman",15,"bold"),width=31,state="readonly")
Com_time_unit1["value"]=("Kelvin","Celsius","Fahrenheit")
Com_time_unit1.current(1)
Com_time_unit1.grid(row=1,column=3)
#Room temperature
F_room_temp=Label(F3,text="Room Temp",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
F_room_temp.grid(row=1,column=0,sticky=W)
E_room_temp=ttk.Entry(F3,textvariable=var_temp_surrond,font=("times new roman",16,"bold"),width=29)
E_room_temp.grid(row=1,column=1)
#Second Temperature of the body after "t" time_initial
F_sec_temp=Label(F3,text="Temp after Time(t)",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
F_sec_temp.grid(row=2,column=0,sticky=W)
E_sec_temp=ttk.Entry(F3,textvariable=var_temp_semi,font=("times new roman",16,"bold"),width=29)
E_sec_temp.grid(row=2,column=1)
#Time "t"
F_time=Label(F3,text="Time(t)",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
F_time.grid(row=3,column=0,sticky=W)
E_time=ttk.Entry(F3,textvariable=var_time_initial,font=("times new roman",16,"bold"),width=29)
E_time.grid(row=3,column=1)
#Time Unit
F_time_unit=Label(F3,text="         Time Unit",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
F_time_unit.grid(row=3,column=2,sticky=W)
Com_time_unit=ttk.Combobox(F3,textvariable=var_time_unit,font=("times new roman",15,"bold"),width=31,state="readonly")
Com_time_unit["value"]=("Second","Minute","Hour")
Com_time_unit.current(1)
Com_time_unit.grid(row=3,column=3)
#time_initial second
F_time=Label(F3,text="Time after which temp is to be calculated",font=("times new roman",16,"bold"),background="light grey",padx=2,pady=6)
F_time.grid(row=5,column=0,sticky=W)
E_time=ttk.Entry(F3,textvariable=var_time_semi,font=("times new roman",16,"bold"),width=29)
E_time.grid(row=5,column=1)


def graph():
    temp_initial=var_temp_initial.get()
    temp_surrond=var_temp_surrond.get()
    temp_semi=var_temp_semi.get()
    time_initial=var_time_initial.get()
    time_unit=var_time_unit.get()
    temp_unit=var_temp_unit.get()
    time_semi=var_time_semi.get()
    if temp_initial=="" or temp_surrond=="" or temp_semi=="" or time_initial=="" or time_semi=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        constant=float(temp_initial)-float(temp_surrond)
        K=-(mt.log((float(temp_semi)-float(temp_surrond))/constant))/float(time_initial)
        period=121
        List1=list()
        for j in range(1,period,5):
            T_t=(mt.exp(-K*j))*constant + float(temp_surrond)
            List1.append(T_t)
        #Matplotlib graph
        x=list(range(1,period,5))
        y=List1
        fig = plt.figure(figsize = (8, 4))
        mngr= plt.get_current_fig_manager()
        mngr.window.geometry("+400+330")
        plt.plot(x, y, color='green', linestyle='solid', linewidth = 3,
                marker='o', markerfacecolor='blue', markersize=7)
        #setting x and y axis range
        plt.ylim(1,100)
        plt.xlim(1,121)
        plt.xlabel(f'Time({time_unit})',fontdict= {'family':'arial','color':'red','size':16})
        plt.ylabel(f'Temperature({temp_unit})',fontdict= {'family':'arial','color':'red','size':16})
        plt.title('Newton\'s law of cooling',fontdict= {'family':'fantasy','color':'black','size':20},weight='bold')
        plt.show()


#Buttons 
B4=Button(F2,text="CALCULATE",command=submit,width=20,font=("times new roman",18,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
# B4.grid(row=1,column=0,pady=10)
B4.place(x=0,y=50,width=288,height=55)
B6=Button(F2,text="GRAPH",command=graph,width=20,font=("times new roman",18,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
# B6.grid(row=2,column=0,pady=10)
B6.place(x=0,y=150,width=288,height=55)
B5=Button(F2,text="END",command=root.destroy,width=20,font=("times new roman",18,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
# B5.grid(row=3,column=0,pady=10)
B5.place(x=0,y=250,width=288,height=55)
# B_Add36.place(x=50,y=50,width=100,height=100)

img3=Image.open(r"NLC.jpg")
img3=img3.resize((300,280),Image.ANTIALIAS)
photoimg3=ImageTk.PhotoImage(img3)

L3=Label(root,image=photoimg3,bd=4,relief=SUNKEN)
L3.place(x=0,y=505,width=300,height=280)
root.mainloop()


