# for file i/o
file_name = 'customer_base.pck'

# standard menu header
menu_title = 'Kimmi Co'
menu_subtitle = 'Where uni assignments are needlessly taken way too far...'
menu_width = 80

# variable for the about menu
about_0 = ['\n\n\tKimmi Co Customer Base',
           '\n\t~~~~~~~~~~~~~~~~~~~~~~',
           '\n\n\tProgrammed by Kimberly Randall - B00370287',
           '\n\n\tCOMP07027 - Introduction to Programming - Assessment 1',
           '\n\n\tTutor:  Tony Gurney']

about_1 = ['\n\tThis simple program was designed for the first assignment in the UWS Introduction to Programming'
           '\n\tcourse as part of my Web and Mobile Development degree. ',
           '\n\n\tThe basics of how the program is structured, is every menu displayed is an instance of the Menu class'
           '\n\tI have made.  This class has a .run() method, which displays the menu, then loops until a valid input '
           '\n\tis given which is an integer depending on the number of menu options, or the exit string of the menu is'
           '\n\tinput. ',
           '\n\n\tThere are three outcomes from the .run() method:',
           '\n\n\t\tA valid integer is returned',
           "\n\t\t‘end_loop’ is returned",
           "\n\t\tThe application is exited",
           "\n\n\tThe first two options are then for the rest of the program to define what happens."
           '\n\n\tFor the data, a single list of Customer objects is used throughout the program.  This holds uses '
           '\n\tvarious attributes to hold the user data.  When the program is run for the first time either without'
           '\n\tthe external file in existence, or if it is empty, the program will automatically create an admin'
           '\n\taccount for the database.  When a new user is created, a new Customer object is created and then only '
           '\n\tadded to the main customer_base list and saved, when all of the required information is input and '
           'validated.',
           '\n\n\tPasswords are checked via a separate function, and the user is given the option to let the computer '
           '\n\tautomatically create one.  The password is then encrypted via the hashlib library, with a randomly '
           '\n\tgenerated iteration variable, using the sha512 encryption.  The resulting hex string is then saved, '
           '\n\twithout the actual password ever being stored.  When the user logs on, their input is encrypted in the '
           '\n\tsame way, then compared to the stored hex string to validate the user has input the correct password.',
           '\n\n\tThe user is given the option to display their account, change their password, or run the extremely'
           '\n\tdubious eighties movie mode, then finally have the option to log off, returning them to the main menu.',
           '\n\n\tAdmin user can display specific or all users, reset passwords, unlock accounts, delete accounts and '
           'log off'
           ]
