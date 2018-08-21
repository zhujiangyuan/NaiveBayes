from pandas import *
from numpy import *

def createDataSet():
    postinglist=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]
    return postinglist, classVec

def createVocaList(postingList):
    vocalSet = set([])
    for line in postingList:
        vocalSet = vocalSet|set(line) # "|" 并集
    return vocalSet

def dataSet2Vec(vocalSet,input):
    vocalList = list(vocalSet)
    num_vocal = len(vocalList)
    num_lines = len(input)
    returnVec = zeros((num_lines,num_vocal))
    for i in range(num_lines):
        for j in range(len(input[i])):
            if input[i][j] in vocal_Set:
                t = input[i][j]
                returnVec[i][vocalList.index(t)] = 1
            else:
                print("")
    return returnVec

def train_dataset(vocal_Vector,classVec):
    num_lines=len(vocal_Vector)
    num_words_in_line=len(vocal_Vector[0])
    count_abusive_list=zeros(num_words_in_line)
    count_no_abusive_list=zeros(num_words_in_line)
    num_Abusive=sum(classVec)
    pAbusive=num_Abusive/float(num_lines)
    for i in range(num_lines):
        if classVec[i] == 1:
            count_abusive_list = count_abusive_list + vocal_Vector[i]
        else:
            count_no_abusive_list = count_no_abusive_list + vocal_Vector[i]
    list_pAbusive = -log((count_abusive_list+0.1)/(sum(count_abusive_list) + 0.1))
    list_pnoAbusive = -log((count_no_abusive_list + 0.1) / (sum(count_no_abusive_list) + 0.1))
    return list_pAbusive, list_pnoAbusive, pAbusive

def classify(voc_to_list, list_pAbusive, list_pnoAbusive, pAbusive):
    num = len(voc_to_list[0])
    list_Abusive=voc_to_list*list_pAbusive
    list_no_Abusive = voc_to_list*list_pnoAbusive
    sum_abusive = 0.0
    sum_no_abusive = 0.0
    for i in range (num):
        if list_Abusive[0][i]>0:
            sum_abusive += list_Abusive[0][i]
        if list_no_Abusive[0][i] >0:
            sum_no_abusive += list_no_Abusive[0][i]

    if (sum_abusive*pAbusive) <= (sum_no_abusive*(1-pAbusive)):
        print("Abusive")
    else:
         print("OK") 

postingList,classVec=createDataSet() #生成数据集
vocal_Set=createVocaList(postingList)  #将训练机转化为set格式
returnVec=dataSet2Vec(vocal_Set,postingList)
list_pAbusive,list_pnoAbusive,pAbusive = train_dataset(returnVec, classVec)
myinput=[['stupid', 'garbage']]
myinput_vector = dataSet2Vec(vocal_Set, myinput)
classify(myinput_vector, list_pAbusive, list_pnoAbusive, pAbusive)