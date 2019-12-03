import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from initialise_dataset import create_coy_dataset, china_stocks_large, full_data_coy

# Use ARIMA Model
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

coy = pd.read_csv('full_data_companies/testing_without_cheating/coy_12697.csv')
coy = coy.fillna(method='ffill')
rolling_devs = coy.rolling_std.values[12:]
train, test = rolling_devs[0:180], rolling_devs[180:len(rolling_devs)]
history = [x for x in rolling_devs]

predictions = []
for t in range(12):
    model = ARIMA(history, order=(3, 0, 1))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)