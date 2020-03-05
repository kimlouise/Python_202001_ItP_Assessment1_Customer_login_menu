# Python_202001_ItP_Assessment1_Customer_login_menu

Assessment Instructions:

The first assessment for this course is an individual programming exercise where you will be expected to
create a program to perform a specified task. The assessment is worth 30 marks.

You are required to create the front end of a new system which allows access for registered customers.
New customers must register their details before they can proceed.
Users should be presented with a menu, giving them the following main choices:
• Existing customers can login using their username and password
• New customers can register their details
If an existing customer accesses the system, the username and password entered is checked against
details held on file.
An incorrect username should be rejected.
If the username is correct, they should be allowed a maximum of three incorrect attempts at the
password before being refused access.
If a new customer accesses the system, they should be asked for their first name and surname.
Your program should create a username is by combining the first three letters of their first name with
the first three letters of their surname (all in lower case).
Example: Name Username
John Smith johsmi
Linda Jones linjon
Al Simon alsim (note – 2 letters in Al)
New customers should also be asked for a password.
The password must contain ALL of the following:
• at least one upper case letter
• at least one lower case letter
• at least one number
• at least one of these eight special characters ! £ $ % & @ # ?
• at least 8 and no more than 16 characters.
When a customer (new or existing) successfully logs in they should see a confirmation message – that’s
all we need to do at this stage.
There is, obviously, more to the system than this, but we are only required to create this part of it.
Usernames and passwords should be stored in an external file so that details can be maintained
between each successive run of the program.
The program should be fully commented and appropriate names should be used throughout for
variables, functions, files etc.

Marks will be allocated as follows:
• Fully working menu up to 5 marks
• Creation of username up to 4 marks
• Creation of password up to 5 marks
• Use of external file for data storage up to 4 marks
• Internal manipulation of data up to 8 marks
• Comments/meaningful identifiers up to 4 marks
