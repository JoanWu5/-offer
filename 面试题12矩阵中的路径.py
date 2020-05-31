class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        def helper(board,i,j,word,length):
            if length == len(word):
                return True
            if 0<=i<m and 0<=j<n:
                if board[i][j] ==word[length]:
                    board[i][j] = '#'
                    result = helper(board,i,j+1,word,length+1) or \
                    helper(board,i,j-1,word,length+1) or \
                    helper(board,i+1,j,word,length+1) or \
                    helper(board,i-1,j,word,length+1) 
                    board[i][j] = word[length]
                    return result
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(board,i,j,word,0):
                        return True
        return False

s = Solution()
print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"))


                