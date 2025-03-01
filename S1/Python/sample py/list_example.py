#WAP to enter Name, marks of 5 subject and calculate total & percentage of student

name = input("Enter your name: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = (total / 500) * 100  

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")