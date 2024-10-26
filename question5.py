#python function that takes dictionary as input and prints all keys whose values are even numbers

def dictionary_values(dictionary):

    for key, value in dictionary.items():
        if value % 2 == 0:
            print(key)
        # print(f"{key}: {value}")
dictionary_values(dictionary = { "a" :1,"b" :2,"c" :3,"d" :4,"e" :5 })