import re

# 1. Binary strings with odd length
pattern1 = r'^(0|1)((0|1)(0|1))*$'

print("1. Binary strings with odd length:")
test_cases1 = [
    ("0", True),      # length 1 (odd)
    ("1", True),      # length 1 (odd)
    ("01", False),    # length 2 (even)
    ("101", True),    # length 3 (odd)
    ("1010", False),  # length 4 (even)
    ("10101", True),  # length 5 (odd)
    ("", False),      # length 0 (even)
]

for string, expected in test_cases1:
    result = bool(re.match(pattern1, string))
    status = "✓" if result == expected else "✗"
    print(f"  {status} '{string}' -> {result} (expected {expected})")

print()

# 2. Lowercase English strings ending with 'b'
pattern2 = r'^[a-z]*b$'

print("2. Lowercase strings ending with 'b':")
test_cases2 = [
    ("b", True),
    ("ab", True),
    ("hello", False),
    ("web", True),
    ("abc", False),
    ("", False),
    ("testb", True),
    ("B", False),  # uppercase
]

for string, expected in test_cases2:
    result = bool(re.match(pattern2, string))
    status = "✓" if result == expected else "✗"
    print(f"  {status} '{string}' -> {result} (expected {expected})")

print()

# 3. Strings from {a,b} where each 'a' is preceded and followed by 'b'
pattern3 = r'^(b|bab)+$|^$'

print("3. Strings where each 'a' is surrounded by 'b':")
test_cases3 = [
    ("", True),       # empty (no 'a')
    ("b", True),      # only 'b'
    ("bb", True),     # only 'b's
    ("bab", True),    # 'a' surrounded by 'b'
    ("babb", True),   # 'a' surrounded, extra 'b'
    ("bbab", True),   # extra 'b', then 'a' surrounded
    ("bbabbb", True), # 'a' surrounded, extra 'b's
    ("babbab", True), # two 'a's, both surrounded (b-a-b + b-a-b with shared 'b')
    ("babbbab", True),# two 'a's with extra 'b's between
    ("a", False),     # 'a' not surrounded
    ("ab", False),    # 'a' not preceded
    ("ba", False),    # 'a' not followed
    ("aba", False),   # middle char is 'b', but 'a's not properly surrounded
    ("baab", False),  # second 'a' preceded by 'a', not 'b'
    ("abab", False),  # first 'a' not preceded by 'b'
    ("baba", False),  # last 'a' not followed by 'b'
    ("aa", False),    # 'a's adjacent
]

for string, expected in test_cases3:
    result = bool(re.match(pattern3, string))
    status = "✓" if result == expected else "✗"
    print(f"  {status} '{string}' -> {result} (expected {expected})")
