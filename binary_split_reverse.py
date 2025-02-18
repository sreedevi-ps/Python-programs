
def bin_split(input_no):
    bi_num=format(input_no,'08b')
    first_half=bi_num[:4]
    second_half=bi_num[4:]
    new_bi=second_half+first_half
    dec_no=int(new_bi,2)
    return dec_no


input_no=int(input())
k=bin_split(input_no)
print(k)