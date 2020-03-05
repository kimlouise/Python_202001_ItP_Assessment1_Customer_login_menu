import os.path
import pickle
import time  # Just for the pause


#  Load file (pickled).  #return the file contents
#  args: file_name:  Name of file
def file_load(file_name):  # open the file name passed
    if os.path.isfile(file_name):
        file_open = open(file_name, "rb")
        if os.stat(file_name).st_size == 0:  # Checks to see if the file is empty, if so, returns an empty list
            return_value = []
        else:
            return_value = pickle.load(file_open)  # if !empty returns file contents
        file_open.close()
        print(f'Opened {file_name}')
    else:
        print(f'{file_name} not found.  Creating new file.')
        file_open = open(file_name, 'wb')  # wb to write or create if not present
        file_open.close()
        return_value = []  # Return empty list if file is new
    time.sleep(1)  # 2 second pause before continuing
    return return_value


#  Save file (pickled)
#  Args:    file_name:  Name of file
#           variable:   Variable to save - list to save of information
#           ##  Only one var is saved and file is overwritten

def file_save(file, variable):  # Passes the variable name and file name to save to
    file_open = open(file, "wb")
    pickle.dump(variable, file_open)  # Save the file
    file_open.close()
