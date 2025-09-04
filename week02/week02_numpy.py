import numpy as np

zeros = np.zeros((3,4))
# zeros = np.array([[0, 0,0,0],[0, 0,0,0],[0, 0,0,0]], dtype=float)
ones = np.ones((3,5))
print(zeros)
print(ones)

# range_array = np.arange(0,20,2)
range_array = np.arange(1,10)
print(range_array)

space_array = np.linspace(0,1,5) # 0부터 1까지 5개로 구간 설정
print(space_array)