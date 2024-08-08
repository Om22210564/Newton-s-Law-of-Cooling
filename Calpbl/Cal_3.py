import math as mt
import matplotlib.pyplot as plt
Ti=float(input("Enter the initial temp of the body "))
Ts=float(input("Enter the room tempp "))
time=float(input("Enter the time after which it reaches T3 "))
T3=float(input("Enter the temp after time t "))
# time2=float(input("Enter the time afeter "))

constant=Ti-Ts
k=-(mt.log((T3-Ts)/constant))/time
# T_t= (mt.exp(-k*time2))*constant + Ts
# print(T_t)

dT=1
period=121
List1=list()
for j in range(1,period,5):
    # constant=Ti-Ts
    # k=-(mt.log((T3-Ts)/constant))/time
    T_t= (mt.exp(-k*j))*constant + Ts
    List1.append(T_t)

x=list(range(1,period,5))
y=List1
fig = plt.figure(figsize = (6, 6))
mngr= plt.get_current_fig_manager()
mngr.window.geometry("+0+0")

plt.plot(x, y, color='green', linestyle='solid', linewidth = 3,
        marker='o', markerfacecolor='blue', markersize=7)

#setting x and y axis range
plt.ylim(1,100)
plt.xlim(1,121)
plt.xlabel('Time',fontdict= {'family':'arial','color':'red','size':16})
plt.ylabel('Temperature',fontdict= {'family':'arial','color':'red','size':16})
plt.title('Graph',fontdict= {'family':'fantasy','color':'black','size':20},weight='bold')
plt.show()
