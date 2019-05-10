class Solution(object):
    def transpose(self, A):
        m = len(A)
        n = len(A[0])
        trans = [[0 for x in range(m)] for x in range(n)]
        y = len(trans)
        for i in range(y):
            o = len(trans[i])
            for j in range(o):
                trans[i][j] = A[j][i]
        return trans
                
            
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
