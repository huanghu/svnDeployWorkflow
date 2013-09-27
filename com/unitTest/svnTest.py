# -*- coding: gbk -*-
'''
Created on 2013-9-21

@author: huanghu
'''
import unittest
from com.svn.getSvnInfo import SvnInfo


class Test(unittest.TestCase):
    
    def setUp(self):
        self.svn = SvnInfo();


    def testName(self):
        self.svn.svnCommand();


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()