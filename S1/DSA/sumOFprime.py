start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
sum = 0
for num in range(start, end + 1):
    if num > 1:
        flag = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            sum = sum + num
            print(num)
print(sum)