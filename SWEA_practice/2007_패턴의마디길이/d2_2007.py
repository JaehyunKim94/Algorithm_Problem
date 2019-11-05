TC= int(input())

for testcase in range(1, TC+1):
    original=input()
    new_str=''

    for i in range(len(original)):
        new_str+=original[i]
        ob=i+1
        check_str=''
        for j in range(ob, ob+len(new_str)):
            check_str+=original[j]
        if new_str==check_str:
            break
    print('#{} {}'.format(testcase, len(new_str)))
