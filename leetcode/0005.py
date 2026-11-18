# Attempt 1 - Success, but slow
def longestPalindrome(s: str) -> str:
    N = len(s)
    max_len = 0
    max_pal = ""
    for i in range(N):
        for j in range(i, N):
            if s[i:j+1] == s[i:j+1][::-1] and j - i + 1 > max_len:
                max_len = j - i + 1
                max_pal = s[i:j+1]

    return max_pal

# s = "babad"
s = "cbbd"
print(longestPalindrome(s))

# Attempt 2
