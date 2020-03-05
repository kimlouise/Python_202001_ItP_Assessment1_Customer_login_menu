from os import name, system


# function to clear the console / terminal
# Usage:  console_clear()
def console_clear():
    if name == 'nt':  # if windows
        _ = system('cls')
    else:  # mac / linux
        _ = system('clear')


# Menu Class
class Menu(object):
    """
    class for Menu objects
    Purpose:            To display menus and if required, accept a valid input from the user - the setup of the menu
                        is used to let the method know what is valid and what is invalid.

    args:               title - title of the menu - ie 'Kimmi Co' that is displayed in the header of the menu
                        subtitle - subtitle for the header
                        width - character length of the menu

    Methods:            run()       display the menu and then return a valid input
                        display()   display the menu - no input etc

    Usage:              admin_menu = Menu('Menu Title', 'Menu Subtitle', 80)
                        admin_menu.menu_option_title = "Menu Option Title"

    other attributes:   menu_option_title       string              title of the options within the menu
    (All optional)      menu_option_list        list of strings     options to display within the menu
                        menu_exit_list          [str1, str2, bool]  str1 - string to accept to exit app or loop
                                                                    str2 - string to display what string 1 does
                                                                    bool - True - Exit app / False - Exit loop
                        menu_instruction_list   list of strings     list of strings with misc instructions to be
                                                                    displayed rather than options
    """

    # Initialise
    def __init__(self, __title, __subtitle, __width):

        # compulsory attributes
        self.menu_title = __title
        self.menu_subtitle = __subtitle
        self.menu_width = __width

        # initialised but optional attributes
        self.menu_option_title = None
        self.menu_instruction_list = None
        self.menu_option_list = None
        self.menu_exit_list = None

    # Method to run the menu -  display then return a valid input dependant on the option / exit variables.
    #                           input is only used when there are options in the option list
    def run(self):
        looping = True
        console_clear()
        while looping:

            # call the display method
            self.display()

            # This section is executed ONLY if the menu option list AND the exit list is populated
            if self.menu_option_list and self.menu_exit_list:
                input_error = False

                # Get the input
                user_input = input('\tPlease choose your option:  ').capitalize()

                # Checks for an exit it the exit list is populated
                if self.menu_exit_list:

                    # Checks for the exit character or string
                    if user_input == self.menu_exit_list[0].capitalize():

                        # ask for confirmation of exit
                        if self.__confirm_exit():

                            # if variable is set to True - exit the app
                            if self.menu_exit_list[2]:
                                print('\n\tExiting.  Goodbye...\n\n')
                                exit()

                            # Or return 'end_loop'
                            else:
                                return 'end_loop'

                    # Check for a numbered option being input
                    else:

                        # Try as it will attempt to convert the input to an int - but will handle the error if not no's
                        try:
                            input_int = int(user_input)

                            # Check if the int is a valid number choice - ie 1 to the no of options
                            if input_int < 1 or input_int > len(self.menu_option_list):
                                input_error = True
                            else:
                                # If all ok - return the selected option
                                return input_int
                        # if not a number inputted - note as an input error
                        except ValueError:
                            input_error = True
                # Display there was an error
                if input_error:
                    print('\n\tInvalid input.  Please try again.\n')
                    input('\n\n\tPress enter to continue...  ')
            else:
                looping = False

    # Method to display the menu
    def display(self):

        # func to return the string plus blank space to make the string appear centred in the menu
        def centre_string(string_to_centre):
            # Usage print(centre_string('Hello'))
            # will print Hello in the horizontal centre of the menu
            return ' ' * int((self.menu_width - len(string_to_centre)) / 2) + string_to_centre

        console_clear()

        break_string = '~' * self.menu_width  # for displaying a full line of ~ to separate sections of the menu
        menu_underline = '~' * len(self.menu_title)  # make a string of ~ with the length of the menu title

        # Print the Header
        print(f'\n\n\t{break_string}\n\n\t{centre_string(self.menu_title)}\n\t{centre_string(menu_underline)}\n\n\t'
              f'{centre_string(self.menu_subtitle)}\n\n\t{break_string}\n')

        # Print the Option Title
        if self.menu_option_title:
            title_underline = '~' * len(self.menu_option_title)
            print(f'\t{centre_string(self.menu_option_title)}\n\t{centre_string(title_underline)}\n')

        # Print the instructions
        if self.menu_instruction_list:  # iterate through the instructions
            for display_string in self.menu_instruction_list:
                print(f'\t{centre_string(display_string)}')
            print('\n')

        # Print the Options
        if self.menu_option_list and self.menu_exit_list:
            for index, display_string in enumerate(self.menu_option_list):
                display = f'{str(int(index) + 1)}:  {display_string}'
                print(f'\t{centre_string(display)}\n')
            print()
            display = f'{self.menu_exit_list[0]}:  {self.menu_exit_list[1]}'
            print(f'\t{centre_string(display)}\n')

        # Close the menu (if options or exit are used) - prints the line at the bottom of the menu
        if self.menu_option_title or self.menu_instruction_list or \
                (self.menu_instruction_list and self.menu_option_list):
            print(f'\t{break_string}\n\n')

    # Confirm the exit - return True if the user confirms
    def __confirm_exit(self):
        user_input = input(f'\n\tAre you sure you want to {self.menu_exit_list[1].lower()}?  (Y/N):  ').capitalize()
        if user_input == 'Y':
            return True
