class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        # max_len = max(len(word) for word in words)
        max_len=0
        for word in words:
            if len(word)>max_len:
                max_len=len(word)

        output = []
        for i in range(max_len):
            column = ''
            for word in words:
                if i < len(word):
                    column += word[i]
                else:
                    column += ' '
            output.append(column.rstrip())

        return output
        