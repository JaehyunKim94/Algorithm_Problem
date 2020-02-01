TC=int(input())

for testcase in range(1, TC+1):
    money=int(input())
    cnt_dict={
        50000:0,
        10000:0,
        5000:0,
        1000:0,
        500:0,
        100:0,
        50:0,
        10:0
    }

    result=''

    if money>=50000:
        cnt_mon=money//50000
        cnt_dict.update({50000:cnt_mon})
        money=money%50000

    if money>=10000:
        cnt_mon=money//10000
        cnt_dict.update({10000:cnt_mon})
        money=money%10000

    if money>=5000:
        cnt_mon=money//5000
        cnt_dict.update({5000:cnt_mon})
        money=money%5000

    if money>=1000:
        cnt_mon=money//1000
        cnt_dict.update({1000:cnt_mon})
        money=money%1000

    if money>=500:
        cnt_mon=money//500
        cnt_dict.update({500:cnt_mon})
        money=money%500

    if money>=100:
        cnt_mon=money//100
        cnt_dict.update({100:cnt_mon})
        money=money%100

    if money>=50:
        cnt_mon=money//50
        cnt_dict.update({50:cnt_mon})
        money=money%50

    if money>=10:
        cnt_mon=money//10
        cnt_dict.update({10:cnt_mon})
        money=money%10

    for v in cnt_dict.values():
        result+=str(v)
        result+=' '
    print('#{}'.format(testcase))
    print('{}'.format(result))


