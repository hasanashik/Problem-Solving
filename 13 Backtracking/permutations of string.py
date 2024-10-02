def generate_permutation(A, taken, perm, result, n):
    if len(perm) == n:
        
        temp = ''
        for item in perm:
            temp = temp + item
        print('==> ',temp)
        result.append(temp)
        return
    
    for i in range(n):
        if not taken[i]:
            taken[i] = True
            perm.append(A[i])
            generate_permutation(A, taken, perm, result, n)
            perm.pop()
            taken[i] = False

def permute(A):
    result = []
    n = len(A)
    taken = [False] * n
    perm = []
    generate_permutation(A, taken, perm, result, n)
    return result

# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
A = 'abc'
print(permute(A))

# Time complexity: O(len(A)!)