# Write a program to read in 10 values from the keyboard and append them to a list

<<<<<<< HEAD

def sum_is_greater_than(my_list, upper_bound):
=======
def sumIsGreaterThan(my_list, upper_bound):
>>>>>>> origin/master
    counter = 0
    for i in my_list:
        counter += i
    return counter > upper_bound


stuff = []
<<<<<<< HEAD
while not sum_is_greater_than(stuff, 100):
=======

while not sumIsGreaterThan(stuff, 100):
>>>>>>> origin/master
    val = input("Enter a value: ")
    try:
        val = int(val)
        stuff.append(val)
    except TypeError:
        val = input("Please enter an integer: ")

print(stuff)
