#python function that takes a list of integers and a target sum. The function should return "true" if there are two distinct numbers
#that add upto the sum and "false" otherwise

def integer_sum(ints, tsum):
    seen = set()
    for i in ints:
        if tsum - i in seen:
            print("True")
            seen.add(i)
    print("False")

integer_sum([1,2,3,4], 7)

