def sum_first_and_last_digit(num):
    num_str=str(num)
    first_digit=int(num_str[0])
    last_digit= int(num_str[-1])
    sum_digits=first_digit+last_digit

    num=123456789
    result=sum_first_and_last_digit(num)
    print("The sum of the first and last digit of", num, "is:", result)