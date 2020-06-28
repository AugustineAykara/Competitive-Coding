def sortString(x):
    return (dictionary[x])

t = int(input())

for _ in range(t):
    p = input()
    s = input()

    dictionary = {}
    for index, letter in enumerate(p):
        dictionary[letter] = index

    res = sorted(s, key = sortString)
    print(''.join(res))
