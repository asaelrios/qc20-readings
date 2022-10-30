import numpy as np
from bs4 import BeautifulSoup
from parse import compile

class qc20:

    # init requires the name of the renishaw b5r file 
    def __init__(self, filename) -> None:
        self.file = filename

        # Opens renishaw b5r analysis file
        with open(self.file, 'r', encoding = 'utf8') as f:
            self.data = f.read()

        # Parsing the data
        self.qc_data = BeautifulSoup(self.data, 'xml')

    # Returns both clockwise and counterclockwise readings as numpy array
    def readings(self):
        cw = self.cw_readings()
        ccw = self.ccw_readings()
        readings = np.concatenate((cw, ccw), axis=0)
        return readings


    # Returns only clockwise readings as numpy array
    def cw_readings(self):

        # Search for all the <READINGS> tags
        readings = self.qc_data.find_all('READINGS')
        readings_lists = len(readings)

        # Parsing argument to determine direction
        dir = compile("<RUN_DIRECTION>{}</RUN_DIRECTION>")
        

        for lists in range(readings_lists):

            # Taking one of the readings set found
            directions = readings[lists]

            # Look for the direction of the actual readings set
            run_dir = directions.find_previous_sibling('RUN_DIRECTION')

            # Taking the direction value
            rd = dir.parse(str(run_dir))


            # Parsing and converting the readings to a list
            directions_values = directions.text.split(' ')

            # Determines readings list size
            directions_len = len(directions_values)

            # Creating empty numpy array with the size of the readings list
            arr = np.zeros((1, directions_len))


            if(rd[lists - 1] == 'CW'):
            
                for values in range(directions_len):
                    arr[0][values] = directions_values[values]

                return arr

    # Returns only counterclockwise readings as numpy array
    def ccw_readings(self):

        # Search for all the <READINGS> tags
        readings = self.qc_data.find_all('READINGS')
        readings_lists = len(readings)

        # Parsing argument to determine direction
        dir = compile("<RUN_DIRECTION>{}</RUN_DIRECTION>")
        

        for lists in range(readings_lists):

            # Taking one of the readings set found
            directions = readings[lists]

            # Look for the direction of the actual readings set
            run_dir = directions.find_previous_sibling('RUN_DIRECTION')

            # Taking the direction value
            rd = dir.parse(str(run_dir))


            # Parsing and converting the readings to a list
            directions_values = directions.text.split(' ')

            # Determines readings list size
            directions_len = len(directions_values)

            # Creating empty numpy array with the size of the readings list
            arr = np.zeros((1, directions_len))

            if(rd[lists - 1] == 'CCW'):
            
                for values in range(directions_len):
                    arr[0][values] = directions_values[values]

                return arr
