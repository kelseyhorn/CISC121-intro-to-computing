import file_dialog
import air_quality
from input_numbers import input_float
import menu
import numbers_csv
from numbers_csv import read_csv

def main():
    m = ['Calculate an Air Quality Health Index (AQHI)',
            'Calculate AQHIs from a file']
    while True:
        choice = menu.do_menu('What would you like to do?',m)

        if choice is None: # Exit menu choice was made.
            break # Break out of loop, end program.

        print()

        if choice == 1:
            ozone = input_float('Ozone level: ')
            nitrogen_dioxide = input_float('Nitrogen dioxide level: ')
            fine_particulate_matter = input_float(
                'Fine particulate matter level: ')
            aqhi = air_quality.calc_aqhi(ozone, nitrogen_dioxide,
                                         fine_particulate_matter)
            print()
            print('AQHI is',aqhi,
                  '(' + air_quality.risk_level(aqhi) + ').')

        elif choice == 2:
            filename = file_dialog.get_filename_from_dialog(
                (('comma-separated values','csv'),))
            print('Reading data from file',filename)
            data = read_csv(filename) 
            for row in data:
                aqhi = air_quality.calc_aqhi(float(row[0]),float(row[1]),float(row[2]))
                print('AQHI is',aqhi,
                '   (' + air_quality.risk_level(aqhi) + ').')
        
main()

