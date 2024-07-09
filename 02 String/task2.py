def strStr(haystack, needle):
    if not needle:
        return 0

    len_haystack = len(haystack)
    len_needle = len(needle)

    for i in range(len_haystack - len_needle + 1):
        if haystack[i:i + len_needle] == needle:
            return i

    return -1


haystack = "codemama"
needle = "ostad"
print(strStr(haystack, needle))
# Time Complexity: O(n⋅m)
# Space Complexity: O(1)
