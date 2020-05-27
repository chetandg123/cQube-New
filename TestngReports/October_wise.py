import unittest

from HTMLTestRunner import HTMLTestRunner

from SAR_2.October_wise import  Clusters_Button_Check, \
    D1_Block_Cluster, D1_Cluster10_Dots, D1_cluster_count, D2_Block_Dots, D20_Block, District_random, \
    District_Record_count, District_test, District_validation, Dots_schoolwise, Home_map, SAR_click, Schools_check, \
    validation_distblockcuster
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        System_test = unittest.TestSuite()
        System_test.addTests([
            # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Clusters_Button_Check.Clusters_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(D1_Block_Cluster.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(D1_Cluster10_Dots.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(D1_cluster_count.schools_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(D2_Block_Dots.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(D20_Block.Dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_random.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_Record_count.dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_test.Dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_validation.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dots_schoolwise.dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Home_map.Sel_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(SAR_click.SAROption),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_check.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(validation_distblockcuster.Schools_validation)




        ])
        # report = pwd()
        outfile = open("/home/chetan/cQube-New/Reports/October_report.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title = 'Test Report',
            verbosity = 1,
            description = 'System Tests'

        )

        runner1.run(System_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()