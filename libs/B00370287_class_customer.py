import hashlib
import random
import time
from datetime import datetime


#  File contains Customer class AND associated password functions
class Customer(object):
    """
    class for customer object
    usage:
        declaration:    new_user = Customer(customer_base)
        args:           existing:  list of objects is passed, a check will be made to check if user already exists
        methods:        customer.display() - displays the details of the customer
                        customer.change_password() - gets a new password and updates the user.password
                        customer.logged_in() - increments the log_number and updates the last_logged for the customer
        attributes:     all attributes are generated when the object is created
    """

    # Initialise
    def __init__(self, exist_check):
        # when the program first runs, it checks if the customer_base file contains, then if not, creates a blank file
        # and the customer_base list is created empty.  When this happens from the main program, a new Customer
        # object is created, using the data in the not_exist condition below.  This creates the admin account and the
        # program file will then save the user in the database, meaning this will only happen once.  Any subsequent
        # new Customer objects will be created as normal

        # if a new customer_base - create admin - will only run if the database has just been created with no entries
        if not exist_check:
            self.admin = True
            self.first_name = 'Admin'
            self.last_name = 'User'
            self.user_id = 'admin'
            self.__encryption_iteration = int(random.randrange(500000, 999999))  # random int for password encryption
            self.password = self.__get_hex('!Password1')  # for password encryption
            self.log_number, self.date_created, self.date_logged = 1, datetime.now(), datetime.now()
            self.duplicate = False
            self.account_locked = False
            # Print details of the admin account
            print('\n\tAdministration account was created using the default admin parameters:')
            print('\n\t\tUser ID:\tadmin')
            print('\n\t\tPassword:\t!Password1')
            print('\n\tFor security reasons, please login and change the password.')
            input('\n\tPress enter to continue...   ')

        # If not, run as normal
        else:
            # duplicate is assigned to the class, to indicate whether the new customer should be saved
            self.duplicate = False
            # default admin is set to False.
            self.admin = False
            # declare the password attribute as none - once created and the names and userID are generated,
            # the user will be prompted to enter a valid password via the password_change method before the account
            # is saved
            self.password = None
            self.account_locked = False
            # variable used for the password encryption - when creating and checking the password - this defines the no
            # of times the password is 'hashed' for extra security
            self.__encryption_iteration = int(random.randrange(500000, 999999))
            # loop until the name is inputted and confirmed by the user
            # For the while loop
            name_confirmed = False
            while not name_confirmed:
                # For the while loops for entering the first and second name
                accepted_first, accepted_second = False, False
                # loop until valid first name is entered
                while not accepted_first:
                    # set the first_name to the input and check it is alpha and 2 or more characters
                    self.first_name = input('\tPlease enter you first name:  ').capitalize()
                    if len(self.first_name) >= 2 and self.first_name.isalpha():
                        accepted_first = True

                # loop until valid last name is entered
                while not accepted_second:
                    # set the last_name to the input and check it is alpha and 2 or more characters
                    self.last_name = input(
                        f'\n\tThank you {self.first_name}.  Please enter your last name:  ').capitalize()
                    if len(self.last_name) >= 2 and self.last_name.isalpha():
                        accepted_second = True

                # check name is correct as this is important to generate the user ID
                if input(f'\n\tYour name is:  {self.first_name} {self.last_name}.  Is this correct? (Y/N):  ') \
                        .capitalize() == 'Y':
                    name_confirmed = True

            # After the name is confirmed, the user_id is set to the first 3 letters of each name in lowercase
            self.user_id = (self.first_name[0:3] + self.last_name[0:3]).lower()  # user ID generated

            # Check if the user_id is a duplicate - check the customer_base and if a duplicate, set the duplicate
            # attribute to True, so the loop calling for a new Customer can act appropriately
            for check in exist_check:
                if check.user_id == self.user_id:
                    self.duplicate = True
                    print('\n\tDuplicate user name...  Cancelling registration.')

            # Set the rest of the non-inputted attributes if the user_id is not a duplicate
            if not self.duplicate:
                self.log_number, self.date_created, self.date_logged, self.password = 0, datetime.now(), \
                                                                                      datetime.now(), ''

                # Get the user password.  Asks for a password or auto generates as required
                self.change_password()

    # Display Method - When called, will display the user details:
    #       user ID  ||  first name  ||  last name  ||  date account created  ||  date last logged in
    #       ||  no of times logged in  ||  whether account is locked || whether user has admin privileges
    # Usage:  customer.display()
    def display(self):
        print(f"\tUser ID:\t\t{self.user_id}\n\t"
              f"Name:\t\t\t{self.first_name} {self.last_name}\n\t"
              f"Account created:\t{self.date_created.strftime('%H:%M - %d %B %Y')}\n\t"
              f"Last login:\t\t{self.date_logged.strftime('%H:%M - %d %B %Y')}\n\t"
              f"No of times logged in:\t{self.log_number}\n\t"
              f"Account Locked:\t\t{self.account_locked}\n\t"
              f"Admin User:\t\t{self.admin}\n\n")

    # Change Password Method - called to set the password attribute to a valid password
    # Usage:  customer.get_password()
    def change_password(self):
        # Calls the get_password function to get a valid password
        temp_password = get_password()
        # convert the inputted valid password to a hashed hex which is stored in the password attribute
        self.password = self.__get_hex(temp_password)
        # print the user credentials
        print(f'\n\tLogin Credentials:\n\n\t\tUser ID:\t{self.user_id}\n\t\tPassword:\t{temp_password}')

    # function to increment the no of log-ins and the last login attribute
    # Usage:  customer.logged_in()
    def logged_in(self):
        self.date_logged = datetime.now()
        self.log_number += 1

    # function to check a password when logging back in
    # Usage:  customer.password_compare(password_inputted)
    def password_compare(self, user_input):
        # convert the input to a hex hash
        temp_check = self.__get_hex(user_input)
        # compare to the customer password hash
        # return True if matching
        if temp_check == self.password:
            return True
        # False if not matching
        else:
            return False

    # convert a string into a hex hash, using the encryption iteration and the string
    # 'UWS: B00370287, Introduction to Programming'
    def __get_hex(self, __user_input):
        __user_input = hashlib.pbkdf2_hmac('sha512', __user_input.encode(),
                                           b'UWS: B00370287, Introduction to Programming', self.__encryption_iteration)
        __user_input = __user_input.hex()
        return __user_input


def auto_password():
    # usage:  password = auto_password()
    # function to auto generate a new password for the user
    # there is no specific number of character types or order so the password doesn't follow any other pattern

    # list of characters the the auto_password can select.  Taken from the password requirement list
    character_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!£$%&@#?")
    # generate the password
    print('\n\tGenerating Password...')
    time.sleep(0.5)  # just a needless delay to make it look like the computer is giving it a lot of thought ;)
    # loop
    loop_required = True
    while loop_required:
        password = ''  # blank password
        # for loop - a 16 character password
        for random_letter in range(16):
            # add a random character from the list to the password string
            password += character_list[random.randrange(70)]
        # if the password generated is valid, then it is returned.  If invalid, will generate another to check
        if password_check(password) == 'Valid':
            return password


def password_check(password):  # function to check if the password meets the requirements of the assessment
    # only designed for use with the get_password() and auto_password() functions
    # initial variables - all set to false to indicate the conditions have not been met
    upper, lower, number, length, special = False, False, False, False, False
    # split the passed password into a list of single chars for checking
    password_list = list(password)
    # iterate all chars
    for check in password_list:
        # if char is uppercase, set upper to true, indicating the condition has been met
        if check.isupper():
            upper = True
        # if char is lowercase, set lower to true, indicating the condition has been met
        elif check.islower():
            lower = True
        # if char in a number, set number to true, indicating the condition has been met
        elif check.isnumeric():
            number = True
        # if char is one of the str, set special to true - condition has been met
        elif check in '!£$%&@#?':
            special = True
        # length check, set length to true - condition met
        if 8 <= len(password) <= 16:
            length = True
    # if ALL are true, return valid
    if upper and lower and number and special and length:
        return 'Valid'
    # if any conditions have not been met, return to the calling script to act upon
    else:
        return [upper, lower, number, special, length]


def get_password():
    # Function to ask the user for a password and check it meets the requirements (auto password option available)
    # Define a list of the password requirements.  This will initially be displayed and if the password does not fulfil
    # requirements, is used to list the requirements not met by the inputted password

    # Requirements list - for displaying prior to input AND for use if any criteria are not met
    password_requirements = ['At least one uppercase letter', 'At least one lowercase letter',
                             'At least one number',
                             'Include at least one of:  ! £ $ % & @ # ?', 'At least 8 and no more than 16 characters']

    # start of loop
    loop_required = True
    while loop_required:
        # Print the Password Requirements
        print('\n\tPassword Requirements:\n')
        for requirement in password_requirements:
            print('\t\t' + requirement)

        # Get a new password from the user
        user_input = input('\n\tType Auto for a generated password\n\tOr enter a new password:  ')

        # Check if auto password is required.  If it is, then the output from the auto password is returned
        if user_input.capitalize() == 'Auto':
            return auto_password()

        # If the user entered their own password
        else:
            # Check the password is valid - 'Valid' is returned if valid / if not, the BOOLs from the check are returned
            result = password_check(user_input)

            # If valid, return the password that was inputted
            if result == 'Valid':
                print('\n\tPassword Accepted')
                return user_input  # inputted password is returned

            # If the password is invalid
            else:
                print('\n\tInvalid password.  You were missing:\n')

                # Iterate the result - and display any requirement that wasn't met
                for index, requirement in enumerate(result):
                    if not requirement:  # user know what requirements have not been met
                        print('\t\t' + password_requirements[index])
                input('\n\tPress enter to try again...   ')
        print('\n\n')
