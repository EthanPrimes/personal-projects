from collections import Counter

def lengthOfLongestSubstring(s: str) -> int:
    def helper(s):
        if len(set(c for c in s)) == len(s):
            return len(s)
        s_chars = Counter(s)
        split_char = s_chars.most_common(1)[0][0]
        positions = [0] + [i for i, c in enumerate(s) if c == split_char] + [len(s)]
        print(positions)
        for elt in (
            s[i:j]
            for i, j in zip(positions[1:-2], positions[2:-1])
        ):
            print(elt)
        return max(
            helper(s[i:j])
            for i, j in zip(positions[1:-2], positions[2:-1])
        )

    return helper(s)

lengthOfLongestSubstring("eea")
