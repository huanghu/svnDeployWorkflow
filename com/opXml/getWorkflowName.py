# -*- coding: utf-8 -*-
'''
Created on 2013-10-10

@author: huanghu
'''
from com.utils.readFile import Read
import os
from com.utils.common import Common
from com.deploy.deployToZip import Deploy
from xml.dom import minidom

class WorkflowName(object):
    '''
        通过xml获得workflow的名称
    '''
    
    def __init__(self ,svnVersion ,codeVersion):
        self.dirPath = None
        self.svnVersion = svnVersion
        self.codeVersion = codeVersion
    
    #path_name_conf path.txt中的workflow_dir_path
    def getWorkflowDirPath(self ,path_name_conf):
        read = Read()
#        filePath = os.path.abspath("../../conf") + "/path.txt"
        common = Common()
        filePath = common.getCommonPath();
        dirPath = read.read(filePath, path_name_conf)
        return dirPath
    
    #递归获得工作流的路径
    def getWorkflowPathByRecursive(self ,dirPath):
        if dirPath.find(".svn") >= 0:
            return
        
        #获得目录下所有文件的内容
        dirPath = ''.join(dirPath.split())
        dirs = os.listdir(dirPath)
        for dirSin in dirs:
            rootPath = dirPath
            rootPath = '%s%s%s' % (rootPath , '\\' ,dirSin)
            isDir = os.path.isdir(rootPath)
            #如果是目录，并且存在workflow.xml,打包部署，返回
            #否则，递归
            if isDir is False:
                #如果是文件，判断是否是workflow.xml，如果是，部署
                flagString = 'job.properties'
                name = 'workflow.xml'
                josIndex = rootPath.find(flagString)
                if josIndex >= 0:
                    #部署
                    #工作流目录路径
                    workflowPath = rootPath.replace(flagString, '')
                    #工作流路径
                    workflowFilePath = '%s\%s' % (workflowPath ,name)
                    #部署之后的目录的名称
                    #格式${workflwname}-${codeVersion}-${svnVersion}
                    targetName = '%s-%s-%s' % (self.getWorkflowName(workflowFilePath) ,self.codeVersion ,self.svnVersion)
                    deploy = Deploy(dirPath ,targetName)
                    deploy.copy()
                    return
            else:
                self.getWorkflowPathByRecursive(rootPath)
                
    #获得工作流名称
    def getWorkflowName(self ,workflowPath):
        doc = minidom.parse(workflowPath)
        root = doc.documentElement
        #获得根节点的attributes,其他
        return root.attributes.get('name').nodeValue
        