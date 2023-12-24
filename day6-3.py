numbers=[10, 501, 22, 37, 100, 999, 87, 351]
def is_happy(num):
    seen=set()
    if num is seen:
        return False
    seen.add(num)
#return True

happy_count=0

for num in numbers:
    if is_happy(num):
        happy_count+=1
print("The number of happy number in the given list is:", happy_count)        