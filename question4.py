#function that accepts a list of strings and returns a new list where each string is reversed

def string_list(list):
    i = 0
    while i < len(list):
        print(list[i][::-1])
        i += 1

string_list(list = ("apple", "banana", "cherry"))