import pandas as pd
import numpy as np
import tensorflow as tf
from Genome.Simulation.World import simulate_model
import datetime
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.models import load_model

def create_input(data):
    dota = []
    labels = []
    for index, row in data.iterrows():
        dota.append([row["Price"], row["HighR"], row["LowR"], row["VolumeR"], row["Avg10"], row["Avg20"], row["Avg30"]])
        if index > 0:
            if dota[index][0] > dota[index - 1][0]:
                labels.append(1)
            else:
                labels.append(0)
    del dota[-1]
    return dota, labels


# physical_devices = tf.config.experimental.list_physical_devices('GPU')
# print("Nump GPUs Avaible: ", len(physical_devices))
# tf.config.experimental.set_memory_growth(physical_devices[0], True)


data = pd.read_csv (r'./Data/BTC_daily.csv')
# labels = pd.read_csv (r'./Data/BTC_daily_labels.csv')

data, labels = create_input(data)

# model = Sequential([
#     Dense(16, input_shape=(7, ), activation='relu'),
#     Dense(32, activation='relu'),
#     Dense(64, activation='relu'),
#     Dense(2, activation='softmax'),
# ])
#
# model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
# model.fit(x=data, y=labels, batch_size=1, epochs=100, shuffle=True, verbose=2)
#
# model.save('THEMODEL')

model = load_model('THEMODEL')

simulate_model(model, datetime.datetime.strptime("16/09/2017", "%d/%m/%Y"), datetime.datetime.strptime("14/12/2020", "%d/%m/%Y"), 500)



