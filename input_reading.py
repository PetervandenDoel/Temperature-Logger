import time
import serial
import serial.tools.list_ports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math





# configure the serial port
try:
    ser = serial.Serial(
        port='COM6', # Change as needed
        baudrate=115200,

        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.EIGHTBITS
    )
    ser.isOpen()
except:
    portlist=list(serial.tools.list_ports.comports())
    print ('Available serial ports:')
    for item in portlist:
       print (item[0])
    exit()




xsize=100
   
def data_gen():
    t = data_gen.t
    i=1
    while True:
       
       t+=1
       i+=1
       strin = ser.readline()
       strin1=strin.decode('utf-8')
       contains_digit = any(map(str.isdigit, strin1))
       if(contains_digit==False):
          val=23
       else :
           val=float(strin1)

       if(val>28):
           line.set_color('red')
       elif(val<20):
           line.set_color('blue')
       else:
           line.set_color('yellow')
       print (val)
       #val=100.0*math.sin(t*2.0*3.1415/100.0)
       yield t, val

def run(data):
    # update the data
    t,y = data
    if t>-1:
        xdata.append(t)
        ydata.append(y)
        if t>xsize: # Scroll to the left.
            ax.set_xlim(t-xsize, t)
        line.set_data(xdata, ydata)

    return line,
#cool guy
def on_close_figure(event):
    sys.exit(0)


data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [] ,lw=2)
ax.set_ylim(15, 35)
ax.set_xlim(0, xsize)
ax.grid()
xdata, ydata = [], []
plt.xlabel("Time (50ms scale)")
plt.ylabel("Temperature °C")

    


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10, repeat=False)
plt.show()



    
