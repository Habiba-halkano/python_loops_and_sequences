#python function using a loop that returns the largest number in a given tuple

def largest_tuple(my_tuple):
    largest = my_tuple[0]
    for i in my_tuple:
        if i > largest:
            largest = i
    print(largest)


largest_tuple(my_tuple = (10, 20, 30, 40 ,50))