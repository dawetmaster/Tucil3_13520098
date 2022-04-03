import numpy as np
import os


def select_input_menu():
    """
    Select input menu
    """
    print("\nSelect input menu")
    print("1. Input from file")
    print("2. Input from keyboard")
    print("3. Exit")
    return input("Select: ")


def insert_file_name_dialog():
    """
    Insert file name dialog
    """
    print("\nInsert your file name")
    return input("File name: ")


def examine(filename):
    # Required: file must be a txt file
    # Required: file cannot be empty
    # Required: file exists

    # Check if file exists
    if not os.path.isfile(filename):
        print("File does not exist")
        return False

    # Check if file is a txt file
    if not filename.endswith(".txt"):
        print("File is not a txt file")
        return False

    # Check if file is empty
    if os.stat(filename).st_size == 0:
        print("File is empty")
        return False

    return True


def load_file(filename):
    # examine filename using function examine(filename)
    # if file is OK, load it
    if examine(filename):
        # open file
        file = open(filename, "r")
        # read file
        string = file.read()
        # close file
        file.close()
        # convert string to numpy array
        np_array = convert_to_np_array(string)
        # return numpy array
        return np_array
    else:
        return None


def insert_from_keyboard_dialog():
    """
    Insert from keyboard dialog
    """
    print("\nInsert your puzzle")
    print("Input format: int1 int2 int3 ... int16")
    print("Example: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16\n")
    return input("Puzzle: ")


def examine_array(string):
    # assume the given input string is a line of numbers separated by space
    # convert the given string to list of integers
    # and then check if list length is 16 and contains unique numbers
    # from 1 to 16, number order is not mandatory
    # return True if all requirements are met
    # return False otherwise

    # convert string to list of integers
    list_of_int = [int(i) for i in string.split()]

    # check if list length is 16
    if len(list_of_int) != 16:
        print("List length is not 16")
        return False

    # check if list contains unique numbers
    if len(list_of_int) != len(set(list_of_int)):
        print("List contains duplicate numbers")
        return False

    # check if list contains numbers from 1 to 16
    if not all(i in range(1, 17) for i in list_of_int):
        print("List contains numbers not from 1 to 16")
        return False

    return True


def convert_to_np_array(string):
    # the previous input string is to be converted
    # to a numpy array with size 4x4
    # return the numpy array
    # if the input string is not valid, return None

    # check the string using function examine_array
    if not examine_array(string):
        return None

    # convert string to list of integers
    list_of_int = [int(i) for i in string.split()]

    # convert list to numpy array
    np_array = np.array(list_of_int, dtype=np.int8)

    # reshape the numpy array
    np_array = np_array.reshape(4, 4)

    return np_array
