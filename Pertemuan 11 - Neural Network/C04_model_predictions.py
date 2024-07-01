# libs manipulations array
import numpy as np

# lib neural network algorithms
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import Bidirectional

# lib boosting algorithm
from xgboost import XGBRegressor
# ----------------------------------------------------------------------------------------

# func model predictions
def get_models(algorithm, timestep, activation, dropout, optimizer):

  # reset of session model
  tf.keras.backend.clear_session()

  # 1. The Neural Network Architecture
  if algorithm == "SBi-LSTM":
    model = Sequential()
    model.add(Bidirectional(LSTM(units=50, activation=activation, return_sequences=True, input_shape=(timestep, 1))))
    model.add(Bidirectional(LSTM(units=50, activation=activation, return_sequences=False)))
    model.add(Dropout(dropout))
    model.add(Dense(1))
  
  # 1. The Neural Network Architecture
  if algorithm == "SBi-GRU":
    model = Sequential()
    model.add(Bidirectional(GRU(units=50, activation=activation, return_sequences=True, input_shape=(timestep, 1))))
    model.add(Bidirectional(GRU(units=50, activation=activation, return_sequences=False)))
    model.add(Dropout(dropout))
    model.add(Dense(1))

  # 2. compile models
  model.compile(optimizer=optimizer, loss="mae")

  # return values
  return model
# ----------------------------------------------------------------------------------------


# func model predictions
def get_predictions(model, x_train, y_train, x_test, y_test, batch_size, epochs):
  
  # 4. fitting models
  history = model.fit(
    x_train, y_train,
    batch_size=batch_size, epochs=epochs, verbose=0, 
    validation_data=(x_test, y_test),
    use_multiprocessing=False, shuffle=False
  )

  # 3. predict models
  predictions = model.predict(x_test, verbose=0)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------

# func model predictions
def get_XGBoost(xtrue, ytrue, ypred):

  # 1. calculate residuals
  residuals = ytrue - ypred[:, 0]

  # 2. xgboost model on residuals
  xgb_model = XGBRegressor(objective='reg:squarederror')

  # 3. fitting models
  xgb_model.fit(np.vstack(xtrue), residuals)

  # 4. predict models
  predictions = xgb_model.predict(np.vstack(xtrue))

  # 5. Combine LSTM and XGBoost predictions
  xgb_predictions = ypred[:, 0] + predictions

  return xgb_predictions

