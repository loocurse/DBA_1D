import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from initialise_dataset import create_coy_dataset, china_stocks_large, full_data_coy
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


# Use ARIMA Model
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error


def acf(company_number,lag=1):
    coy = create_coy_dataset(company_number)
    coy = coy.fillna(method='ffill')
    rolling_devs = coy.rolling_std
    return rolling_devs.autocorr(lag=lag)


def predict_volatility(company_number, print_predictions=False, print_error=False, print_graph=False):
    # Split data
    coy = create_coy_dataset(company_number)
    coy = coy.fillna(method='ffill')
    rolling_devs = coy.rolling_std.values[12:]
    train, test = rolling_devs[0:200], rolling_devs[200:len(rolling_devs)]

    # Create model
    history = [x for x in train]
    predictions = [np.NaN for x in train]
    MSE_anal = []

    # Naive model
    naive = naive_model(train,10)


    for t in range(len(test)):
        model = ARIMA(history, order=(3, 0, 1))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        MSE_anal.append(yhat)
        obs = test[t]
        history.append(yhat)
        if print_predictions:
            print('predicted=%f, expected=%f' % (yhat, obs))

    if print_error:
        error = mean_squared_error(MSE_anal, test)
        error_naive = mean_squared_error(naive[-10:],test)
        print(f"The mean squared error is {error} for Cxrf {company_number}")
        return error, error_naive

    if print_graph:
        scope = -30
        plt.figure(figsize=(12, 5), dpi=100)
        plt.plot(rolling_devs[scope:], color='black', label='actual')
        plt.plot(predictions[scope:], color='red',label='forecasted')
        plt.plot(naive[scope:], color='blue',label='naive')
        plt.title('Forecast vs Actuals')
        plt.legend(loc='upper left', fontsize=8)
        plt.show()


# predict_volatility(9690, print_graph=True)


def naive_model(train, len):
    rep = [np.NaN for x in train]
    mean = np.mean(train[-12:])
    rep.extend([mean for x in range(len)])
    return rep

error_1, error_2 = (list(), list())


for idx, company in enumerate(full_data_coy):
    try:
        x,y = predict_volatility(company,print_error=True)
        error_1.append(x)
        error_2.append(y)
    except:
        error_1.append(np.NaN)
        error_2.append(np.NaN)


mse = pd.DataFrame([full_data_coy,error_1,error_2])


