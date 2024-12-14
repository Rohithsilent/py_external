import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

arr =np.array([1,2,3,4,5,6,7,8,9,10])
square=np.square(arr)

t_test,p_value = stats.ttest_1samp(arr,3)
print(f'array:{arr}')
print(f'square:{square}')
print(f't_test:{t_test}')
print(f'p_value:{p_value}')

plt.plot(arr,square)
plt.title('square')
plt.show()