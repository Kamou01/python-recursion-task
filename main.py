# recursion task for fibonacci sequence
# function for the 20th fibonacci number

# defining "n"
def fib(n):
    # check if n equals 0 or 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print fib(n)
for n in range(20):
    print(fib(n), end=" ")
