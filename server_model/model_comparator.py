# model_comparator.py
from model import process, process2
from weight_used_model import plot_predictions
import shutil
import re

BEST_OUTPUT_PATH = "server/images/stock.png"

def extract_rmse_value(rmse_str):
    match = re.search(r"[-+]?\d*\.\d+|\d+", rmse_str)
    return float(match.group()) if match else float('inf')

# RMSE 차이가 20% 이상이면 커스텀 모델(model2) 을 선택
# 그 이하라면 기존 모델(model1)을 선택
# 그리고 선택된 모델의 그래프 이미지 저장(stock.png)
def compare_and_save_best(dataset):
    path1, rmse1, test1, pred1 = process(dataset)
    path2, rmse2, test2, pred2 = process2(dataset)


    # 0으로 나누는 경우 방지
    if rmse1 == 0:
        diff_ratio = float("inf")
    else:
        diff_ratio = abs(rmse2 - rmse1) / rmse1

    # 차이가 20% 이상이면 커스텀 모델(model2) 선택
    if diff_ratio >= 0.2:
        shutil.copy(path2, BEST_OUTPUT_PATH)
        best = "model2"
        plot_predictions(test2, pred2)
    else:
        shutil.copy(path1, BEST_OUTPUT_PATH)
        best = "model1"
        plot_predictions(test1, pred1)

    return best
