# -*- coding: utf-8 -*-
'''
Created on 2013-9-21

@author: huanghu
'''
import os
from com.utils.readFile import Read

class SvnInfo(object):
    
    def __init__(self):
        self.read = Read()
        self.workPath = ''

    #执行svn命令，将svn 信息放入info.txt文件夹
    def svnCommand(self):
        filePath = os.path.abspath("../../conf") + "\path.txt"

        key = "svn_path";
        self.workPath = self.read.read(filePath, key)
        os.chdir(self.workPath)
        command = "svn info > info.txt"
        os.system(command)
        
    def getSvnInfo(self):
        self.svnCommand()
        
        #info.txt文件的路径
        infoPath = self.workPath + '/info.txt'
        key = '版本'
        svnInfo = self.read.read(infoPath, key);
        print svnInfo
        
        
        
        