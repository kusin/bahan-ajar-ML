# libs manipulations array
import numpy as np

# lib evaluate models
from math import sqrt
import scipy.stats as sc
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

# func evaluate models
def evaluate_models(y_test, predictions):

  # calculate mae, rmse, mape
  r = sc.mstats.pearsonr(y_test, predictions)[0]
  p_value = sc.mstats.pearsonr(y_test, predictions)[1]
  mae = mean_absolute_error(y_test, predictions)
  rmse = sqrt(mean_squared_error(y_test, predictions))
  mape = mean_absolute_percentage_error(y_test, predictions)
  
  # return values
  return np.round(r,4), np.round(p_value,4), np.round(mae,4), np.round(rmse,4), np.round(mape,4)