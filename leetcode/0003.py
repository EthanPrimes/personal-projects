# Attempt 1 - didn't work

from collections import Counter

def lengthOfLongestSubstring(s: str) -> int:
    def helper(s):
        if len(set(c for c in s)) == len(s):
            return len(s)
        s_chars = Counter(s)
        split_char = s_chars.most_common(1)[0][0]
        positions = [i for i, c in enumerate(s) if c == split_char]
        sub_strings = []
        for i, p in enumerate(positions):
            sub_string = []
            if not i:
                sub_string.append(0)
            else:
                sub_string.append(positions[i - 1])
            if i == len(positions) - 1:
                sub_string.append(len(s) - 1)
            else:
                sub_string.append(positions[i + 1])
            sub_strings.append(sub_string)

        print(positions)
        print(sub_strings)
        return max(
            helper(s[i:j])
            for i, j in sub_strings
        )

    return helper(s)

lengthOfLongestSubstring("eea")

# Attempt 2 - worked, but too slow
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(c for c in s)):
            return len(s)
        # Sliding window technique
        i = j = 0
        max_length = 0
        char_counts = Counter(s[0])
        max_chars = char_counts.most_common(1)[0][1]
        while (j < len(s) - 1 or max_chars > 1):
            # Update pointers
            if max_chars > 1:
                char_counts[s[i]] -= 1
                i += 1
            else:
                j += 1
                char_counts[s[j]] += 1

            max_chars = char_counts.most_common(1)[0][1]

            # Update max length
            if max_chars < 2:
                max_length = max(max_length, j - i + 1)

        return max_length


# Attempt 3 - Still slow, but fast enough
from time import perf_counter as pc

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == len(set(c for c in s)):
        return len(s)
    # Sliding window technique
    i = j = 0
    max_length = 0
    chars = set(s[0])
    while j < len(s) - 1:
        # Update pointers
        j += 1
        if s[j] in chars:
            sub_string = s[:j]
            new_i = sub_string.rfind(s[j]) + 1
            chars -= set(sub_string[i:new_i-1])
            i = new_i
        else:
            chars.add(s[j])

        # Update max length
        max_length = max(max_length, j - i + 1)

    return max_length

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "

# s = "eea"
# s = "abcabcbb"
# s = "pwwkew"

N = 100
times = []
for _ in range(N):
    start = pc()
    length = lengthOfLongestSubstring(s)
    times.append(pc() - start)

print(f"Result: {length}")
print(f"Average walltime: {sum(times) / N}")
