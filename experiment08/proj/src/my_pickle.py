"""
my_pickle - 

Author: 水果捞
Date: 2024/5/8
Github: https://github.com/yating1022
"""
import pickle
import os
from proj.config.settings import *
class MyPickle:
    def __init__(self,filename):
        self.filename = filename
    def write(self,data):
        with open(self.filename,'ab') as fp:
            pickle.dump(data,fp)
    def readiter(self):
        with open(self.filename,'rb') as fp:
            while  True:
                try:
                    data = pickle.load(fp)
                    yield data
                except:
                    break
    def delete(self,name):
        fp = MyPickle(self.filename+'.bak')
        for item in self.readiter():
            if item.name == name:
                pass
            else:
                fp.write(item)
        os.remove(self.filename)
        os.rename(self.filename+".bak",self.filename)
