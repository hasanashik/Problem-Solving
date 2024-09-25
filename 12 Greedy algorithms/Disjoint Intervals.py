# https://www.interviewbit.com/problems/disjoint-intervals/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A, key=lambda x: x[1],reverse=False )
        checking_item = A[0]
        count = 1 # First sorted one default added
        for i in range(1,len(A)):
            if A[i][0] > checking_item[1]:
                count = count + 1
                checking_item = A[i]
        return count

# Time complexity: O(length of A)
# Space complexity: O(1)