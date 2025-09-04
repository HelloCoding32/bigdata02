# Numpy
# 써드파티 라이브러리 (별도의 설치가 필요, 단 colab에 기본 설치가 되어 있음.)
# 파이썬에서 수치 계산을 위한 핵심 라이브러리, 다차원 배열 객체와 이를 다루기 위한 다양한 함수를 제공

import numpy as np

# 리스트 대신 배열을 사용하는 이유
list1 = [1,2,"3",4,5]
arr1 = np.array(list1) # 파이썬 리스트를 넘파이 배열로 변환
print(list1, type(list1))
print(arr1, type(arr1))

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2, type(arr2))