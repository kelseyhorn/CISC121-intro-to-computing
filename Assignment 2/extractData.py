"""
Kelsey Horn
20061821

This module is used for reading the data and creating the test and training
data sets.
"""
import urllib.request 

def readData(url):
    """
    This function reads all the data contained in the given url.  It creates a dictionary for each line and adds this dictionary to a list.

    Parameters: 
        url: name of the url containing the data records

        Returns: a list of dictionaries
    """
    
    # This function is done - Do not modify.
    dataSet = []

    #Open the web page containing the data
    response = urllib.request.urlopen(url)
    
    #Read first line and remove new line indicator
    html = response.readline().rstrip()
    
    # Read in file
    while len(html) != 0:
        #data will contain a list with each element a different attribute
        lineList = html.decode('utf-8').split(",")

        # Create a dictionary for the line
        #   assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys
        record = {}
        record["age"] = float(lineList[0])
        record["workclass"] = lineList[1]
        record["educationnum"] = float(lineList[4])
        record["marital"] = lineList[5]
        record["occupation"] = lineList[6]
        record["relationship"] = lineList[7]
        record["race"] = lineList[8]
        record["sex"] = lineList[9]
        record["capitalgain"] = float(lineList[10])
        record["capitalloss"] = float(lineList[11])
        record["hours"] = float(lineList[12])
        record["class"] = lineList[14]

        # Add the dictionary to a list
        dataSet.append(record)

        #Read next line
        html = response.readline().rstrip()

    return dataSet

def makeTrainingSet(data):
    """"
    Makes a new list of dictionaries containing the first half of the records
    from the full data set (the parameter "data")
    
    Parameters:
        data - a list of dictionaries read from the url
    Returns:
        trainingData - a list of dictionaries (1/2 of data)
    """
    #take the length of half the training set
    halfLength = int(len(data)/2)
    #take rows up to half of the dataset for the training set  
    trainingData = data[:halfLength]
   
    return trainingData



def makeTestSet(data):
    """
    Create a test set of data from the second half of the data (ie. the
    second half of the data set (indicated by the parameter data).
    Add to each dictionary in this set a key called "predicted"
    and set it to "unknown".
    Paramters:
        data - a list of dictionaries (complete data read from url)
    Returns:
        testData - a list of dictionaries (second half of data file)
    """
    #take the length of half the training set
    halfLength = int(len(data)/2)
    
    #take rows starting at the halfway mark until the end
    testData = data[halfLength:]
    
    #add a "predicted" key to each dictionary and set to "unknown"
    for item in testData:
        item.update({"predicted":"unknown"})
    
    return testData


#testing goes here.  For each module you should show tests for each function.
if __name__ == "__main__":
    data = readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
    #trying to print all the data will probably make your program crash.
    #so, print the first and last values to check them.
    print(data[0])
    print(data[len(data)-1])
    print(len(data), "records have been read")
    
    #see what hald of the set would look like
    print ("Half of the records would be", int(len(data)/2))

    #check the length of the training data and print a sample
    trainingData = makeTrainingSet(data)
    print("The length of the training set is", len(trainingData))
    print(trainingData[0])
    
    #check the length of the test data and print a sample
    testData = makeTestSet(data)
    print("the length of the test set is", len(testData))
    print(testData[0], "\n")
    
    #see if the test and training sets add to the total set
    if len(trainingData)+len(testData) == len(data):
        print("The datasets are complete :)", "\n")
    else:
        print("something is wrong :(", "\n")
        
    #check that the test set includes the added 'predicted' key
    if 'predicted' in testData[0]:
        print("'predicted' key was found in dictionary")
    else:
        print("'predicted' key not found")

