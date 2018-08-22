import os
from DataSetReader import DataSetReader
from DocumentClassifyTrainning import Training

dataset = DataSetReader("DataSet.txt")
data_list,result_list = dataset.ReadFile()
myTraining = Training(data_list, result_list)
list_pAbusive, list_pnoAbusive, pAbusive = myTraining.TrainData()

print ("Finish!")
