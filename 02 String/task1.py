def restoreString(s, indices):
    shuffled = [''] * len(s)
    for i, index in enumerate(indices):
        shuffled[index] = s[i]
    return ''.join(shuffled)


s = "abc"
indices = [1, 0, 2]
print(restoreString(s, indices))

# Time Complexity: O(len(s))
# Space Complexity: O(len(s))
