stack = []
max_size = 3

def is_empty():
    return len(stack) == 0

def is_full():
    return len(stack) == max_size

def push(item):
    if is_full():
        print("Stack is full")
    else:
        stack.append(item)

def pop():
    if is_empty():
        print("Stack is empty")
    else:
        return stack.pop()

push(10)
push(20)
push(30)
push(40)

print(pop())
print(pop())
print(pop())
print(pop())
