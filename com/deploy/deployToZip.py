# -*- coding: utf-8 -*-
'''
Created on 2013-10-14

@author: huanghu
'''
import os
from com.utils.readFile import Read
from com.utils.common import Common

#部署到制定目录下，而且压缩为zip
class Deploy(object):
    
    '''
        @workflow_path workflow.xml路径
        @workflowDirName 工作流所在目录名称
    '''
    def __init__(self ,workflowPath ,workflowDirName):
        self.workflow_path = workflowPath;
        #工作流的目录名称
        self.workflowDirName = workflowDirName;
        
    def copy(self):
        self.getPath();
        self.deleteMkdir();
        self.copyXml();
        self.copyJar();

    def deleteMkdir(self):
        command = "rd " + self.target_path + " /s /q";
        os.system(command);
        
    def copyXml(self):
        command = "xcopy /s " + self.workflow_path + " " + self.target_path;
        print command
        os.system(command);
        
    def copyJar(self):
        key = 'svn_path';
        svn_path = Read().getCommonValue(key)
        
        jars_key = 'jars';
        jars = Read().getCommonValue(jars_key);
        
        jar_arr = jars.split(',')
        target_lib_path = self.target_path + "\lib\\";
        for jar in jar_arr:
            jar_path = svn_path + "\\" + jar + "\\target\\" + jar + ".jar";
            print 'jar_path' + jar_path
            command = "xcopy " + jar_path + " " + target_lib_path;
            os.system(command);

    def getPath(self):
        read = Read();
        common = Common()
        filePath = common.getCommonPath();
        self.target_path = read.read(filePath, 'target_path');
        
        self.target_path = self.target_path + "\\" + self.workflowDirName + "\\"
        
        
    def formatStr(self ,item):
        #item_f = item.decode('unicode_escape').strip();
        item_f = item.decode('utf-8').encode('gbk').strip();
        return item_f;
        
    def test(self):
        command = "xcopy " + self.workflow_path + " " + self.target_path;
        os.system(command);
        