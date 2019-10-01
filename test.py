mag_lst = [1, 2, 3, 4, 5, 6, 7, 8]
rm = mag_lst[7]
# for n in range(8):
#     mag_lst[n-1] = mag_lst[n]
# mag_lst[6] = rm
# print(mag_lst)

new_lst = mag_lst[1:]
new_lst.append(mag_lst[0])
print(new_lst)