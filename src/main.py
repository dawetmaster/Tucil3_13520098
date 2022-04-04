import menu
import process

if __name__ == "__main__":
    # repeat until input menu is correct
    while True:
        # select input menu
        input_menu = menu.select_input_menu()
        # if input menu is 1
        if input_menu == "1":
            # insert file name dialog
            filename = menu.insert_file_name_dialog()
            # load file
            np_array = menu.load_file(filename)
            # if file is OK
            if np_array is not None:
                # go to main process
                process.main(np_array)
        # if input menu is 2
        elif input_menu == "2":
            # insert input string from keyboard
            input_str = menu.insert_from_keyboard_dialog()
            # convert string to numpy array
            np_array = menu.convert_to_np_array(input_str)
            # print numpy array
            print(np_array)
            # go to main process if np_array not none
            if np_array is not None:
                process.main(np_array)
        # if input menu is 3
        elif input_menu == "3":
            # exit
            break
        # if input menu is not 1, 2 or 3
        else:
            # print error
            print("Error: invalid input")
