# Data Preprocesssing/Labeling Instructions

For the Data Collection preprocessing work, we will want to get the raw data and get the mean of every 2 rows. We combine every 2 rows as we collect 2 samples per second and from mimicing the work of a kaggle dataset for driving behavior where they also got the mean and collected 2 samples per second.

Steps:
1. Extract the CSV Files to whatever day you are trying to start preprocessing. Can do this with installing the github desktop and using the external editor to grab specific CSV files. (There is likely a better method to extract specific files, but this seems to work for Marc)
2. Extract the video(s) that correspond to what CSV file(s) that you are planning to preprocess. Will use the video(s) to help label the data with 5 class labels: 

*Sudden Acceleration* (1), *Sudden Right Turn* (2), *Sudden Left Turn* (3), *Sudden Break* (4), and *Normal* (5)

3. Create a table in app (ex: excel, doc, word, etc) with label (1 Sudden Acceleration) (2 Sudden Right) (3 Sudden Left) (4 Sudden Break) (5 Normal) 

4. Watch the entire video that correspond with the specific run, 
    1) Record the time stamp of each abnormaties under corresponding labels
    2) Record the time it takes for the Rasberry Pi to be turned on (Ex: after video starts, it takes 15 seconds until the Rasberry Pi starts)
    3) Record the starting time (where the scooter starts moving forward)
    4) Record the ending time (where the scooter completely stops)
    5) Record the time of segments where the direction or labeling will be unclear (Ex: Moving backwards, unsure if driver did a left or sudden left, etc)

5. Prepare for labeling 
    1) Copy and paste the CSV data into the data template (in Processed CSV Files folder) 
    2) Select the columns (Row #	acc_x	acc_y	acc_z	gyro_x	gyro_y	gyro_z	datetime	IGNORE	Elapsed) and drag them down to bottom of data set
    3) Add a 5 under the Labels and drag it down until the end of the data set
    4) Double click the function under Elapsed Time label and add the time it takes for Rasberry Pi to be turned on at the end of the function (Ex: If it takes 15 seconds for the Rasberry Pi to be started, at the function make =OFFSET(Q2,ROW(I2)-1,0) into =OFFSET(Q2,ROW(I2)-1,0)+15)
    5) Delete or grey out the extra labels at the start (from start of Rasberry Pi to the start of scooter moving) 
    6) Delete or grey out the extra labels at the end (from the moment scooter completly stops to the end of the data set)
    7) Delete or grey out the segments of labels where the labeling will be unclear based on step 4 

6. Label the labels column with corresponding numbers based on time stamp from table made in step 3 and elapsed time (Ex: In table it says a sudden left from 78 seconds to 82 seconds, label 3 from 78 to 82) 
    1) Round down if elapsed time is a decimal
    
7. Save the finished CSV file and upload it into the Procssed CSV Files folder name it **PR_[Original Name].csv**
