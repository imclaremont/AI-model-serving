# 주식 데이터를 기반으로 학습한 LSTM 모델 사용 "주가 예측 시스템"

최근 데이터(2018년-2024년)를 가상으로 증강하여 추가하고, 이 데이터를 이용해 2023년 데이터를 예측

데이터의 분포와 특성 변화로 인해 기존 모델의 성능 하락이 예상되며, 성능 저하 발생 시 다른 모델로 전환하는 MLOps 시스템을 구성


## 데이터 구성
- 원본 데이터: IBM 주식 데이터 (2006년-2017년)

- 증강 데이터: 6년 추가 (2018년-2024년)

주요 특성: Open(시가), High(고가)

예측 기간: 2023년

<증강된 최종 데이터>

<img width="700" alt="Image" src="https://github.com/user-attachments/assets/eefa81d8-3ce3-4ac7-9f70-f7affade0697"/>

## 모델 성능 평가 결과
<b>[기존 LSTM 모델]</b>

RMSE = 10.352

특징) 증강된 데이터에 대해서는 추세를 따라가지 못하고 예측 성능 저하 발생

<b>[새롭게 재학습된 LSTM 모델]</b>
	
RMSE = 3.953

특징) 재학습을 통해 변경된 데이터 분포를 반영하여 성능이 크게 향상

<img width="700" alt="Image" src="https://github.com/user-attachments/assets/abc0de84-934b-4626-9e79-4c1d3148df06"/>

## MLOps flow 전/후
1.	기존 Flow
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/510f4b0b-fa8d-4497-ac6d-26f11f8400ea" />

2. 수정된 Flow
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/414a7d5c-8100-493b-ad5f-fbd01555d6d7" />

## 최종 UI
<img width="500" alt="image" src="https://github.com/user-attachments/assets/a6aa63cf-24b3-489c-8802-18065b19ff75" />

<img width="500" alt="image" src="https://github.com/user-attachments/assets/6fcc0fed-fe59-4adf-af7e-2dba78c3e1ca" />

## 느낀 점
기존 데이터를 기반으로 학습된 모델은 데이터 변화에 민감하며, 새로운 데이터 분포를 반영하지 못할 경우 성능이 크게 저하될 수 있다. 따라서 데이터 드리프트가 예상될 경우 지속적으로 모델을 모니터링하고, 성능 저하 시 자동으로 신규 학습 모델로 대체하는 MLOps 시스템 구축은 필수적이다. 본 프로젝트의 결과로 RMSE 성능이 약 62% 개선된 것을 통해 데이터 변화에 맞춘 재학습이 중요함을 확인하였다!

## 실행 커맨드
poetry run uvicorn main:app --host 0.0.0.0 --port 8001 --reload
