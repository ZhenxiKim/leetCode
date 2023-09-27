import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    order = sys.stdin.readline().rstrip()
    list_a = order.split()
    num = 0
    if len(order.split()) > 1:
        num = list_a[1]
        order = list_a[0]
    num = int(num)

    if order == 'push':
        stack.append(num)
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
