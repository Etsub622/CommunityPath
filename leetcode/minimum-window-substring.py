class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ''

        tes = Counter(t)
        window = {}
        l, count = 0, 0
        min_window = ""
        min_len = float("inf")

        for r in range(len(s)):
            if s[r] in t:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] <= tes[s[r]]:
                    count += 1

            while count == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r + 1]

                if s[l] in t:
                    window[s[l]] -= 1
                    if window[s[l]] < tes[s[l]]:
                        count -= 1

                l += 1

        return min_window
