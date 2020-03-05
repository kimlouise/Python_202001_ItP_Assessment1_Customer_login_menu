from libs.B00370287_class_customer import Customer
from libs.B00370287_class_menu import console_clear
from libs.B00370287_functions_files import *
from libs.B00370287_functions_misc import slow_print
from libs.B00370287_functions_modes import *
from libs.B00370287_variables import *


# File contains functions for the main menu that is displayed when the program loads

# Customer Login - if Option one in the main menu is selected - Arg is the list of customers for checking etc
def customer_login(customer_base):
    # New Menu for the login screen
    menu_login = Menu(menu_title, menu_subtitle, menu_width)
    menu_login.menu_option_title = 'Customer Sign In'
    menu_login.menu_instruction_list = ['You will be asked for your user ID and Password.', '',
                                        'Please follow all prompts.']
    # Display the Login Menu
    menu_login.display()

    # Request the user ID to login with - convert to lower and all ids are lowercase
    user_input = input('\tPlease enter your User ID:  ').lower()
    valid_user = None

    # Iterate through the customer_base and check for valid ID
    for user_check in customer_base:
        if user_check.user_id == user_input:
            # If found - valid_user becomes the variable used containing the Customer object of the ID
            valid_user = user_check
    # Not found - Display - giving the option to register
    if not valid_user:
        if input('\n\tUser ID not found.  Would you like to register a new account? (Y/N):  ').capitalize() == 'Y':
            customer_register(customer_base)
        else:
            print('\n\tReturning to the main menu...')
            time.sleep(1)
    # If valid user name is entered
    else:
        # 3 password chances
        password_chance = 3
        login_loop = True  # for loop of password inputs
        # checks if the account is locked - if not runs this section
        if not valid_user.account_locked:
            # Loop while the password entered is not correct - but exits the applications after 3 failed attempts
            while login_loop:
                # Request password
                user_input = input('\n\tPlease enter your password:  ')

                # Uses the password_compare method from the Customer Object to check the password is correct.  This is
                # required because the password is encrypted and stored without recording the actual password inputted
                if valid_user.password_compare(user_input):
                    print('\n\tPassword accepted.  Loading menu...')
                    # execute the logged_in method to update no of log-ins and update the date last logged
                    # then save the customer_base
                    valid_user.logged_in()
                    file_save(file_name, customer_base)

                    time.sleep(2)
                    login_loop = False  # end this loop if password is correct

                    # if the correct password is entered - if Admin, load the admin menu, or if not, open the user menu
                    if valid_user.admin:
                        admin_mode(valid_user, customer_base)
                    else:
                        user_mode(valid_user, customer_base)
                # If password is incorrect
                else:
                    # reduce the number of password attempts remaining
                    password_chance -= 1

                    # After 3 incorrect password attempts - Admin exits as an admin is needed to reset an account
                    if password_chance == 0 and valid_user.user_id == "admin":
                        print("\n\n\tPassword incorrect.  Exiting application...")
                        exit()
                    # for any other user, account is locked and then returns to the main menu
                    elif password_chance == 0:
                        print('\n\tPassword incorrect.  Your account has now been locked.  Please contact the '
                              'administrator to restore access.\n\n')
                        # property to lock account
                        valid_user.account_locked = True
                        file_save(file_name, customer_base)
                        login_loop = False
                    # after 1 or 2 incorrect passwords - displays the chances remaining
                    else:
                        print(f'\n\tPassword incorrect.  You have {password_chance} attempt(s) remaining.')
        # if account is locked....
        else:
            print(f"\n\n\tThe account {valid_user.user_id} is currently locked.  Please contact the administrator to "
                  f"unlock the account.\n\n\tReturning you to the main menu.")


# Register a new customer - Option 2 from the main menu - customer_base to check for duplicates
def customer_register(customer_base):
    # New menu for registration screen
    menu_register = Menu(menu_title, menu_subtitle, menu_width)
    menu_register.menu_option_title = 'Register New User'
    menu_register.menu_instruction_list = ['You will be asked for your first, then last name,',
                                           'then asked to supply a password.', 'Please follow all prompts.']
    # Display the menu
    menu_register.display()

    # create a new Customer object - the object takes the relevant details
    new_user = Customer(customer_base)

    # If the user is not a duplicate, then the new Customer object will be added to the customer_base and saved
    if not new_user.duplicate:
        customer_base.append(new_user)
        file_save(file_name, customer_base)
        print('\n\n\tPlease make a note of your credentials.')

    # If it is a duplicate, offer to go straight to the sign in screen
    else:
        if input('\n\tWould you like to load the Sign In screen? (Y/N):  ').capitalize() == 'Y':
            customer_login(customer_base)
        else:
            print('\n\tReturning to the main menu...')
            time.sleep(1)


# About option 3 from the main screen
def customer_about():
    # Clear the screen
    console_clear()
    # Display using the slow_print function in the functions_misc.py file - variables in the variables.py file
    slow_print(about_0, 0.02)
    slow_print(about_1, 0.005)
