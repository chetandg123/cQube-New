import unittest

from HTMLTestRunner import HTMLTestRunner

from SAR_2.September_wise import Blocks_random, Check_dist_blk, cluster_data_check, cluster_dots_check, \
    cluster_school_check, Cluster_validate, Cluster_wise, cluster_wise_check, Clusters_Button_Check, D1_Block_Cluster, \
    D1_Cluster10_Dots, D1_cluster_count, D2_Block_Dots, D20_Block, District_random, District_Record_count, \
    District_test, District_validation
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        System_test = unittest.TestSuite()
        System_test.addTests([
            # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Blocks_random.District_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Check_dist_blk.Block_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_data_check.District_check),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_dots_check.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_school_check.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_validate.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_wise.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_wise_check.Blocks_Wise_test),
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

        ])
        # report = pwd()
        outfile = open("/home/chetan/cQube-New/Reports/September_report.html", "w")

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