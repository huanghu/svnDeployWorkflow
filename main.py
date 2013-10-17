# -*- coding: utf-8 -*-
'''
Created on 2013-10-16

@author: huanghu
'''
from com.opXml.getWorkflowName import WorkflowName
from com.utils.readFile import Read

if __name__ == '__main__':
    s_message = '输入svn版本号：'
    svnVersion = raw_input(s_message.decode('utf-8').encode('gbk'))
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