
import os

# 기본 경로 설정 (환경 변수에서 가져오거나 기본값 사용)
# BASE_DIR = os.getenv("BASE_DIR", "/Users/phoenix/Eagle/2025_FastAPI/service_model/model_serving/server")
BASE_DIR = os.getenv(
    "BASE_DIR", 
    "C/Users/hadongheon/Desktop/SKALA 1기/데이터분석 및 MLOps/ozo/server"
)


# 상대 경로를 연결할 때 슬래시(/) 제거
UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
MODEL_DIR = os.path.join(BASE_DIR, "model")
IMAGE_DIR = os.path.join(BASE_DIR, "view-model-architecture")
MODEL_IMG_DIR = os.path.join(BASE_DIR, "model-images")

# 파일 경로 설정
DATA_PATH = os.path.join(UPLOAD_DIR, "IBM_final.csv")
MODEL_SAVE_PATH = os.path.join(MODEL_DIR, "stock_lstm_model_nogpu.keras")
MODEL_SAVE_PATH2 = os.path.join(MODEL_DIR, "lstm_model_type_2.keras")
#MODEL_SAVE_PATH = "C:/Users/Administrator/Documents/my_project/skala/model_serving_rpt/model_serving_rpt/server/model/stock_lstm_model_nogpu.keras"
MODEL_PLOT_PATH = os.path.join(IMAGE_DIR, "model.png")
MODEL_SHAPES_PLOT_PATH = os.path.join(IMAGE_DIR, "shapes/model_shapes.png")
PREDICTION_PLOT_PATH = os.path.join(IMAGE_DIR, "stock.png")
