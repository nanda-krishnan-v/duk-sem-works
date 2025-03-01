import array as arr

a= arr.array("i",[1,2,3])
print(a)

for i in range(0,3):
    print(a[i],end=" ")
    
print()

b = arr.array("d",[5.5,7.6,2.2])
for i in range(0,3):
    print(b[i],end=" ")