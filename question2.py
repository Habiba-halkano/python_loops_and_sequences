#use while loop to write a function that continually ask the user for input until they type the word exit. program should print each word
# given by the user before asking for the next input

def input_word():
    word = input("Enter a word: ")
    while word != "exit":
        print(word)
        word = input("Enter a word: ")

input_word()

