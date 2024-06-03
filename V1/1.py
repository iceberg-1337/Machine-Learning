import numpy as np


rand_arr = np.random.randint(1, 100, 30)
max = np.max(rand_arr)
rand_arr[4::5] = max


print(rand_arr)
print(max)