
def reverse(A: list):
    n = len(A)
    for i in range(n // 2):
        A[i], A[n-i-1] = A[n-i-1], A[i]


A = list(range(10))
print(A)
reverse(A)
print(A)
