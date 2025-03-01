import array as arr

a= arr.array("i",[1,2,3])
print(a)

print("Before pop")
for i in range(0,3):
    print(a[i],end=" ")
    
print()

# b = arr.array("d",[5.5,7.6,2.2])
# for i in range(0,3):
#     print(b[i],end=" ")

print("After pop")

a.pop(2)
for i in range(0,2):
    print(a[i],end=" ")
print()

print("Before remove")
for i in range(0,2):
    print(a[i],end=" ")
print()
print("After remove")

a.remove(1)
for i in range(0,1):
    print(a[i],end=" ")
    
print()