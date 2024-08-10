def check_palindrome(string):
    length = len(string)
    for i in range(0, len(string) // 2):

        if string[i] != string[length-1]:
            return False
        length = length - 1
    return True


# len(string) // 2 = 2
string = 'dam'  # madam
ispalindrome = check_palindrome(string)
print('ispalindrome: ', ispalindrome)
if ispalindrome == False:
    start = 0
    end = len(string) // 2
    length = len(string)
    print('start: ', start, ' end: ', end)
    while start != end:
        print('start: ', start)
        if string[start] != string[length-1]:
            string = string[length-1] + string
            print('==> ', string)
        length = length - 1
        start = start + 1
    print('Updated stirng: ', string)

    print('ispalindrome: ', check_palindrome(string))
