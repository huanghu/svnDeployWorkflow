'''
Created on 2013-10-14

@author: huanghu
'''

import os

class Common(object):
    def getCommonPath(self):
        filePath = os.path.abspath('conf') + "\path.txt"
        self.filePath = filePath
        return self.filePath