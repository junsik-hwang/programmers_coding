# leetcode 937. Reorder Log File

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

# 문자 로그와 숫자 로그 판별하기
numbers = []
strings = []

for log in logs:
    if(log.split()[1].isdigit()):
        numbers.append(log)
    else:
        strings.append(log)

strings.sort(key=lambda x : (x.split()[1:], x.split()[0]))

print(strings + numbers)