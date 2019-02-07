import json

def encodeData(colonna, name="name"):
    countDistinctValues=len(set(colonna))
    distinctValues=list(set(colonna))
    encodingDict={}
    for idx, items in enumerate(distinctValues):
        encodingDict[items]=idx
    with open('encoding{}.json'.format(name), 'w') as fp:
        json.dump(encodingDict, fp)
    listToBeReturned=[]
    for idx, items in enumerate(colonna):
#         print('{}/{}'.format(idx, len(colonna)), end="\r")
        listToBeReturned.append(encodingDict[items])
    
    return listToBeReturned

def decodeData(colonna, name="name"):
    with open('encoding{}.json'.format(name), 'r') as fp:
        encodingDict=json.load(fp)
    listToBeReturned=[]
    for idx, items in enumerate(colonna):
        for key_, value_ in encodingDict.items():
            if value_ == items:
                listToBeReturned.append(key_)
    return listToBeReturned

