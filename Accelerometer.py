from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime
from csv import writer
import time
import sys
from time import sleep
import os

csvname = "June23_Run_0.csv"


sense = SenseHat()
sense.set_imu_config(True, True, True)
sense.clear()
logging = False

def get_Data():
    s_data = []
    acceleration = sense.get_accelerometer_raw()
    acc_x = acceleration['x']
    acc_y = acceleration['y']
    acc_z = acceleration['z']
    
    
    acc_x=round(acc_x,16) 

    acc_y=round(acc_y,16) 
    acc_z=round(acc_z,16) 
    s_data.append(acc_x)
    s_data.append(acc_y)
    s_data.append(acc_z)
    
    gyro = sense.get_gyroscope_raw()
    gyro_x = gyro['x']
    gyro_y = gyro['y']
    gyro_z = gyro['z']
    
    acc_x=round(gyro_x,16) 
    acc_y=round(gyro_y,16) 
    acc_z=round(gyro_z,16)
    s_data.append(gyro_x)
    s_data.append(gyro_y)
    s_data.append(gyro_z)
    
    s_data.append(datetime.now())
    sleep(.5)
    return s_data

g = (0, 255, 0)     # green
r = (255, 0, 0)     # red


green = [ # >_< ._.
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    ]



red = [ # >_< ._.
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
    ]


def pushed_up(event):
    global logging, timestart
    if event.action == ACTION_PRESSED:
        print("START")
        sense.set_pixels(green)
        logging = True

def pushed_down(event):
    global logging, logs
    if event.action != ACTION_PRESSED:
        print("STOP")
        sense.set_pixels(red)
        logging = False
        
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

timestamp = datetime.now()
timestart = datetime.now()
delay = 1000

with open(csvname,'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['acc_x','acc_y','acc_z','gyro_x','gyro_y','gyro_z','datetime','elapsed'])

    while True:
        if logging:
            data = get_Data()
            dt = data[-1] - timestart
            elapsed = data[-1] - timestart
            data.append(round(elapsed.total_seconds(),1))
            data_writer.writerow(data)
            timestamp = datetime.now()
            size = os.path.getsize('/home/reu/Desktop/Code/{0}'.format(csvname))
            print(size)
            print(data)
            
            
