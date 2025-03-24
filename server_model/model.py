# model.py
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout
from keras.utils import plot_model
import os
import math
from sklearn.metrics import mean_squared_error
from config import DATA_PATH, MODEL_SAVE_PATH, MODEL_SAVE_PATH2, MODEL_PLOT_PATH, MODEL_SHAPES_PLOT_PATH, PREDICTION_PLOT_PATH

# 데이터 로딩
dataset = pd.read_csv(DATA_PATH, index_col='Date', parse_dates=['Date'], encoding='utf-8')


# 🚀 **추가된 `process()` 함수**
def process(dataset):
    """ 주어진 데이터셋으로 모델을 로드하고 예측을 수행 """
    model = load_model(MODEL_SAVE_PATH)

    # 'High' 열 선택
    training_set = dataset.loc[:'2022', ["High"]].values
    test_set = dataset.loc['2023':, ["High"]].values

    # 데이터 스케일링
    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(training_set)

    # 테스트 데이터 준비
    dataset_total = pd.concat([dataset.loc[:'2022', "High"], dataset.loc['2023':, "High"]], axis=0)
    inputs = dataset_total[len(dataset_total) - len(test_set) - 60:].values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)

    X_test = []
    for i in range(60, len(inputs)):
        X_test.append(inputs[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # 모델 예측
    predicted_stock_price = model.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    # 결과 시각화 및 평가
    result_visualizing = plot_predictions(test_set, predicted_stock_price)
    result_evaluating = return_rmse(test_set, predicted_stock_price)

    return result_visualizing, result_evaluating, test_set, predicted_stock_price


# 🚀 **추가된 `process()` 함수**
def process2(dataset):
    """ 주어진 데이터셋으로 모델을 로드하고 예측을 수행 """
    model = load_model(MODEL_SAVE_PATH2)

    # 'High' 열 선택
    training_set = dataset.loc[:'2022', ["High"]].values
    test_set = dataset.loc['2023':, ["High"]].values

    # 데이터 스케일링
    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(training_set)

    # 테스트 데이터 준비
    dataset_total = pd.concat([dataset.loc[:'2022', "High"], dataset.loc['2023':, "High"]], axis=0)
    inputs = dataset_total[len(dataset_total) - len(test_set) - 60:].values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)

    X_test = []
    for i in range(60, len(inputs)):
        X_test.append(inputs[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # 모델 예측
    predicted_stock_price = model.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    # 결과 시각화 및 평가
    result_visualizing = plot_predictions(test_set, predicted_stock_price)
    result_evaluating = return_rmse(test_set, predicted_stock_price)

    return result_visualizing, result_evaluating, test_set, predicted_stock_price



# 🚀 **추가된 `plot_predictions()` 및 `return_rmse()` 함수**
def plot_predictions(test, predicted):
    plt.clf()  # 이전 그래프 초기화
    plt.plot(test, color='red', label='Real IBM Stock Price')
    plt.plot(predicted, color='blue', label='Predicted IBM Stock Price')
    plt.title('IBM Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('IBM Stock Price')
    plt.legend()
    plt.savefig(PREDICTION_PLOT_PATH)
    return PREDICTION_PLOT_PATH

def return_rmse(test, predicted):
    rmse = math.sqrt(mean_squared_error(test, predicted))
    result_msg = f"The root mean squared error is {rmse}."
    print(result_msg)
    return result_msg
