"""
Provides some arithmetic functions
"""
from typing import Any

import numpy as np

def pearson_correlation(x, y):
    n = len(x)

    sum_y = np.sum(y)
    sum_x = np.sum(x)

    sum_x_squared = np.sum(np.square(x))
    sum_y_squared = np.sum(np.square(y))

    product_sum = np.sum(np.multiply(x, y))

    num = n*product_sum-sum_x*sum_y
    denominator = np.sqrt((n * sum_x_squared - np.square(sum_x)) * (n * sum_y_squared - np.square(sum_y)))

    return num / denominator


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])

correlation = pearson_correlation(x, y)
print(correlation)
