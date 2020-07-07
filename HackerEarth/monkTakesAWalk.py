vowels = ['a', 'e', 'i', 'o', 'u']


def countVowels(str):
    count = 0
    n = len(str)
    for i in range(n):
        if str[i].lower() in vowels:
            count += 1

    print(count)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        str = input()
        countVowels(str)
