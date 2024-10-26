#function that takes a list of tuples as input where each tuple takes a string and an int. The function should return a dictionary where the strins are keys
#and integers are values

def convert_list(tuples):
    result_dict = {}
    for key, value in tuples:
        result_dict[key] = value
    print (result_dict)

convert_list(tuples = [('apple', 3), ('banana', 5), ('orange', 2)])