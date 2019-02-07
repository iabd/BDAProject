def countDistinctValues(df, columnsList=None):
    if not columnsList:
        columnsList=list(df.columns)
    distinctValuesDict={}
    for column in columnsList:
        try:
            distinctValuesDict[column]=len(set(df[str(column)]))
        except:
            print("the column {} doesn't belong to the dataframe provided".format(column))
            pass
    return distinctValuesDict


def generalizeLocations(listOfLocations):
    generalizedListOfLocations=[]
    for location in listOfLocations:
        try:
            tempVar=location.replace('On or near ', '')
        except:
            pass
        if tempVar.isupper():
            tempVar="Other particular location"
        generalizedListOfLocations.append(tempVar)
    return generalizedListOfLocations


def generalizeNames(listOfLsoaNames):
    generalizedNames=[]
    for names in listOfLsoaNames:
        generalizedNames.append(names[:-5])
    return generalizedNames

