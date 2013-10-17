# -*- coding: utf-8 -*-
'''
Created on 2013-10-10

@author: huanghu
'''
import unittest
from com.xml.getWorkflowName import WorkflowName


class Test(unittest.TestCase):

    def setUp(self):
        svnVersion = '11111'
        codeVersion = '0.4.001'
        self.workflow = WorkflowName(svnVersion ,codeVersion)

    def testName(self):
        path_name_conf = 'workflow_dir_path'
        path = self.workflow.getWorkflowDirPath(path_name_conf);
        self.workflow.getWorkflowPathByRecursive(path)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()