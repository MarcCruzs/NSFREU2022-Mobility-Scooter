#Instructions

For the Data Collection preprocessing work, we will want to get the raw data and get the mean of every 2 rows. We combine every 2 rows as we collect 2 samples per second and from mimicing the work of a kaggle dataset for driving behavior where they also got the mean and collected 2 samples per second.

Steps:
1. Extract the CSV Files to whatever day you are trying to start preprocessing. Can do this with installing the github desktop and using the external editor to grab specific CSV files. (There is likely a better method to extract specific files, but this seems to work for Marc)
2. Extract the video(s) that correspond to what CSV file(s) that you are planning to preprocess. Will use the video(s) to help label the data with 5 class labels: 
*Sudden Acceleration* (1), *Sudden Right Turn* (2), *Sudden Left Turn* (3), *Sudden Break* (4), and *Normal* (5)
3. Go to the video, check when the data collection actually starts (driver starts moving), then see what the stop watch on the video is at. Whatever time it is on get rid of the rows that correspond to that time. For example, if the driver starts moving 31 seconds in then in the CSV file remove all the rows that corresponds to the first 32 seconds. Why rows relating to 32 seconds and not just 31? Later on it would become an issue when averaging the data, so as best as you can keep the data even
4. Do step #3 except at the end of the video. Discard any data after the data collection is done (driver stops driving).
5. With the CSV file get the mean of every 2 rows for all columns except *Time Stamp* & *Time Elapsed*
6. Then with the dataset that was averaged label each row with the 5 Class Labels by checking the video and seeing at what times a class label occurs. (ex. driver at 21-23 seconds does a sudden right turn, label the rows corresponding to 21-23 seconds)
7. For rows (samples, instances, or etc [There is a lot of interchangeable words]) that is hard to determine what class label the row should be then just discard that row and move on. Any uncertainty can ruin the quality of the data.
8. With the CSV File, add it back into the original folder you got the csv file from and name it: **[Orginal Name]_Processed.csv**
