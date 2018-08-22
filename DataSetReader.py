import sys
import os
class DataSetReader:
    '''This class is used to read data set'''
    def __init__(self,file_path):
        self.path = sys.path[0] + "\\" + file_path
        self.data_list = []
        self.data_result = []

    def splitOriginalData(self,original_line):
        standard_list = []
        temp_line = original_line
        temp_line = temp_line.strip('\n')
        standard_list = temp_line.split(',')
        result = int(standard_list[-1])
        standard_list = standard_list[0:len(standard_list) - 1]
        return standard_list,result

    def ReadFile(self):
        try:
            open_file = open(self.path)
        except OSError:
            print("Failed to open the file")
        while True:
            line = open_file.readline()
            if len(line) == 0:
                break
            else:
                data_list,result = self.splitOriginalData(line)
                self.data_list.append(data_list)
                self.data_result.append(result)
        open_file.close()
        return self.data_list,self.data_result
   


        
