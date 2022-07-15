from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime
from csv import writer
import time
import sys
from time import sleep
import os

'''Change "csvname" to whatever day and run # that day is on. Do this manually as its faster to change manually
than automatically'''

csvname = "qfwijujhbfwegjkbiwfeg.csv"

sense = SenseHat()
sense.set_imu_config(True, True, True)
sense.clear()
logging = False


# This function handles obtaining the raw acceleration and raw gyroscope data
def get_Data():
    s_data = []
    acceleration = sense.get_accelerometer_raw()
    acc_x = acceleration['x']
    acc_y = acceleration['y']
    acc_z = acceleration['z']

    acc_x = round(acc_x, 16)

    acc_y = round(acc_y, 16)
    acc_z = round(acc_z, 16)
    s_data.append(acc_x)
    s_data.append(acc_y)
    s_data.append(acc_z)

    gyro = sense.get_gyroscope_raw()

    gyro_x = gyro['x']
    gyro_y = gyro['y']
    gyro_z = gyro['z']

    acc_x = round(gyro_x, 16)
    acc_y = round(gyro_y, 16)
    acc_z = round(gyro_z, 16)
    s_data.append(gyro_x)
    s_data.append(gyro_y)
    s_data.append(gyro_z)

    s_data.append(datetime.now())
    sleep(.5)
    return s_data


'''To make it easier on the field, every time the 'start' switch is flicked the sense hat rgb grid will turn green, while
the 'stop' switch is flicked the sense hat rgb grid turns red. Do note when stopping the code it will keep the same
color that is being displayed at the time of stopping the code'''
b = (0, 0, 255)  # blue
g = (0, 255, 0)  # green
r = (255, 0, 0)  # red
y = (255, 255, 0)  # yellow

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

# This is the safety net that stops the code from running if there is already another csv file with the csv name.
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
    global logging, logs
    if event.action != ACTION_PRESSED:
        print("STOP")
        sense.set_pixels(red)
        logging = False


sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

# Added timestamp to do better labelling
# Note: elapse time can start at random number sometimes. So it can start on the 1000 second or on the 20 second.
# To fix this issue would match the elapse time with the corresponding helmet view recording.
timestamp = datetime.now()
timestart = datetime.now()

with open(csvname, 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z', 'datetime', 'elapsed'])

    # Constantly uploading data until the raspberry pi is stopped.
    while True:
        if logging:
            data = get_Data()
            dt = data[-1] - timestart
            elapsed = data[-1] - timestart
            data.append(round(elapsed.total_seconds(), 1))
            data_writer.writerow(data)
            timestamp = datetime.now()
            size = os.path.getsize('/home/rjanairo/CSV_SenseHat/{0}'.format(csvname))
            print(size)
            print(data)
