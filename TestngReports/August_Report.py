import unittest

from HTMLTestRunner import HTMLTestRunner

from CRC_Report import Cluster_wise_file, Clusterwise_test, CRC_Blockwise, crc_cluster, CRC_distlist, CRC_District, \
    CRC_District_Details, CRC_download, CRCreports, dist_blk_clu, District_click_all, District_wise_file, \
    Districtwise_file, Districtwise_validation, map_cluster, Footer_data, Map_validation1, map_validation2, Select_Type, \
    Select_District_validate, Selecttype_files, TableData_District
from Dashboard import Click_on_SAR, Dashboard_menu, SAR_test, SR_click
from SAR_2.August_wise import blockdata_check, Blocks_Check, Blocks_random, Check_dist_blk, cluster_data_check, \
    cluster_dots_check, cluster_school_check, Cluster_validate, Cluster_wise, cluster_wise_check, Clusters_Button_Check, \
    D1_Block_Cluster, D1_Cluster10_Dots, D1_cluster_count, D2_Block_Dots, D20_Block, District_random, \
    District_Record_count, District_test, District_validation, Dots_schoolwise, Home_map, SAR_click, Schools_check, \
    validation_distblockcuster
from User_create import user_pwd_click, click_on_usercreate, Fillup_user, Negative_changepwd, set_new_password, \
    Roles_test
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        System_test = unittest.TestSuite()
        System_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(blockdata_check.Blockdata_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Blocks_Check.Block_validation),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Blocks_random.District_validation),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Check_dist_blk.block_validation),
            # unittest.defaultTestLoader.loadTestsFromTestCase(cluster_data_check.dist_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_dots_check.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_school_check.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_validate.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_wise.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_wise_check.blocks_Data_test),
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
            unittest.defaultTestLoader.loadTestsFromTestCase(validation_distblockcuster.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_wise_file.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(Clusterwise_test.table_recordtest),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_Blockwise.crc_cluster_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc_cluster.cluster_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_distlist.District_list),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_District.CRCtest_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_District_Details.crc_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_download.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRCreports.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(dist_blk_clu.District_recordtest),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_click_all.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_wise_file.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(Districtwise_file.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(Districtwise_validation.dwise_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(Footer_data.bar_details),
            unittest.defaultTestLoader.loadTestsFromTestCase(map_cluster.Map_blocks),
            unittest.defaultTestLoader.loadTestsFromTestCase(Map_validation1.Map_District),
            unittest.defaultTestLoader.loadTestsFromTestCase(map_validation2.Map_blocks),
            unittest.defaultTestLoader.loadTestsFromTestCase(Select_District_validate.District_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(Select_Type.Sel_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(Selecttype_files.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(TableData_District.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_SAR.Click_on_SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dashboard_menu.Dash_menu),
            unittest.defaultTestLoader.loadTestsFromTestCase(SAR_test.SAROption),
            unittest.defaultTestLoader.loadTestsFromTestCase(SR_click.Click_on_SR),
            unittest.defaultTestLoader.loadTestsFromTestCase(user_pwd_click.Click_on_pwd),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_usercreate.Click_create),
            unittest.defaultTestLoader.loadTestsFromTestCase(Fillup_user.Fillup_user),
            unittest.defaultTestLoader.loadTestsFromTestCase(Negative_changepwd.Click_ChangePwd),
            unittest.defaultTestLoader.loadTestsFromTestCase(set_new_password.Click_ChangePassword),
            unittest.defaultTestLoader.loadTestsFromTestCase(Roles_test.select_each_roles),




        ])
        # report = pwd()
        outfile = open("/home/chetan/cQube-New/Reports/TestExecution_Report.html", "w")

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