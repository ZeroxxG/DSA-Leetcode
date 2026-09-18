n = 6

def fun(n):
    if n == 1:
        return 1
    ans = fun(n-1)
    return ans + n

# def fun(n):
#     if n == 0:
#         return 0
#     return fun(n-1) + n

print(fun(n))


