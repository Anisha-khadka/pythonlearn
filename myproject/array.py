# import numpy as np
# print(np.__version__)

# # arrr=np.array([1,2,3,4])
# # print(arrr)

# # 0-D array
# arr0=np.array(22)
# print(arr0)

# # 1-D array
# arr1=np.array([1,2,3,4,5])
# print(arr1)

# # 2-D array
# arr2=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr2)

# # 3-D array
# arr3=np.array([[[1,2,3,4],[4,5,6,7]],[[1,2,3,4],[4,5,6,7]]])

# print(arr3)
# print(arr3.ndim)

# # multiple dimention
# arrn=np.array([1,2,3,4],ndmin=5)
# print(arrn)

# import pandas as pd
# dict={
#     'names':["Anisha","Ashish","Ramesh","Deena"],
#     'ages':[22,23,30,21]
# }
# mydict=pd.DataFrame(dict)
# print(mydict)

# from scipy import constants
# print(constants.litre)
# print(constants.pi)
# print(dir(constants))

import matplotlib.pyplot as plt
import numpy as np
x=np.random.uniform(0,5,250)
print(x)
plt.hist(x,5)
plt.show()