# 40.002 Data and Business Analytics 1D Project

## Project information

### Project background
Low volatility can be a very effective predictor for future returns in China A- shares market.  However, we have observed that we need to carefully understand and build a low volatility signal that is indicative of not only a stock’s current volatility, but also its future volatility. 

https://www.msci.com/www/blog-posts/how-the-low-volatility-factor/01132841955

### Project objectives
We would like to build a company-level predictive model for identifying stocks with low future volatility. We will look to combine company fundamental data (from the income statement and balance sheet) with trailing volatility and return information to build a better forecast for future volatility of a company.

Our company will provide all the data and sub-indicators in easily usable formats to facilitate the project. 

### Project deliverables

The students are required to deliver a predictive model generating a quantitative signal that is indicative of a company’s future volatility over the next 1 year.

## Approach
### Arima model

After moving out of the regression approach, we did an ACF analysis on the variance of all companies. The result of the ACF Plot showed that a company’s volatility is highly dependent on its previous values. Hence, we decided to build an ARIMA (Auto Regressive Integrated Moving Average) time series forecasting model
ARIMA is a forecasting algorithm that uses past values of the time series to predict the future values. The ARIMA model is able to take into account the lags of forecast errors between consecutive data and patterns in growth/decline in data, including the rate of the changes. This is achieved through the use of the autocorrelation function, which is easily controlled by differences, auto-regression and moving averages, without performing complicated transformations or using extra surrogate variables.

### Naive model
To compare the accuracy of the ARIMA model, we created a naive prediction model. This naive model set the future 12 months rolling standard deviation value to be the mean value of the previous 12 months value. Figure 5 shows the ARIMA and naive model forecast for one company. This can be seen for a single company in the plot for [company 9690](Results/company9690.jpeg)

### Results

In measuring the mean squared error of our naive model and ARIMA model, we found that the ARIMA model outperformed the naive model by 52%. In other words, the magnitiude of the errors by the ARIMA model were about half compared to the errors of the naive model. This shows that the model is <b>twice<b> as accurate as our naive model. This can be seen for a [sample of a few companies](Results/mean_squared_error.jpeg).

