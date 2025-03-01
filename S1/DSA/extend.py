#extend function 
import array as arr

a=[1,2,3,4,5,6,7,8]

print("Before Extend")
for i in range(0,7):
    print(a[i],end=" ")
print()

a.extend([9,10])
print()
print("After Extend")
for i in range(0,9):
    print(a[i],end=" ")