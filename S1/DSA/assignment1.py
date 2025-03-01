import array as arr

marks = arr.array('i',[])

print("Enter marks for 10 students:")
for i in range(0,9):
    mark = int(input("Enter mark: "))  
    marks.append(mark) 
    
for i in range(0,9):
    print(marks[i],end=" ")

print("\nMarks and how many students got them:")
for i in range(len(marks)):
    mark = marks[i]
    count = 0
    for j in range(len(marks)):
        if marks[j] == mark:
            count += 1
    if i == marks.index(mark):
        if count > 1:
            print(f"{count} students got {mark} mark")
            
n= int(input("Enter the item to be searched:   "))

count = 0
for i in range(0,9):
    if marks[i] == n:
        print(f"the {n} is found at {i}th postition")
        count = 1
        break
  
if count == 0:
    print("Item not found")