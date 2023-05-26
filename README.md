# Car_price_prediction_with_xgboost

## Introduction
Price is one of the major factors that determines the sales of a product. Potential car owners search through various online sites to determine the price of cars before proceeding to car retailers or auctioners for car purchase. This car prediction model can reduce the time spent in decision making before purchase of cars in the Nigerian Market.
Economic benefits of the model:
* Enable potential car owners to determine car price before purchase without searching various sources
* enable car owners determine market value of cars by inputing the mileage, year, fuel type and other necessary details

## the dataset
The data was sourced from a public datas source, kaggle. 
features of the dataset

## Model parameter selection
The model parameters were estimated using the randomized search cv

## Model Quality
R squared score : 0.8317
RMSE: 1990991.03
mean Squared Error: 3964045308043.7

## cross-validation
On cross_validation, the model appears to be overfitted. This is not surprising since the dataset is not really large and have a tendency of overfitting. It is best to put it into production and track performance.

## recommendations
* Train model with a larger dataset
* Get a dataset that include the unique model of cars, such as Toyota Corolla and not just Toyota. This can be achieved by scraping data from online listings
* deploy, track and experiment model
