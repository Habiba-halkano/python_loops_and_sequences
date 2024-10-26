#function that takes a list as input and returns a new list with all duplicate items removed

def remove_duplicates(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    # new_list = list(dict.fromkeys(my_list))
    print(new_list)

remove_duplicates(my_list = [1, 2, 3, 3, 3, 4, 4 ,5 ,5])
