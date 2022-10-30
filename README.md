# qc20-readings
## Renishaw ballbar qc20 readings 

Converting Renishaw ballbar qc20 readings to numpy arrays. Use the b5r file generated from the ballbar test to generate a numpy arrary.

## Description & Usage

This project is only a set of functions to convert the readings values of the ballbar test to numpy arrays. The ballbar test generated file is an xml file, even do it has a ".b5r" extension, it contains descriptions about the conditions of the test and two sets of readings, clockwise (CW) and counterclockwise (CCW), derived from the use of the G02 and G03 codes respectively.

#### **readings():

This returns both clockwise and counterclockwise sets of readings as a numpy array.

#### **cw_readings():

This returns the values of the clockwise readings as a numpy array.

#### **ccw_readings():

This returns the values of the counterclockwise readings as a numpy array.

### Initialaze the qc20 class 
Python: qc20('path\filename')

### Example
import qc20

reni = qc20('YZ_220grad_150mm-120924.b5r')

array = reni.readings()

print(array)


