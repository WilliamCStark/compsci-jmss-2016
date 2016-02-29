# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

user_input = ""
word_collection = []
user_input = input("Please enter a word: ").lower()
while user_input != "quit":
    word_collection.append(user_input)
    user_input = input("Please enter a word: ").lower()
word_collection.sort()
for i in word_collection:
    print(i)
