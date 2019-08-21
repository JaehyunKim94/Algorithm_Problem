# num_lst=['00', '01', '10', '11']
# TC=int(input())
# for testcase in range(1, TC+1):
#     num_cnt=list(map(int, input().split()))
    
#     new_str=''

#     # 암호의 개수 구하기
#     num_len=0
#     stt_index=0
#     for i in range(4):
#         num_len+=num_cnt[i]
#         if num_cnt[i] > num_cnt[stt_index]:
#             stt_index=i

#     new_str+=num_lst[i]
#     num_cnt[i]-=1
#     new_num=''
#     while True:    
#         if len(new_num)==0:     # 처음 수 적용
#             new_num=new_str
#         if new_num[1]=='0':     # 두번째 자리가 0일 경우
#             chek_cnt=0
#             for cnt in num_cnt[:2:]:    # 첫째자리가 0인 index 0과 1에 대해 cnt를 합쳐서
#                 chek_cnt+=cnt
#             if chek_cnt==0:             # 0일 경우 불가능하기 때문에 break
#                 stp_chk=1
#                 break
#             else:


#         elif new_num[1]=='1':
#             chek_cnt=0
#             for cnt in num_cnt[2::]:
#                 chek_cnt+=cnt
#             if chek_cnt==0:
#                 stp_chk=1
#                 break
                