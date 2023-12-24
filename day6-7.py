def first_non_repeating(list):
    count_dict={}
    for num in list:
        count_dict[num]=count_dict.get(num,0)+1
        if count_dict[num]==1:
            return num
        else:
            return None