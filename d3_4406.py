aeiou=['a', 'e', 'i', 'o', 'u']

TC=int(input())
for testcase in range(1, TC+1):
    st_in=input()
    new_str=''
    for char in st_in:
        if char not in aeiou:
            new_str+=char
    print('#{} {}'.format(testcase, new_str))