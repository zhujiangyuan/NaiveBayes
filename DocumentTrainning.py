from numpy import *
from pandas import *
import DataHelper

class Training:
    '''This class is used to training data set'''
    def __init__(self, data_list, result_list):
        self.data_list = data_list
        self.result_list = result_list 
    
    def TraningPrepare(self):
        self.data_set = DataHelper.createVocaList(self.data_list)
        self.data_vector = DataHelper.dataSet2Vec(self.data_set, self.data_list)
        
    def TrainData(self):
        self.TraningPrepare()
        num_lines=len(self.data_vector)
        num_words_in_line=len(self.data_vector[0])
        count_abusive_list=zeros(num_words_in_line)
        count_no_abusive_list=zeros(num_words_in_line)
        num_Abusive=sum(self.result_list)
        pAbusive=num_Abusive/float(num_lines)
        for i in range(num_lines):
            if self.result_list[i] == 1:
                count_abusive_list = count_abusive_list + self.data_vector[i]
            else:
                count_no_abusive_list = count_no_abusive_list + self.data_vector[i]
        list_pAbusive = count_abusive_list / (sum(count_abusive_list))
        list_pnoAbusive = (count_no_abusive_list) / (sum(count_no_abusive_list))
        return list_pAbusive, list_pnoAbusive, pAbusive
