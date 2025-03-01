n = int(input("Enter the maximum number for the Fibonacci series: "))
a = 0
b = 1

print("Fibonacci series up to", n, "is:")
while a <= n:
    print(a, end=' ')
    next_number = a + b
    a = b
    b = next_number