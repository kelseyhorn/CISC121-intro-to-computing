"""
Kelsey Horn
20061921

This module tests the accuracy of the classifier using the test data.
"""


from extractData import readData, makeTrainingSet, makeTestSet
from makeClassifier import buildClassifier

def testAccuracy(testData, moreThan50K, lessThan50K):
    """
    Using the testing set, test to see if the accuracy of the classifier
    by using the models for >50K and <=50K to classify the test data.
    Then, compare the predictions to the real values. 
    Parameters:
        testData - half of the original data set aside for testing 
        moreThan50K - model with averages for data over 50K
        lessThan50K - model with averages for data less than or equal to 50K
    Returns:
        numCorrect - number of correctly classified sets
    """
    #define what are the numerical and categorical keys
    numerical = ["age", "educationnum", "capitalgain", "capitalloss", "hours"]
    categorical = ["workclass", "marital", "occupation", "relationship", "race", "sex"]

    for i in range(len(testData)):
        #initialize counting for both classifiers
        less = 0
        more = 0
        
        #set data as one line of the test data
        data = testData[i]
        
        #for each key and value in the set
        for key, val in data.items():
            if key in numerical:
                #if the difference in the lessThan is greater than the moreThan add a 'point' to less otherwise to more
                if abs(val - moreThan50K[key]) > abs(val - lessThan50K[key]): 
                    less += 1
                else:
                    more += 1
            #whichever classifier has a higher value for the testData key, add a 'point' tothat one
            if key in categorical:
                k1 = key
                data1 = data[k1]
                if moreThan50K[k1][data1] < lessThan50K[k1][data1]:
                    less += 1
                else:
                    more += 1
                    
        #update the predicted value in the dictonary to include the classifier prediction
        #if there are more points for more than classify as >50K otherwise classify as <=50K
        if less < more:
            testData[i]['predicted'] = '>50K'
        else:
            testData[i]['predicted'] = '<=50K'

    #initialize correct number counter
    numCorrect = 0
    
    #test the entire list against the class key value to count how many are correct
    for i in range(len(testData)):
        if testData[i]['predicted'] == testData[i]['class']:
            numCorrect += 1
        
    return numCorrect

if __name__ == "__main__":
    #testing for classifier 
    data = readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
    testData = makeTestSet(data)
    trainingData = makeTrainingSet(data)
    moreThan50K, lessThan50K = buildClassifier(trainingData) 
    numCorrect = testAccuracy(testData, moreThan50K, lessThan50K) 
    print (testData[0], '\n')
    print ('>50K =', moreThan50K, "\n")
    print ('<=50K =', lessThan50K, "\n")

    #manually comparing values in testData and classifiers 
    print('looking at it manually'
          , "\n", 'age = >50K'
          , "\n", 'workclass = <=50K'
          , "\n", 'eductionnum = <=50K'
          , "\n", 'marital = >50K'
          , "\n", 'occupation = <=50K'
          , "\n", 'relationship = >50K'
          , "\n", 'race = >50K'
          , "\n", 'sex = >50K'
          , "\n", 'capitalgain = <=50K'
          , "\n", 'capitalloss = <=50K'
          , "\n", 'capitalloss = <=50K'
          , "\n", 'hours = <=50K'
          , "\n", 'class = <+50K, predicted should be <=50K according to classifier (6 to 5)'
          , "\n", 'actual predicted = <+50 = good!')
      

