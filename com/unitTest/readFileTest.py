'''
Created on 2013-9-29

@author: huanghu
'''
import unittest
from com.utils.readFile import Read

class ReadFileTest(unittest.TestCase):
    def setUp(self):
        self.read = Read()
        self.__path = "D:\Python\program\svnDeployWorkflow\conf\path.txt";

    def testName(self):
        self.read.read(self.__path ,'svn_path')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()