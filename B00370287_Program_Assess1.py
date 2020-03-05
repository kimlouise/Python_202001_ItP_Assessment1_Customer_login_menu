from libs.B00370287_class_customer import Customer
from libs.B00370287_class_menu import Menu
from libs.B00370287_functions_files import file_load, file_save
from libs.B00370287_functions_main_menu import customer_login, customer_register, customer_about
from libs.B00370287_variables import file_name, menu_title, menu_subtitle, menu_width

# File List:
#   libs / class_customer.py:       Customer Class:         Used to create valid Customer objects
#                                   auto_password():        To generate an auto password
#                                   password_check():       Determine if a password is valid
#                                   get_password():         Get a valid password from a user (using password_check)
#   libs / menu_class.py:           Menu Class:             Create / store / display / run menus
#                                   console_clear():        Clear the console window
#   libs / functions_eighties.py    eighties_mode():        Just display text to the user and decide where to go next
#                                   tic-tac-toe():          A simple noughts and crosses game....
#   libs / functions_files.py       file_load():            Load a file and return the contents
#                                   file_save():            Save a variable to a pickle file
#   libs / functions_main_menu.py   customer_login():       Gets the user login and validates etc
#                                   customer_register():    Registers a new customer
#                                   customer_about():       Display a simple 'About' screen
#   libs / functions_misc.py        slow_print():           Slowly print any text passed - variable speed
#                                   clear():                Clear the console
#   libs / functions_modes.py       user_mode():            Options for a user once logged in
#                                   admin_mode():           Options for admin when logged in
#   libs / variables.py             misc variables:         Misc variables - separate file to keep files tidy

# load existing data into the variable customer_base which is a list of all Customer objects
customer_base = file_load(file_name)

# if there is not an existing customer_base, it will be created, but then a standard admin account will be created
# this is done by the class checking - then creating admin with the password of !Password1
if not customer_base:
    admin = Customer(customer_base)
    customer_base.append(admin)
    file_save(file_name, customer_base)

# define the main menu
# main_menu - Menu object from class_menu.py
# Menu Title, Subtitle and Width taken from variables imported from variables.py
main_menu = Menu(menu_title, menu_subtitle, menu_width)

# further Menu attributes for the main menu object
# menu option title
main_menu.menu_option_title = 'Main Menu'
# list on menu options to be displayed
main_menu.menu_option_list = ['Customer Sign In', 'Customer Registration', 'About this Application',
                              'Display Admin Credentials (for development purposes only)']
# menu exit options.  string to exit, string to display, as True is selected, if the exit is triggered,
# will exit the app and no further action is needed
main_menu.menu_exit_list = ['Exit', 'Exit the Application', True]

main_loop = True

# Main Loop
while main_loop:
    user_input = main_menu.run()  # get a valid input from the Menu object - can only return a valid choice

    # valid options to trigger functions within functions_main_menu.py
    if user_input == 1:
        # customer list is passed to the function to process - function in functions_main_menu.py
        customer_login(customer_base)
    if user_input == 2:
        # customer list is passed to the function to process - function in functions_main_menu.py
        customer_register(customer_base)
    if user_input == 3:  # run the customer_about function - function in functions_main_menu.py
        customer_about()
    if user_input == 4:  # Display the admin credentials
        print('\n\n\tAdmin User ID:\tadmin\n\n\tAdmin Password:\t!Password1')

    input('\n\tPress Enter to Continue...  ')
