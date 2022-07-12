# NSFREU2022-Mobility-Scooter

## Summary
The focus for NSF REU Summer 2022 is to make the steps to create a multi-modal model that is capable of predicting the a binary/percentage riskiness if an individual should use a Mobility Scooter. The multi-modal would contain accelerometer, gyroscope, and heart rate data.

### Extracting Heart Rate Data
-----
- Used Polar H9 Heart Rate Sensor
- Follow this [link](https://support.polar.com/en/how-to-download-all-your-data-from-polar-flow
) for instructions\
- After downloading zip file, use [HeartRate.py](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/code/HeartRate.py)
to convert json file to csv file

### Data Folder
-----
- Data Folder contains all csv files that were used to output accelerometer, gyroscope, and heart rate data.
- Two Folders containing NSF REU csv files and a Kaggle Dataset csv file.
  - *NSF REU Folder* is organized by each day data collection occurred. Each Date Folder contains the corresponding csv files that were recorded that day and details on who was driver that day
  - *Kaggle Dataset Folder* is just one combined dataset of all featured csv files that were given in the dataset. (Go to folder for more details)
  
### Code
======
- Contains all code used in the NSF REU 2022. 

### Raspberry Pi 4 to EDUROAM Folder
-----
- Instructions to get EDUROAM wifi onto the Raspberry Pi 4 
