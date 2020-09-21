from collections import defaultdict
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)

for word in a:
    anagrams["".join(sorted(word))].append(word)

print(anagrams.values())