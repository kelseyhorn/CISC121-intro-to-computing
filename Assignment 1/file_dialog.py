"""
Simple file open dialogue using tkinter, inspired by
https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python

R. Linley
2019-03-20
"""

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def get_filename_from_dialog(types):
    """Returns a file open dialogue box filtering for types, a tuple of tuples,
    each of which consists of a brief description of a file type, e.g., 'text
    files', followed by an appropriate file extension, e.g., 'txt'.
    """
    root.wm_attributes('-topmost', 1)
    root.update() # Required for macOS. Added 2019-09-18 by R. Linley
    return filedialog.askopenfilename(filetypes=types)

if __name__ == '__main__':
    # Testing!
    
    # In addition to demonstrating the opening of a file dialogue, this test
    # code reads and processes a comma-separated values (csv) text file of
    # numbers, a file structured somewhat like this:
    #
    #   3.2,-7,33,92
    #   1,2.0,15,153.2
    #   ...
    #
    # I've over-commented since the code is likely to be hard to understand.

    # This next statement causes an open file dialogue to appear, and loads
    # csv_file_path with the name of the file (if any) selected by the user.
    csv_file_path = get_filename_from_dialog((
        ('comma-separated values', 'csv'),))

    # If the user closed the file dialogue without selecting a file,
    # csv_file_path will be the empty string, '', so this next if statement
    # guards against that possibility.
    if csv_file_path != '':
        # If execution got here, the user chose a csv file to open.
        # Python 3 has a csv module for handling csv files, but they can also
        # be opened for reading as simple text files.
        file = open(csv_file_path, 'r')
        # The next statement reads all the lines from the file into a
        # potentially very long string, and strips any blank lines at the ends.
        file_data = file.read().strip()
        # First, I'll split the string into a list of lines.
        lines = file_data.split('\n') # \n is the new-line character.
        # Then, I'll split each line at the commas
        for i in range(len(lines)):
            lines[i] = lines[i].split(',')
            # Finally, I'll convert the line elements to floats (numbers)
            for j in range(len(lines[i])):
                lines[i][j] = float(lines[i][j])
        # Now we can process the data from the file in its new form, lines,
        # which is a 2-d list of floats.
        for line in lines:
            line_sum = 0.0
            for val in line:
                print(val,'',end='') # print each value (on same line)
                line_sum += val
            print(line_sum) # print the sum and a new-line
    else:
        print ('No file selected.')

