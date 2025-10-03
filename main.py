def new_append(numbers):
    new_list = []
    for number in numbers:
        if type(number) == int:
            new_list.append(number)
    print(sum(new_list))
print(new_append([1, 2, "13", "4", "645"]))
print(new_append([True, False, "123", "75"]))
print(new_append([1, 2, 3, 4, 5, True]))
def dublekate_list(itemas):

    delete_duplicate = set(itemas)
    new_list = list(delete_duplicate)



    delete_duplicate = set(itemas)
    new_list = list(delete_duplicate)


    delete_duplicate = set(itemas)
    new_list = list(delete_duplicate)
print(dublekate_list([1, 0, 1, 0]))
print(dublekate_list(["The", "big", "cat"]))
print(dublekate_list(["John", "Taylor", "John"]))