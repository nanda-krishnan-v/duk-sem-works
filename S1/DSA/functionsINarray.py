import array as arr

a= arr.array("i",[1,2,3])
for i in range(0,3):
    print(a[i],end=" ")
print()

# b = arr.array("d",[5.5,7.6,2.2])
# for i in range(0,3):
#     print(b[i],end=" ")
print()  


print("Before insertion:")

for i in range(0,3):
    print(a[i],end=" ")
print()

print("After insertion:")
#insert Function
a.insert(4,4)
for i in a:
  print(i,end=" ")
print()

print("Before Append:")
for i in a:
  print(i,end=" ")
print()

print("After Append:")
#append Function
a.append(5)
for i in a:
  print(i,end=" ")