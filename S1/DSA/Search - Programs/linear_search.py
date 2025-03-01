arr = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
target = 3
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print((True, i))
            return
    print("not found")

linear_search(arr,target)