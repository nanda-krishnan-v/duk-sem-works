#Slicing of an Array
import array as arr
l = [1,2,3,4,5,6,7,8,9,10]

a = arr.array("i",l)
print(a[3:8],end="  \n")
print(a[3:],end="  \n")
print(a[::-1],end="  \n")
print(a[:-1],end="  \n")
print(a[:],end="  \n")
print(a[:-1],end="  \n")
print(a[-1:3],end="  \n")