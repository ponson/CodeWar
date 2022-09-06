def order_weight(strng):
#parse string list to list of strings
    str_lst = strng.split()

#add every digit of the string
    digit_list = []
    for num in str_lst:
        sum = 0
        for i in num:
            sum += int(i)
        digit_list.append(sum)

#  create a specified bubble sort
    for idx in range(len(digit_list)):
        for round in range(len(digit_list) - idx - 1):
            if digit_list[round] > digit_list[round+1] or (digit_list[round] == digit_list[round+1] and str_lst[round] > str_lst[round+1]):
                temp_digit = digit_list[round]
                digit_list[round] = digit_list[round+1]
                digit_list[round+1] = temp_digit
                temp_str = str_lst[round]
                str_lst[round] = str_lst[round+1]
                str_lst[round+1] = temp_str

# combine into a string and return
    return " ".join(str_lst)


print(order_weight("103 123 4444 99 2000"))  # 2000 103 123 4444 99
# 11 11 2000 10003 22 123 1234000 44444444 9999
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
print(order_weight("1 2 3 4 5 5 6"))
print(order_weight(""))
