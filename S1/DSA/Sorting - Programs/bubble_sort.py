#bubble sort

arr = [13,25,83,272,82,825,8]

n = len(arr)

for i in range(n-1):
  for j in range(n-i-1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array:", arr)




