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
        command = "svn info > info.txt"
        os.system(command)
    

        