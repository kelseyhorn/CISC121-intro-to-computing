"""
Kelsey Horn
20061821

This module builds the classifier.
"""

from extractData import readData, makeTrainingSet, makeTestSet


def buildClassifier(trainingData):
    """
    Create a classifier which takes in a training set and builds
    a model for >50K income and <=50K income by calculating the 
    averages of the various attributes
    Parameters:
        trainingData - a list of dictonaries created from half
                       the dataset
    Returns:
        classifier - 
    """
    #define what are the numerical and categorical keys
    numerical = ["age", "educationnum", "capitalgain", "capitalloss", "hours"]
    categorical = ["workclass", "marital", "occupation", "relationship", "race", "sex"]

    #set blank dictionary for class <50K
    moreThan50K = {
        'age': 0,
        'workclass': {'Private' : 0, 'Self-emp-not-inc' : 0, 'Self-emp-inc' : 0, 'Federal-gov' : 0, 
                      'Local-gov' : 0, 'State-gov' : 0, 'Without-pay' : 0, 'Never-worked' : 0},
        'educationnum': 0,
        'marital': {'Married-civ-spouse' : 0, 'Divorced' : 0, 'Never-married' : 0, 'Separated' : 0, 'Widowed' : 0, 
                    'Married-spouse-absent' : 0, 'Married-AF-spouse' : 0},
        'occupation' : {'Tech-support' : 0, 'Craft-repair' : 0, 'Other-service' : 0, 'Sales' : 0, 'Exec-managerial' : 0
                        ,'Prof-specialty' : 0, 'Handlers-cleaners' : 0, 'Machine-op-inspct' : 0, 'Adm-clerical' : 0, 
                        'Farming-fishing' : 0, 'Transport-moving' : 0, 'Priv-house-serv': 0, 'Protective-serv' : 0
                        , 'Armed-Forces' : 0},
        'relationship' : {'Wife' : 0, 'Own-child' : 0, 'Husband' : 0, 'Not-in-family' : 0, 'Other-relative' : 0
                          , 'Unmarried' : 0},
        'race' : {'White' : 0, 'Asian-Pac-Islander' : 0, 'Amer-Indian-Eskimo' : 0, 'Other' : 0, 'Black' : 0},
        'sex' : {'Female' : 0, 'Male' : 0},
        'capitalgain' : 0.0,
        'capitalloss': 0.0,
        'hours': 0
    }

    #set blank dictionary for class <=50K
    lessThan50K = {
        'age': 0,
        'workclass': {'Private' : 0, 'Self-emp-not-inc' : 0, 'Self-emp-inc' : 0, 'Federal-gov' : 0, 
                      'Local-gov' : 0, 'State-gov' : 0, 'Without-pay' : 0, 'Never-worked' : 0},
        'educationnum': 0,
        'marital': {'Married-civ-spouse' : 0, 'Divorced' : 0, 'Never-married' : 0, 'Separated' : 0, 'Widowed' : 0, 
                    'Married-spouse-absent' : 0, 'Married-AF-spouse' : 0},
        'occupation' : {'Tech-support' : 0, 'Craft-repair' : 0, 'Other-service' : 0, 'Sales' : 0, 'Exec-managerial' : 0
                        ,'Prof-specialty' : 0, 'Handlers-cleaners' : 0, 'Machine-op-inspct' : 0, 'Adm-clerical' : 0, 
                        'Farming-fishing' : 0, 'Transport-moving' : 0, 'Priv-house-serv': 0, 'Protective-serv' : 0
                        , 'Armed-Forces' : 0},
        'relationship' : {'Wife' : 0, 'Own-child' : 0, 'Husband' : 0, 'Not-in-family' : 0, 'Other-relative' : 0
                          , 'Unmarried' : 0},
        'race' : {'White' : 0, 'Asian-Pac-Islander' : 0, 'Amer-Indian-Eskimo' : 0, 'Other' : 0, 'Black' : 0},
        'sex' : {'Female' : 0, 'Male' : 0},
        'capitalgain' : 0.0,
        'capitalloss': 0.0,
        'hours': 0
    }
    #initialize counter values for both class options
    k = 0
    j = 0

    #iter over all lines
    for i in range(len(trainingData)):
        #set data as the variable for each new line
        data = trainingData[i]

        #extract the class key and its variable
        d = data['class']

        #code for over 50K class
        if d == '>50K':
            k += 1
            
            #for each key and value in the line
            for key, val in data.items():
                if key in numerical:
                    #add to key value of classifier every iteration of numerical data
                    moreThan50K[key] += float(val)
                if key in categorical:
                    #count how many times key words appear in categorical data
                    #the value of the key is used as the new key in the nested dictionary
                    moreThan50K[key][val] += 1

        #repeat the same process for the <= 50K condition
        else:
            j += 1
            for key, val in data.items():
                if key in numerical:
                    lessThan50K[key] += float(val)
                if key in categorical:
                    lessThan50K[key][val] += 1

    #calculate the averages of each key value
    for key in moreThan50K:  
        if key in numerical:
            moreThan50K[key] =  round(moreThan50K[key]/k, 5)
            lessThan50K[key] =  round(lessThan50K[key]/j, 5)
        else:
            #for nested dictionaries calculate the frequency within each key
            k1 = key
            for key in moreThan50K[k1]:
                moreThan50K[k1][key] =  round(moreThan50K[k1][key]/k, 5)
                lessThan50K[k1][key] =  round(lessThan50K[k1][key]/j, 5)
            
    
    return moreThan50K, lessThan50K

if __name__ == "__main__":
    #testing for classifier 
    data = readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
    trainingData = makeTrainingSet(data)
    
    #check to make sure data looks accurate for each specification
    moreThan50K, lessThan50K = buildClassifier(trainingData)
    print (moreThan50K, "\n")
    print (lessThan50K, "\n")
    #make sure categorical data adds to 100%
    print('Percent sex adds to a total of =', (moreThan50K['sex']['Female'] + moreThan50K['sex']['Male'])*100, '%')

