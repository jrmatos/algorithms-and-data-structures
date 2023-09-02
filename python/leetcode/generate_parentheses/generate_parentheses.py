class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_parentheses = []
        self.DFS(n, 1, valid_parentheses,  "(")
        return valid_parentheses

    def DFS(self, n, open_count, valid_parentheses, current):
        if len(current) == n * 2: # leaf
            if open_count == 0:
                valid_parentheses.append(current)
            return
        
        self.DFS(n, open_count + 1, valid_parentheses, current + "(")
        if open_count > 0: # unbalanced
            self.DFS(n, open_count - 1, valid_parentheses, current + ")")
