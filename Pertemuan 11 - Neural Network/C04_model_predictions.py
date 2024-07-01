# lib neural network algorithms
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Bidirectional
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Dropout
from keras.layers import Dense
# ----------------------------------------------------------------------------------------

# func model predictions
def get_models(algorithm, timestep, dropout):

  # reset of session model
  tf.keras.backend.clear_session()

  # 1. The Neural Network Architecture
  if algorithm == "SBi-LSTM":
    model = Sequential()
    model.add(Bidirectional(LSTM(units=50, return_sequences=True, input_shape=(timestep, 1))))
    model.add(Bidirectional(LSTM(units=50, return_sequences=False)))
    model.add(Dropout(0.05))
    model.add(Dense(1))
  
  # 1. The Neural Network Architecture
  if algorithm == "SBi-GRU":
    model = Sequential()
    model.add(Bidirectional(GRU(units=50, return_sequences=True, input_shape=(timestep, 1))))
    model.add(Bidirectional(GRU(units=50, return_sequences=False)))
    model.add(Dropout(0.05))
    model.add(Dense(1))

  # 2. compile models
  model.compile(optimizer="adamax", loss="mae")

  # return values
  return model
# ----------------------------------------------------------------------------------------

# func model predictions
def get_predictions(model, x_train, y_train, x_test, y_test):
  
  # 3. fitting models
  history = model.fit(
    x_train, y_train,
    batch_size=16, epochs=50, verbose="auto", 
    validation_data=(x_test, y_test),
    use_multiprocessing=False, shuffle=False
  )

  # 4. predict models
  predictions = model.predict(x_test, verbose=0)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------