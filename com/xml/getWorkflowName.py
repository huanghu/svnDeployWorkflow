# -*- coding: utf-8 -*-
'''
Created on 2013-10-10

@author: huanghu
'''
from com.utils.readFile import Read
import os

class WorkflowName(object):
    '''
        通过xml获得workflow的名称
    '''
    
    def __init__(self):
        self.dirPath = None
    
    #path_name_conf path.txt中的workflow_dir_path
    def getWorkflowDirPath(self ,path_name_conf):
        read = Read()
        filePath = os.path.abspath("../../conf") + "/path.txt"
        dirPath = read.read(filePath, path_name_conf)
        return dirPath
    
    #递归获得工作流的路径
    def getWorkflowPathByRecursive(self ,dirPath):
        #获得目录下所有文件的内容
        dirs = os.listdir(dirPath)
        for dirSin in dirs:
            rootPath = dirPath
            rootPath = '%s/%s' % (rootPath ,dirSin)
            isDir = os.path.isdir(rootPath)
            if isDir is True:
                #如果是目录，递归
                self.getWorkflowPathByRecursive(rootPath)
            else:
                #在这里获得工作流名称，然后部署
                print rootPath
                
        
        