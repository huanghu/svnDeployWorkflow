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
        filePath = os.path.abspath("../../conf") + "\path.txt"
        self.dirPath = read.read(filePath, path_name_conf)
    
    #递归获得工作流的路径
    def getWorkflowPathByRecursive(self ,path_name_conf):
        self.getWorkflowDirPath(path_name_conf);
        
        
        
        