# -*- coding: gbk -*-
'''
Created on 2013-9-21

@author: huanghu
'''
import os

class SvnInfo(object):
    '''
    classdocs
    '''

    def svnCommand(self):
        file = os.path.abspath("../../conf") + "\path.txt"
        
#        file = open("../../")
#        command = "D:\Java\program\ebsdi\maven.1379495293888";
#        os.chdir(command)
#        command = "svn info > info.txt"
#        os.system(command)
        