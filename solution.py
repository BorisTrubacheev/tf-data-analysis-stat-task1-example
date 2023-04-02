import pandas as pd
import numpy as np


chat_id = 1736726957 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    E = np.mean(x)
    D = np.var(x)
    return np.log(E/(np.sqrt(D/E**2 + 1))) # Ваш ответ
