from libs.B00370287_class_menu import Menu
from libs.B00370287_functions_files import file_save
from libs.B00370287_variables import menu_title, menu_subtitle, menu_width, file_name
from libs.B00370287_functions_eighties import eighties_mode


# User menu after logged in
# user (Customer Object) / customer_base the list of Customer Objects
def user_mode(user, customer_base):
    # New Menu Object
    user_menu = Menu(menu_title, menu_subtitle, menu_width)
    user_menu.menu_option_title = f'Customer Menu:  {user.first_name} {user.last_name}'
    user_menu.menu_option_list = ['Display User Details', 'Update Password', 'Extremely Dubious Eighties Movie Mode']
    user_menu.menu_exit_list = ['X', 'Sign Out', False]

    user_loop = True

    # execute the logged_in method to update no of log-ins and update the date last logged - then save the customer_base

    # Loop until user signs out
    while user_loop:
        # Display the menu and get a valid option
        user_input = user_menu.run()

        if user_input == 1:
            print()
            user.display()  # Display the user

        if user_input == 2:
            # execute the change_password from the Customer object - then save the updated file
            user.change_password()
            file_save(file_name, customer_base)
            input('\n\tPress enter to continue...  ')

        if user_input == 3:
            # send the user's first name only to the eighties function
            eighties_mode(user.first_name)

        if user_input == 'end_loop':
            # stop looping
            print('\n\tReturning to the main menu\n\n')
            user_loop = False

        # if not 1 or 3, the input is not required
        if user_input == 1 or user_input == 3:
            input('\n\tPress enter to continue...  ')


# When an admin account logs in
def admin_mode(user, customer_base):
    # Admin Menu
    admin_menu = Menu(menu_title, menu_subtitle, menu_width)
    admin_menu.menu_option_title = 'Admin Menu'
    admin_menu.menu_option_list = ['Display User', 'Display All Users', 'Reset User Password', 'Unlock Account',
                                   'Delete User Account', 'Reset Own Password']
    admin_menu.menu_exit_list = ['X', 'Sign Out', False]

    admin_loop = True  # variable to indicate a loop is needed

    # several options need the list of IDs to be displayed prior to any further action - so split into another function
    def list_users():
        print('\n\tAvailable Users:\n')
        # List all IDs in the customer_base
        for user_loop in customer_base:
            print(f'\t{user_loop.user_id}')

    while admin_loop:
        # Display the admin menu and get a valid input
        admin_input = admin_menu.run()

        if admin_input == 1:
            # Display available IDs
            list_users()
            # Ask for the user to display
            sub_input = input('\n\tPlease enter the username to display:  ').lower()
            user_found = False
            # confirm the user ID entered is valid
            for user_class in customer_base:
                if sub_input == user_class.user_id:
                    admin_menu.display()
                    user_found = True
                    # Display the user details when found
                    user_class.display()
            if not user_found:
                print('\n\tUser ID not recognised.')

        if admin_input == 2:
            print()
            # loop through all users, displaying their details
            for user_class in customer_base:
                user_class.display()

        if admin_input == 3:
            # list all available IDs
            list_users()
            sub_input = input('\n\tPlease enter the username to reset:  ').lower()
            user_found = False
            # Check valid ID entered
            for user in customer_base:
                if sub_input == user.user_id:
                    user_found = True
                    # If valid user, call the change_password method from the object then save the file
                    user.change_password()
                    file_save(file_name, customer_base)
            if not user_found:
                print('\n\tUser ID not recognised.')

        if admin_input == 4:
            print('\n\tLocked Users:\n')
            # List all IDs of any locked users from the customer_base
            for user in customer_base:
                if user.account_locked:
                    print(f'\t\t{user.user_id}')
            # Unlock the user account
            user_to_unlock = input("\n\n\tPlease enter the User ID of the account to unlock:  ").lower()
            user_found = False
            # iterate the customerbase for the user
            for user in customer_base:
                if user_to_unlock == user.user_id:
                    user_found = True
                    # check if the entered ID is locked - if so, change the account_locked and save the file
                    if user.account_locked:
                        user.account_locked = False
                        file_save(file_name, customer_base)
                        # communicate to the user
                        print(f"\n\n\tUser ID:  {user.user_id}  has been unlocked.  Consider resetting the password.")
                    else:
                        # unlocked user ID entered
                        print(f"\n\n\t{user.user_id} was not locked.  No action has been taken.")
            # user ID entered not valid
            if not user_found:
                print("\n\n\tUser not found.")

        if admin_input == 5:
            # List all available IDs
            list_users()
            sub_input = input('\n\tPlease enter the username to DELETE:  ').lower()
            # Check if admin account and reject if attempted
            if sub_input == 'admin':
                print('\n\tSorry, you cannot delete the admin account!')
            else:
                user_found = False
                # check valid ID entered
                for user in customer_base:
                    if sub_input == user.user_id:
                        user_found = True
                        # if a valid ID entered - confirm that a delete is required
                        if input(f'\n\tAre you sure you want to DELETE {user.user_id}? (Y/N):  ').capitalize() \
                                == 'Y':
                            print(f'\n\tDeleting {user.user_id}')
                            # delete the user from the list and save the file
                            customer_base.remove(user)
                            file_save(file_name, customer_base)
                if not user_found:
                    print('\n\tUser ID not recognised.')

        if admin_input == 6:
            # change password of user - which is the object of the admin user that is logged in - then save the file
            user.change_password()
            file_save(file_name, customer_base)

        if admin_input == 'end_loop':
            # stop looping if the exit is selected
            print('\n\tReturning to the main menu\n\n')
            admin_loop = False
        else:
            input('\n\n\tPress Enter to Continue...  ')
