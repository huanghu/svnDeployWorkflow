# -*- coding: utf-8 -*-
'''
Created on 2013-9-21

@author: huanghu
'''
from com.opXml.getWorkflowName import WorkflowName
from com.utils.readFile import Read
import os

if __name__ == '__main__':
    svnVersion = raw_input('输入svn版本号：')
    '''
    从svn获得版本号，或许需要改为从输入参数获得
    '''
    
    '''
    递归目录，获得workflow名称，然后将其所在的目录打包
    '''

    codeVersionName = 'code_version'
    codeVersion = Read().getCommonValue(codeVersionName)
    workflow = WorkflowName(svnVersion ,codeVersion)
    path_name_conf = 'workflow_dir_path'
    path = workflow.getWorkflowDirPath(path_name_conf);
    workflow.getWorkflowPathByRecursive(path)
