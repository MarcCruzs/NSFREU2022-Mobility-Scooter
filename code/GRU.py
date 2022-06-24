import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

'''If trying to learn from this GRU machine learning code,
then also look into the documentation for the LSTM code because both codes give
decent documentation.'''
#This CSV is the combined data from Driving Behavior Dataset features
'''Features used:
    Accelerometer's X, Y, and Z axis
    Gyroscopes X, Y, and Z axis
    In total used 6 features for this project
    For more details on the kaggle data:
    https://www.kaggle.com/datasets/shashwatwork/driving-behavior-dataset'''
DB_train = pd.read_csv('New_CombinedData.csv', names = ["Target", "X","Y","Z","GX","GY","GZ"])
#sero_features_10
#sensor_raw (1)
'''Keep in mind I splitted my information differently than what can be found online. 
usually its splitting the information into 4 variables(x_train,y_train,x_test,y_test)
,but here I split it into 2 (DS_train & DS_test) then formed them into the
4 variables stated earlier'''
#Splitting Data into train and test (80/20)
DS_train, DS_test = train_test_split(DB_train, test_size = 0.2)
#validation data. *Keep in mind validation data is different from test data
DS_train, DS_val = train_test_split(DS_train, test_size = 0.1)

'''Separation of the Target/Class column and the characteristics/features is 
preparing the data to fit into the model. Models only take two inputs, array
of all the features and the target column. Target Column would usually be the
desired column to be predicted.'''
#Seperating "Target" column and combining feature data
DS_valid = DS_val.copy()
y_val= DS_valid.pop("Target")
X_val = np.array(DS_valid)

#Seperating "Target" column and combining feature data
DS_train_features = DS_train.copy()
y_train = DS_train_features.pop("Target")
X_train = np.array(DS_train_features)

#Seperating "Target" column and combining feature data
DS_test_features = DS_test.copy()
y_test = DS_test_features.pop("Target")
X_test = np.array(DS_test_features)

#GRU model
'''Due to GRU asking for specific shape of the data, need to modify the code to handle
the features'''
inputs = tf.keras.Input(shape=(X_train.shape[1],)) #Input layer
expand_dims = tf.expand_dims(inputs, axis=2)
gru = tf.keras.layers.GRU(64, return_sequences=True)(expand_dims) #Hidden layer
flatten = tf.keras.layers.Flatten()(gru)
#output is 5, but expecting 4. With the code it excludes the highest number.
#Reads the value as [0,5) not [0,5]
outputs = tf.keras.layers.Dense(5, activation='softmax')(flatten) #Output layer
model = tf.keras.Model(inputs = inputs, outputs = outputs)

'''sparse_categorical_crossentropy helped to increase acccuracy, but lead to
increasing the amount of neurons in the output layer. Maybe lack of understanding
on my part for what is required on the output layer other than output layer's neurons
are based on amount of desired predicted values'''
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

'''I assume this stops the whole thing if whatever is being monitored
stays the same for the amount of patience. So in this case, if the val_loss
is the same for 5 epochs then it stops. 
'''
history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    batch_size=32,
    epochs=50,
    validation_data =(X_val,y_val),
    callbacks=[  
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True
            )
        ]   
    )
#Tests accuracy for the model
model_acc = model.evaluate(X_test,  y_test, verbose=0)[1]
print("Test Accuracy {:.3f}%".format(model_acc*100))


