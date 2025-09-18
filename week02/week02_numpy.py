import numpy as np

arr = np.arange(1,6)
print(arr)

# indexing
print(arr[2])
print(arr[4],arr[-1], arr[len(arr)-1])

# slicing
print(arr[1:3])
print(arr[::3])


#2d 배열
arr2d = np.array(
    [
        [
            [1.0, 2.0, 3.1],
            [4.2, 5.9, 9.1]
        ],
        [
            [1.1, 0.8, 2.1],
            [6.3, 1.9, 77.1]
        ],
        [3, 2, 1],
        [4, 5, 6],
        [14, -5, 76]

    ]
)
print(arr2d)
print(arr2d[1, 2])  # 6
print(arr2d[:, 1])  # [2  5 -5] 모든 행의 1열(0열~2열)