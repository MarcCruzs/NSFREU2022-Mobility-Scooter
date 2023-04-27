from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime
from csv import writer
import time
import sys
from time import sleep
import os

'''Change "csvncame" to whatever day and run # that day is on. Do this manually as its faster to change manually
than automatically'''

csvname = "foo.csv"

sense = SenseHat()
sense.set_imu_config(True, True, True)
sense.clear()
logging = False
offSwitch = False

#This function handles obtaining the raw acceleration and raw gyroscope data
def get_Data():
    '''get_Data() function is used to extract accelerometer and gyroscope data. This function would be later on used in a while loop
    to create a constant stream of data.

    args:
    None

    returns:
    an array containing accelerometer gyroscope data.
    format of data:
        [acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z]
    '''
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
    time.sleep(.5)
    return s_data


'''To make it easier on the field, every time the 'start' switch is flicked the sense hat rgb grid will turn green, while
the 'stop' switch is flicked the sense hat rgb grid turns red. Do note when stopping the code it will keep the same
color that is being displayed at the time of stopping the code
'''

''' Used 8x8 pixel grid to create indicators:
- Armed/Ready = blue grid
- Required File Rename = yellow grid
- Running = green grid
- stopped = red grid
'''
BLUE = (0, 0, 255)      #blue
GREEN = (0, 255, 0)     #green
RED = (255, 0, 0)       #red
YELLOW = (255, 255, 0)  #yellow
PURPLE = (160,32,240)   #purple

#converted the constant variables to simpler names to make the grids easier to understand
b = BLUE
g = GREEN
r = RED
y = YELLOW
p = PURPLE


purple = [
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    ]

green = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    ]

blue = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    ]

red = [
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    ]

yellow = [
    y, y, y, y, y, y, y, y,
    y, r, y, r, y, r, y, y,
    y, r, y, r, y, r, y, y,
    y, r, y, r, y, r, y, y,
    y, r, y, r, y, r, y, y,
    y, y, y, y, y, y, y, y,
    y, r, y, r, y, r, y, y,
    y, y, y, y, y, y, y, y,
    ]

#This is the safety net that stops the code from running if there is already another csv file with the csv name.
Check = os.path.exists(csvname)
if Check:
    print('Name already Exists')
    sense.set_pixels(yellow)
    exit()
else:
    print("Ready")
    sense.set_pixels(blue)

def pushed_up(event):
    global logging, timestart
    if event.action == ACTION_PRESSED:
        print("START")
        sense.set_pixels(green)
        logging = True

def pushed_down(event):
    global offSwitch, logs
    if event.action != ACTION_PRESSED:
        print("STOP")
        sense.set_pixels(red)
        offSwitch = True
        
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

#Added timestamp to do better labelling
#Note: elapse time can start at random number sometimes. So it can start on the 1000 second or on the 20 second.
#To fix this issue would match the elapse time with the corresponding helmet view recording.
timestamp = datetime.now()
timestart = datetime.now()

with open(csvname, 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z', 'datetime', 'elapsed'])

    # Constantly uploading data until the raspberry pi is stopped.
    while True:
        try:
            if logging:
                    data = get_Data()
                    dt = elapsed = data[-1] - timestart
                    data.append(round(elapsed.total_seconds(), 1))
                    data_writer.writerow(data)
                    timestamp = datetime.now()
                    size = os.path.getsize('/home/reu/Desktop/Code/{0}'.format(csvname))
                    if size > 0:
                        sense.set_pixels(purple)
            if offSwitch:
                logging = False
                print("Switch | Closing File and saving data ...")
                f.close()
                break
        except KeyboardInterrupt:
            sense.set_pixels(red)
            print("Key Interruption | Closing File and saving data ...")
            f.close()
                
