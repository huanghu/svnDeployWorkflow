# -*- coding: utf-8 -*-
'''
Created on 2013-9-29

@author: huanghu
'''
from com.utils.common import Common

class Read(object):

    def getCommonValue(self ,key):
        path = Common().getCommonPath()
        value = self.read(path, key);
        return value
        

    def read(self ,path ,key):
        files = open(path ,"r")
        contents = files.readlines()
        for content in contents:
            index = content.index("=")
            contentKey = content[0:index]
            if contentKey == key :
                contentValue = content[index + 1: len(content)]
                #去掉回车换行
                return ''.join(contentValue.split())
        
        