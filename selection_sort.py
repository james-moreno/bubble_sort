from datetime import datetime
startTime = datetime.now()


def sorter(arr):
    for x in range(len(arr)-1, 0, -1):
        for i in range(x):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp


a = [26, 87, 14, 30, 54, 61, 82, 76, 57, 78, 99, 91, 30, 38, 70, 21, 93, 39, 96, 31, 33, 15, 44, 15, 15, 12, 49, 62, 0, 23, 22, 49, 55, 41, 0, 1, 28, 90, 22, 41, 60, 88, 25, 99, 1, 0, 44, 63, 84, 70, 67, 25, 19, 90, 56, 26, 92, 24, 56, 21, 98, 7, 25, 25, 98, 29, 8, 31, 8, 78, 10, 53, 86, 60, 44, 12, 56, 98, 9, 39, 97, 48, 12, 74, 4, 99, 34, 25, 34, 63, 53, 22, 18, 61, 28, 1, 78, 10, 99, 76]

sorter(a)
print(a)

print(datetime.now() - startTime)
