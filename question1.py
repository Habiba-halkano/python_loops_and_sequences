#python project that prints numbers 1 - 50 using a for loop. for numbers divisible by 3 print fizz, for numbers divisible by 5 print buzz
#for numbers divisible by both print fizzbuzz

#function declaration
def print_numbers():
    for x in range(1,51):
        if x%3 == 0 and x%5 == 0:
            print("fizzbuzz")
        elif x%3 == 0:
            print("fizz")
        elif x%5 == 0:
            print("buzz")
        else:
            print(x)

print_numbers()