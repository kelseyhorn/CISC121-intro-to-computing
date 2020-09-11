"""
Kelsey Horn
20061821

This is the main function of the code that combines all other modules to
output the correct and incorrectly identified samples as well as the accuracy
"""

from extractData import readData, makeTrainingSet, makeTestSet
from makeClassifier import buildClassifier
from accuracyTest import testAccuracy

def main():
    #utilize functions 
    print('Reading in data')
    data = readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
    print('Making training and test files')
    testData = makeTestSet(data)
    trainingData = makeTrainingSet(data)
    print('Building classifier')
    moreThan50K, lessThan50K = buildClassifier(trainingData) 
    print('Classifying test data', '\n')
    numCorrect = testAccuracy(testData, moreThan50K, lessThan50K)

    #calculate required values
    Total = len(testData)
    numIncorrect = Total - numCorrect
    Accuracy = ((numCorrect/Total) * 100)

    #print out number of incorrect and correct and accuracy percentage
    print('Classified Correctly:', numCorrect)
    print('Classified Incorrectly:', numIncorrect)
    print('Accuracy:', '{:.2f}'.format(round((Accuracy), 2)),'%')
    
main()    
