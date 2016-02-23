my_list = [0, 0, 0, 0, 0, 0]
elementToChange = ""
indexToAddTo = 0

elementToChange = input("Please enter anything you like: ")
try:
    elementToChange = int(elementToChange)
except TypeError:
    print("Error")

CorrectInput = False
while not CorrectInput:
    try:
        indexToAddTo = int(input("Choose where to add this in my_list that has " + str(len(my_list)) + " elements: "))
        my_list[indexToAddTo] = elementToChange
        CorrectInput = True
    except TypeError:
        print("Please enter an integer.")
    except IndexError:
        print("Please choose an element that lies in the list.")

print(str(my_list(indexToAddTo)))