def palindrome(str):
    start = 0
    end = len(str)-1

    while(start < end):
        if str[start] != str[end]:
            return 'NO'
        start += 1
        end -= 1

    if start == end:
        return 'YES ODD'

    else:
        return 'YES EVEN'


t = int(input())

for i in range(t):
    str = input()
    print(palindrome(str))
