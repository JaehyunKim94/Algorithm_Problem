TC=int(input())

for testcase in range(1, TC+1):
    total_map=list()
    result=1
    for l in range(9):
        list_a=list(map(int, input().split()))
        total_map.append(list_a)
    
    for y in range(9):
        result_x=0
        result_y=0
        for x in range(9):
            result_x+=total_map[y][x]
            result_y+=total_map[x][y]
        if result_y!=45 or result_x!=45:
            result=0
            break
        
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            result_box=0
            for j in range(3):
                for i in range(3):
                    result_box+=total_map[y+j][x+i]

            if result_box!=45:
                result=0
                break
    print('#{} {}'.format(testcase, result))


            
