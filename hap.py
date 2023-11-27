from scipy.optimize import minimize
import numpy as np

func = lambda x: np.exp(-1/(x[0]**2)) - (np.exp(-1/(x[1]**2)) * (1 - (2/(x[1]**2)) +(2*x[0]/(x[1]**3))))

x0 = np.array([0, 1])
bounds = [(0, 1), (0, 1)]
min_val = minimize(func, x0, bounds=bounds).fun
max_val = minimize(lambda x: -func(x), x0, bounds=bounds).fun

print(min_val, max_val)