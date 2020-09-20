# leetcode 819. Most Common Word

paragraph = "Bob hit a ball, the hit Ball flew far after it was hit"
banned = ["hit"]

import collections
import re

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
counts = collections.Counter(words)

print(counts.most_common(1)[0][0])
