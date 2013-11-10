# -*- coding: utf-8 -*-
'''
Created on 2013-10-10

@author: huanghu
'''
import unittest
from com.opXml.getWorkflowName import WorkflowName


class Test(unittest.TestCase):

    def setUp(self):
        svnVersion = '11111'
        codeVersion = '0.4.001'
        self.workflow = WorkflowName(svnVersion ,codeVersion)

    def testName(self):
#        path_name_conf = 'workflow_dir_path'
#        path = self.workflow.getWorkflowDirPath(path_name_conf);
        path = "D:\Java\program\ebsdi-test\ebsdi-apps\src\main\\resources\main\\vendor\qlDhc";
        self.workflow.getWorkflowPathByRecursive(path)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()