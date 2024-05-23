import pandas as pd
import numpy as np
import scipy.stats as sps


chat_id = 334982039 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02

    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_var = np.var(x)
    y_var = np.var(y)

    std = np.sqrt(x_var / x.size + y_var / y.size)
    z_stat = sps.norm.ppf(1-alpha)
    return y_mean - x_mean > std * z_stat # Ваш ответ, True или False
