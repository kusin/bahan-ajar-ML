# lib neural network algorithms
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Bidirectional
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Dropout
from keras.layers import Dense


# func model predictions
def get_models(algorithms, timestep):
  
  # 1. SBi-LSTM-RNN architecture
  if algorithms == "SBi-LSTM-RNN":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=True, input_shape=(timestep.shape[1], 1))),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=False)),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Dense(1)
    ])
  
  # 1. SBi-GRU-RNN architecture
  if algorithms == "SBi-GRU-RNN":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=True, input_shape=(timestep, 1))),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=False)),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Dense(1)
    ])
  
  # 2. compile models
  model.compile(optimizer="adamax", loss="mean_squared_error")
  
  # return values
  return model
# ----------------------------------------------------------------------------------------

# func model predictions
def get_predictions(model, x_train, y_train, x_test, y_test):
  
  # 3. fitting models
  history = model.fit(
    x_train, y_train,
    batch_size=16, epochs=50, verbose=0, 
    validation_data=(x_test, y_test),
    use_multiprocessing=False, shuffle=False
  )

  # 4. predict models
  predictions = model.predict(x_test, verbose=0)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------