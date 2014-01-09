'''
Created on 2014-1-9

@author: huanghu
'''
import unittest
from com.deploy.deployToZip import Deploy


class Test(unittest.TestCase):


    def testName(self):
        workflowPath = ''
        workflowDirName = ''
        deploy = Deploy(workflowPath ,workflowDirName)
        deploy.copyJar();
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()