# NSFREU2022-Mobility-Scooter

## Summary
The focus for NSF REU Summer 2022 is to make the steps to create a multi-modal model that is capable of predicting the a binary/percentage riskiness if an individual should use a Mobility Scooter. The multi-modal would contain accelerometer, gyroscope, and heart rate data.

## GitHub Organization
While making this realized some individuals like finding relevant instructions/details 
based on what folder its in (ex. Data collection instructions in the data folder), but if
you want to simply Find Command (Ctrl + F) everything then just look into TOC.md. Wanted
to note this out of convenience -Marc

## Future Work
Issues that prevailed in the project that were not resolved as they were deemed just minor
inconveniences. Problems stated here are fixable issues that can help make different
stages in the project faster. I recommend looking over the issues to see if there is
spare time to fix any of the problems
- _**Gimbal needs stiffer extender:**_\
Gimbal may need stiffer extender as while doing data collection, it lowers if the driver
is a bit rougher, so a permanent issue is needed. We (SUM 2022 peeps) used chopsticks
to prop it up, but obviously that is not the best solution to be made.
- _**Raspberry Pi inconsistent data collection frequency:**_\
For the data collection, there was 2 raspberry pis we collected from. We tried to compare
the data that was collected together, but an issue that occurred is that Raspberry Pi B (the pi
that was put on the back of the Mobility Scooter) frequency of collecting data inconsistently
changes from 1.0 seconds to 1.1 seconds. While the other raspberry pi, is consistent with 1.1 seconds.
This leads to difficulty to align rows of data as each row should be relatively the same
time stamp but are not as one dataset time stamps lags behind the other. So have to do 
extra work to find the right rows that have similar time stamp.
- _**Improving attachments of side view GoPro:**_\
At the moment we used a lot of blue tape mixed with spoons,forks and arc shaped objective to
make a splint to keep the side view camera from moving too much.
- _**Front Camera View attachments:**_\
Similar issue with Side View as it was not 100% stable as we taped a gimbal into the basket
- _**Optimizing Data Collection Code:**_\
The code that creates a csv file and inputs Accelerometer and Gyroscope data is decent
But have to stop, modify and start code after each run. What we modify is the name of csv
file name. Code can be improved by automating naming of csv files. Usually we just change 
a number (ex. July27_Run_0 to July27_Run_1), so this can be automated.
- _**Method to make transferring csv files to where they need to be:**_\
How the csv files are extracted from the raspberry pis is through discord. We just shove
all the files from that day into a discord channel then later move it into the github. 
Obviously better way to do it, but due to the dynamics of our group just knowing how to 
move things fast in discord we just stuck to this method.

## Equipment used for Data Collection
### Cameras
Used 2 Raspberry Pi 4 models with sensor hat to collect Accelerometer and Gyroscope Data
In the NSF REU, we referenced the 2 Raspberry Pis as **"Raspberry Pi A"** & **"Raspberry Pi B."** \
Raspberry Pi A is the one that was placed on the front part of the Mobility Scooter, while
Raspberry Pi B was placed on the back part of the Mobility Scooter (Photo References of each one)\
**NOTE: we referenced this in the data collection. As descriptions of files have an *A* or *B* in it.**

Used 2 Action Cameras (bootleg "GoPros") and a phone camera attached to a gimbal.
- One Action Camera is used on the side view. Using a clamp that is attached to a part of the
arm rest (Image for reference). \
![Image Link](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/DSC_0001-2.jpg)
- The Helmet View Action Camera has a band that can be put on and angled in a way to see the
drivers hands and steering wheel.
- Phone Camera used as a front view. Attached to a gimbal to get the phone camera to follow the
body of the driver. (Individuals like leaning on one of the armchairs or like to move side to side)
  - A Gimble "is a pivoted support that permits rotation of an object about an axis" (Google)
    - Name of Gimble we used: **DJI OM5**
      - NOTE: Can use a different brand. Just referencing what gimbal used

**Essential Camera would be the Helmet View where it shows the hands and the handle that
allows a person to use to label the CSV files**

The other two cameras are used for kinesiology group to identify driver body movement. Included these cameras to just prep for the data collection. Not really using it yet in the models (They asked for a front
and side view of driver so we made it possible to do these recordings).

### Raspberry Pi
Have 2 Raspberry Pis: **Raspberry Pi A & Raspberry Pi B**\

**Raspberry Pi A** is the Pi mounted to the front section of the mobility scooter\
**Raspberry Pi B** is the Pi mounted to the back section of the mobility scooter

Each Raspberry Pi has its own portable battery. Although Raspberry Pi B shares the battery
with wireless router. Everything can be attached to the mobility scooter with velcro except
wireless router.

# Extracting recordings from Action Cameras
Will need a micro SD card reader. In the supplies there are 2-3 micro SD card readers, but
they are flimsy and one of them does not work well. I recommend using a personal one to read
the micro SD cards from the Action Cameras.

We made use of the School's personal One Drives. (If you need access of the recordings 
from REU 2022, please contact Dr. Chen. She can forward you to owner of the one drive
containing the recordings)

## Details of Data Labeling
[Details](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/Data/README.md)

## Extracting Heart Rate Data
- Used Polar H9 Heart Rate Sensor
- Make an account with Polar then go to [Diary](https://flow.polar.com/diary)  sub-section.
In this section it allows you to go to individual runs and extract csv
- NOTE: csv will give extra details too\
**ALTERNATIVE METHOD**
- Follow this [link](https://support.polar.com/en/how-to-download-all-your-data-from-polar-flow
) for instructions
- After downloading zip file, use [HeartRate.py](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/code/HeartRate.py)
to convert json file to csv file

## Data Folder
- Data Folder contains all csv files that were used to output accelerometer, gyroscope, and heart rate data.
- Two Folders containing NSF REU csv files and a Kaggle Dataset csv file.
  - *[NSF REU Folder](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/tree/main/Data/NSF%20REU%202022%20Data%20Collection)* is organized by each day data collection occurred. Each Date Folder contains the corresponding csv files that were recorded that day and details on who was driver that day
  - *[Kaggle Dataset Folder](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/tree/main/Data/Kaggle%20Driving%20Behavior%20Dataset)* is just one combined dataset of all featured csv files that were given in the dataset. (Go to folder for more details)
  
## Code Folder
- Contains all code used in the NSF REU 2022. 

## Router Info
- Explains how to use the router and how it was used to connected to Raspberry Pis to do
VNC viewer

## Raspberry Pi 4 to EDUROAM Folder
- Instructions to get EDUROAM wifi onto the Raspberry Pi 4

## Failed Attempts
While trying to optimize data collection, we ran into red tape.
- Can not use drones as the school is a no-fly zone. 
- Using VNC viewer on the school internet will not work unless you go through the IT
department. If this is at the start of a new group I recommend to tackly this issue as soon
as possible to make it easier for the time you will have on this project.
- Helmets from the mobility clinic are kid sizes, so will not work for individuals with
large heads.
- Cheap paint is not a good way to make a rough surface for sticking velcro onto. Did
this cause velcro sticky part does not stay on smooth surfaces. 