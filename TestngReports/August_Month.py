from HTMLTestRunner import HTMLTestRunner
import unittest

from Monthwise_validations.August_Validation import D1_cluster_count, D2_Block_Dots, D20_Block, D1_Block_Cluster, \
    D1_Cluster10_Dots, blockdata_check, Blocks_Check, Blocks_random, Chandloadiacluster, Check_dist_blk, cluster_jaliya, \
    Cluster_vankiya, Clusters_check, DBP_schoolwise, Dist_morbi, District_DevBhoomi, District_Gir, District_random, \
    district_Vadodara, Home_map, Khedadist, SAR_click, Schools_check, Simar_Una_test, una_block, \
    validation_distblockcuster


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Integration_test = unittest.TestSuite()
        Integration_test.addTests([
             # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(D1_cluster_count.AMH_schools),
            unittest.defaultTestLoader.loadTestsFromTestCase(D2_Block_Dots.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(D20_Block.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(D1_Block_Cluster.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(D1_Cluster10_Dots.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(blockdata_check.Blockdata_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Blocks_Check.Block_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Blocks_random.Surat_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Chandloadiacluster.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Check_dist_blk.cityblock_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_jaliya.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_vankiya.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Clusters_check.Clusters_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(DBP_schoolwise.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dist_morbi.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_DevBhoomi.DevBhooomi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_Gir.Gir_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(district_Vadodara.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Home_map.Sel_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(Khedadist.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(SAR_click.SAROption),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_check.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Simar_Una_test.simar_dist),
            unittest.defaultTestLoader.loadTestsFromTestCase(una_block.Una_blocks),
            unittest.defaultTestLoader.loadTestsFromTestCase(validation_distblockcuster.Schools_validation),





        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/August_validation.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Integration Testing of August month'

        )

        runner1.run(Integration_test)

if __name__ == '__main__':
    unittest.main()