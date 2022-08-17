# Sandbox
Here is the models I was able to create as of NSF REU 2022. Models 1-4 are LSTM models that 
I tailored to its dataset (the csv files). Mainly tinkered with batch size and neurons in
hidden layer. My reasoning for altering batch size was due to the small size of data I was
working with and seemed that I didn't need a large batch size. For neurons in hidden layer,
from experience it is a parameter that alters the possible accuracy by a good amount. To figure
out the right amount, had to do trial and error. Would start from 16,32,64,128, and 256. I
assume there is a better method to find the right amount, but this is what I did to slowly
find the amount that makes the best accuracy. 

## CSV files
- Combo_A_Poster.csv contains all class labels
- Combo_A_Poster_5Gone.csv contains all class labels except *Class Label 'Normal'*
- Data_No4.csv contains all class labels except *Class Label 'Sudden Break'*
- Data_No4No5.csv contains all class labels except *Class Labels 'Sudden Break' & 'Normal'*

**NOTE** Class label "Sudden Acceleration" has a bias and it may have affected the accuracy.
As in we made the assumption with the mobility scooter that it takes 4 seconds for it to
accelerate to its max speed. In the end, only needed to label the data that corresponds to
the first 2 seconds and not 4 seconds. Although referenced in future work and other errors, 
will say it again here. The first 1-2 seconds is needed for labeling as the 'jerking' movement
that causes sudden movement is recorded from the raspberry pis and the rest of the movement
is not needed to be recorded to be also 'sudden.'