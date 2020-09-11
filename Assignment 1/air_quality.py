"""
This module provides functions that return the Air Quality Health Index (as
calculated for Canada) and corresponding Risk level based on external input.

Functions:

aqhi (o3, no2, pm25)
    Returns the Air Quality Health Index (AQHI) associated with these
    parameters: ozone , nitrougen dioxide, and fine particulate matter.

risk_level (aqhi)
    Returns a string representing the Risk level (low, moderate, high, or
    very high) associated with aqhi, a number representing an Air Quality
    Health Index.

R. Linley
2019-08-30
"""

import math

def calc_aqhi (o3, no2, pm25):
    """Returns the Air Quality Health Index (AQHI) associated with these
    parameters: ozone , nitrougen dioxide, and fine particulate matter.

    Arguments:

    o3 - A number representing a three-hour average concentration of
        ground-level ozone, measured in parts per billion (ppb).

    no2 - A number representing a three-hour average concentration of
        nitrogen dioxide, measured in ppb.

    pm25 - A number representing a three-hour average concentration of fine
        (2.5 micrometres or less diameter) particulate matter, measured in
        micrograms per cubic metre.

    Calculation source:
    https://en.wikipedia.org/wiki/Air_Quality_Health_Index_(Canada)#Calculation
    """
    
    aqhi = (1000/10.4)*((math.exp(0.000537*o3) - 1) + (math.exp(0.000871*no2) - 1) + (math.exp(0.000487*pm25) - 1)) 

    aqhi = math.ceil(aqhi)
    
    return aqhi

def risk_level (aqhi):
    if aqhi >= 1 and aqhi <=3:
        level = 'Low'
    elif aqhi >= 4 and aqhi <= 6:
        level = 'Moderate'
    elif aqhi >= 7 and aqhi <= 10:
        level = 'High'
    elif aqhi >= 11:
        level = 'Very High'
    else:
        level = 'Not a Valid Number'
    
    return level # Replace with working code.

if __name__ == '__main__':
    # Testing!
    for i in range(60):
        val = calc_aqhi(i, i, i)
        print (i, val, '(' + risk_level(val) + ')')
        
