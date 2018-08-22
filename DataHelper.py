from numpy import *

def createVocaList(postingList):
    vocalSet = set([])
    for line in postingList:
        vocalSet = vocalSet|set(line) 
    return vocalSet

def dataSet2Vec(vocalSet,input):
    vocalList = list(vocalSet)
    num_vocal = len(vocalList)
    num_lines = len(input)
    returnVec = zeros((num_lines,num_vocal))
    for i in range(num_lines):
        for j in range(len(input[i])):
            if input[i][j] in vocalList:
                t = input[i][j]
                returnVec[i][vocalList.index(t)] = 1
            else:
                print("")
    return returnVec