"""
This module provides a simple read function for any comma-separated values
(csv) file that contains only numeric data, commas, and new lines.
Such a file may look like this:

    12.3,13,11,6,0,-28.2
    -5,6.23,7.71,18.34,-12,1
    44,17.2,3.54,6.783,21.7,4
    ...

(though the number of values stored on each line may vary). Blank lines in the
data are not allowed, however any blanks (whitespace or empty lines) before or
after the lines containing data will be stripped before processing by the read
function.

Function:

read_csv (filename)
    Returns a two-dimensional list of floating-point numbers extracted from
    the file specified by filename.

R. Linley
2019-08-31
"""
import csv

def read_csv (filename):
    """Returns a two-dimensional list of floating-point numbers extracted from
    the file specified by filename, a comma-separated values file containing
    only numbers, commas (separating the numbers), and newlines (at the end of
    each data row). It is assumed that the data doesn't contain any blank
    lines, however, any blanks (whitespace or empty lines) before or after the
    lines containing data will be stripped before processing. filename is
    assumed to contain a valid file name (and path).

    Example: Given the filename of a csv file that looks like this:
    
        27.6,19.8,12.9
        28.8,18.6,13.5
        30,15.6,13.8
        
    the 2d list returned by this function would be:
    
        [[27.6, 19.8, 12.9], [28.8, 18.6, 13.5], [30.0, 15.6, 13.8]]
    """
    print(filename)
    with open (filename, 'r') as csvFile:
        reader = csv.reader(csvFile, skipinitialspace=True)
        lines = list(reader)   
            
    
    return lines

if __name__ == '__main__':
    # Testing!
    import file_dialog
    fn = file_dialog.get_filename_from_dialog(
        (('comma-separated values','csv'),))
    if fn != '':
        print(fn)
        data = read_csv(fn)
        for row in data:
            print (row)
    else:
        print('No file selected.')
    
