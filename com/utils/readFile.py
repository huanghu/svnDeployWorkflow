# -*- coding: utf-8 -*-
'''
Created on 2013-9-29

@author: huanghu
'''

class Read(object):

    def read(self ,path ,key):
        files = open(path ,"r")
        contents = files.readlines()
        for content in contents:
            index = content.index("=")
            contentKey = content[0:index]
            if contentKey == key :
                contentValue = content[index + 1: len(content)]
                return contentValue
        
        