# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
# write a program that reads in 10 numbers, then prints the sum of those


def _sum(sum_list):
    return_sum = 0
    for i in sum_list:
        return_sum += i
    return return_sum


def input_int(disp_str, err_message):
    try:
        return True, int(input(disp_str))
    except ValueError:
        print(err_message)
        return False, err_message

def input_until_int(disp_str, err_message):
    is_int = False
    _input = ""
    while is_int is False:
        (is_int, _input) = input_int(disp_str, err_message)
    return _input

def collect_input(list_size):
    collect_list = []
    for i in range(list_size):
        collect_list.append(input_until_int("Enter the " + str(i+1) + "th number: ", "Please enter a number"))
    return collect_list


def collect_input_until(stop_value):
    collect_list = []
    _input = ""
    while _input != stop_value:
        _input = input_until_int("Please enter a number: ", "Make sure that you are entering a number")
        collect_list.append(_input)
    return collect_list

print(_sum(collect_input_until(-1)))
