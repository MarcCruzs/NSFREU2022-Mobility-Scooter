# Code
All the python files should be documented. Although some files are better documented than others, so I suggest going through LSTM.py and GRU.py if looking for better understanding of the Machine Learning code. The RaspberryPiCode.py is what was used for the raspberry pi 4 and sensor hat to allow it to collect Accelerometer and Gyroscope X, Y, and Z axis.

- The [**LSTM**](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/code/LSTM.py)
and [**GRU**](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/code/GRU.py)
used a [CSV file](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/tree/main/Data/Kaggle%20Driving%20Behavior%20Dataset) from a [Kaggle Dataset](https://www.kaggle.com/datasets/shashwatwork/driving-behavior-dataset) on driving behavior.
Both python scripts are two different machine learning models using the same csv file.
- [**ClassLabelFilter.py**](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/code/ClassLabelFilter.py)
can be used to filter labelled csv files to separate the labels into 5 csv files that correspond to each class label (Sudden Acceleration, Sudden Left Turn, Sudden Right Turn, Sudden Break, and Normal). 
- [**RaspberryPiCode.py**](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/code/RaspberryPiCode.py)
is used in thonny python IDE in the raspberry pi 4 with sensor hat that allows recording of Accelerometer and Gyroscope data 
- [**HeartRate.py**](https://github.com/MarcCruzs/NSFREU2022-Mobility-Scooter/blob/main/code/HeartRate.py) used to convert and organize json file for Polar H9 heart rate sensor

