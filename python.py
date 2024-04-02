def string_matching(text, pattern):
    matches = []
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches

# Example usage:
text = "ababcababcabc"
pattern = "abc"
print("Indices where pattern occurs:", string_matching(text, pattern))

