# NSFREU2022-Mobility-Scooter

## Summary
The focus for NSF REU Summer 2022 is to make the steps to create a multi-modal model that is capable of predicting the a binary/percentage riskiness if an individual should use a Mobility Scooter. The multi-modal would contain accelerometer, gyroscope, and heart rate data.

## Github Organization
While making this realized some individuals like finding relevant instructions/details 
based on what folder its in (ex. Data collection instructions in the data folder), but if
you want to simply Find Command (Ctrl + F) everything then just look into TOC.md. Wanted
to note this out of convenience -Marc

## Equipment used for Data Collection
Used 2 Raspberry Pi 4 models with sensor hat to collect Accelerometer and Gyroscope Data
In the NSF REU, we referenced the 2 Raspberry Pis as **"Raspberry Pi A"** & **"Raspberry Pi B."** \
Raspberry Pi A is the one that was placed on the front part of the Mobility Scooter, while
Raspberry Pi B was placed on the back part of the Mobility Scooter (Photo References of each one)\
**NOTE: we referenced this in the data collection. As descriptions of files have an *A* or *B* in it.**

Used 2 Action Cameras (bootleg "GoPros") and a phone camera attached to a gimble.
- One Action Camera is used on the side view. Using a clamp that is attached to a part of the
arm rest (Image for reference). 
- The Helmet View Action Camera has a band that can be put on and angled in a way to see the
drivers hands and steering wheel.
- Phone Camera used as a front view. Attached to a gimble to get the phone camera to follow the
body of the driver. (Individuals like leaning on one of the arm chairs or like to move side to side)
  - A Gimble "is a pivoted support that permits rotation of an object about an axis" (Google)
    - Name of Gimble we used: **DJI OM5**
      - NOTE: Can use a different brand. Just referencing what gimble used

**Essential Camera would be the Helmet View where it shows the hands and the handle that
allows a person to use to label the CSV files**

The other two cameras are used for kinesiology group to identify driver body movement. Included these cameras to just prep for the data collection. Not really using it yet in the models (They asked for a front
and side view of driver so we made it possible to do these recordings).

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
