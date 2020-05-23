import sys
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from Data.parameters import Data
from TS import click_on_cqube_login
pwd = Data()
sys.path.append(pwd.get_system_path())

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_cqube_login.CqubeLogin)

        ])
        html_report_generate_path = Data()
        outfile = open(html_report_generate_path.get_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity=1,
            description='Smoke Tests'

        )

        runner1.run(smoke_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()
