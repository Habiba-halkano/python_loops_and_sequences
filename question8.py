#function that takes dictionary and an integer n as input and returns a list of keys from the dictionary where the values are greater than n

def dictionary_function(my_dict, n):
    result = [key for key, value in my_dict.items() if value > n]
    print(result)

dictionary_function(my_dict={'a':4, 'b':7, 'c':6}, n=5)