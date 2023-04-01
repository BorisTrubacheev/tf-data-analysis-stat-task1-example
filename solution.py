import pandas as pd
import numpy as np


chat_id = 1736726957 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    normal = np.log(x-99)
    return np.exp(normal.mean()) # Ваш ответ
