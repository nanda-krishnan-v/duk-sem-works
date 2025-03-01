#searching of an element
import array as arr

l = [1,2,3,4,5,6,7,8,9,10]

a = arr.array("i",l)
print(a)
print("The occurrence of 1 is at:",a.index(1))
print("The occurrence of 5 is at:",a.index(5))
print("The occurrence of 10 is at:",a.index(10))